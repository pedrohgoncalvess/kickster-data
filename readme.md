# Football data

## Oque é

Este é um script de populamento que coleta dados de futebol. Ele usa a [API FOOTBALL](https://www.api-football.com/documentation-v3#section/Introduction) que tem plano free então você (com paciencia) pode popular
seu banco sem precisar gastar, o ideal é que você assine a API de acordo com a sua demanda. O plano free tem o limite de 200 requests diarias que esgota com bastante facilidade. Essa API tem dados de diferentes ligas então pode você analisar os dados
das ligas que bem entender, mas claro, como mencionado anteriormente você pode assinar a API para aumentar o seu limite de requests e conseguir popular e atualizar as suas informações de maneira mais rápida.  
O banco usado foi o **PostgreSQL** mas claro, você pode adaptar o código e o build do banco para a sua preferencia.  

**Essa é uma parte essencial de um projeto maior o qual eu não vou falar sobre e muito provavelmente não vou deixar público as próximas partes do projeto.**

## Schema do banco de dados

Eu construi o arquivo build.sql (que é importado automaticamente no docker-compose) com base nas informações que fui coletando lendo a documentação da API e julgando as 
informações que eu gostaria de analisar e vou usar nas fases posteriores. Criei um schema porque o postgresql me da essa liberdade e essa organização vai ser importante no futuro do projeto.

Tentei deixar o nome das tabelas o mais autoexplicativas e otimizei para que não houvesse (tanta) redundancia dos dados, então sim, você vai ter que escrever querys complicadas para consultar e fazer seus relatórios
ou pode fazer como eu e usar um software ou escrever suas rotinas/consultas/analises, como PowerBI, Tableau ou até pandas.

Existem 2 tipos de ids nesse schema, o id interno que todas as tabelas possuem, são uma constraint do tipo serial. Alem delas tem também os ids externos que fazem referência
aos dados na API da SportsAt e que é salva no banco. Você pode julgar confuso tem 2 ids pra ligas, partidas, jogadores e afins, mas eles são necessarios em algumas relações em que
o id externo não funcionaria na modelagem que foi planejada, alem disso é importante ter uma primary key em qualquer que seja a tabela, então você pode fazer um exercicio mental para
não ficar tão confuso o uso dos ids, se a atividade se comunicar com a API, vai usar o id externo, se não se comunicar, vai usar o id interno gerado pelo banco. 


## Código

Está é uma aplicação rápida da "arquitetura" do código e como ocorre a comunicação entre a API, o código e o banco.

### .env file
O arquivo .env como pode você reparar está marcado no arquivo .gitignore. Ele espera algumas configs que precisam ser setadas para o código rodar.

```
DB_HOST = host do banco
DB_PORT = porta do banco
DB_NAME = nome do banco 
DB_USER = usuario para acessar
DB_PASSWORD = senha do usuario
API_TOKEN = token da API
LEAGUES_TO_ANALYZE = 13,71,72,73 #ligas para analisar
```
*Obs: esses códigos na variavel LEAGUES_TO_ANALYZE são códigos internos da API que você consegue pelo endpoint https://v3.football.api-sports.io/leagues*
*você listar as ligas por paises e outros metodos de procura. LEAGUES_TO_ANALYZE é importante estar mencionado porque toda o populamento do banco se da por ele*


### database package
O arquivo **connection.py** tem uma classe de conexão com o banco com 3 metodos para centralizar a execução de statements dentro do banco, isso evita a abertura de muitas conexões ou erro de sessão em uma conexão.

O arquivo **data_from_db.py** é o centralizador de queries de consulta e a execução delas, ele tem uma classe com metodos que não recebem parametros,
geralmente retornam uma lista de ids e que possuem um for loop simples para retornar a lista da maneira correta.

O arquivo **queries** é o centralizador dos statements tanto de insert, quanto de update e consulta. Todos os statements de insert e update devem ser definidos como um metodo e no caso de consultas uma variavel de classe. As consultas (variaveis)
quem consome é a classe DataFromDb do arquivo **data_from_db.py** enquanto os inserts e updates quem consome é a classe Manager do arquivo **managers.py** no package **handlers**.

### handlers package
O arquivo **managers.py** tem a classe que faz o gerenciamento das responses, na maioria dos metódos ele chama o parser e passa o response "cru", depois com o retorno do parser ele faz uma querie com a classe Queries e insere no banco com a classe DatabaseConnection.

O arquivo **parsers.py** tem a classe Parsers que para cada (quase toda a tabela (digo quase porque a tabela de estádios e times são inseridas derivadas do mesmo request)) tabela no banco (proveniente do script build.sql) tem um metodo que transforma o response do request
em um dicionário com os valores que a classe Queries (que também possui um metodo de insert para cada tabela do build.sql) espera.

### api_requests package

O arquivo **address_request.py** centraliza o requests e retorna o body. Para cada tipo de informação (geralmente separada por tabela), como jogadores e ligas, tem um método que pede algum tipo parametro como id externo (falo sobre os ids mais abaixo) de algum estádio, jogador etc.

O restante dos arquivos são **arquivos de inicialização dos request**, falei sobre os managers que trabalham passando as responses "crus" para os parsers, pegando responsando e passando para o Queries e depois executando no banco, mas eles não são responsaveis pela inicialização dos estados,
chamar a função main do arquivo inicia as requests e o populamento no banco daquele arquivo. **Ex: chamar o a função main do arquivo teams-stadiums.py vai popular o banco com informações dos times que jogam as ligas que tem no banco (tabela ftb.leagues) e com os estádios desses times.


#### Fluxo de "populamento" do banco.

##### league > teams > stadiums > players > fixtures > fixtures_stats > fixtures_events > fixtures_lineups > teams_squad > players_stats > teams_cards_stats > teams_goals_stats > teams_fixtures_stats

- **leagues.py**: Espera que no arquivo .env tenha ids externos de ligas e popula a tabela **leagues** e inserta as informações de ligas.


- **teams-stadiums.py**: Como expliquei anteriormente esse arquivo popula a tabela estadiums e teams juntos. Ele pega no banco as informações de liga que são provenientes da primeira tabela **leagues** populadas pelo arquivo **leagues.py** e inserta informações dos times e dos estádios. É importante mencionar que os times são inseridos primeiros e logo depois os estadios dos respectivos times porque os estadios fazem referência a um time.


- **players.py**: Pega os ids de times que estão no banco que são provenientes da tabela teams que foi populada pelo arquivo **teams-stadiums.py**.


- **fixtures.py**: Pega os ids de ligas que estão no banco, os mesmos que **teams-stadiums.py** consulta. Ele inserta no banco as informações de cada partida de cada liga na season que foi passada como parametro na chamada do request.


- **fixtures_stats.py**: Pega os ids de partida que foram insertadas no banco pela **fixtures.py** e inserta estatisticas dos dois times que jogaram aquela partida.


- **fixtures_events.py**: A tabela **fixtures_events** é diferente da **fixtures_stats**, ela conta os eventos da partida como cartões, faltas, substituições, gols e afins com algumas informações a mais, ela também faz relação com a tabela **players**. Ela também pega os ids de fixtures no banco populada pela **fixtures.py** assim como fez a **fixtures_stats.py**.


- **fixtures_lineups.py**: A tabela **fixtures_lineups** é mais uma tabela filho da **fixtures** que tem as informações das line ups de cada time que disputou aquela partida. Ela também pega os ids das partidas que estão no banco.


- **teams_squad.py**: Esse arquivo popula a tabela **teams_squad**, a tabela são os atuais jogadores que estão em determinado time, ela pega os ids dos times no banco e popula com os jogadores fazendo referencia a tabela **players** com a tabela **teams**.

 
- **players_stats.py**: Esse arquivo popula o banco com algumas estatisticas e informações de cada jogador em cada liga que ele disputou, ela referencia a tabela **leagues**, **teams** e **players**. Ela pega o id de cada player no banco e popula.
 

- **teams_cards_stats.py**: Esse arquivo serve para popular a tabela **teams_cards_stats**, ela tem algumas estatisticas que poderiam ser calculadas com a tabela **fixtures_events** e um pouco de trabalho, mas afim de evitar perca de informação e trabalho, ela foi incluida no schema. O arquivo pega os ids de todos os times que tem no banco de dados e tras as estatisticas das ligas que os times participaram e que estão no banco. Faz relação com **teams** e **leagues**
 

- **teams_goals_stats.py**: Esse arquivo popula a tabela **teams_goals_stats**, a tabela é bastante semelhante a **teams_cards_stats** mas trás estatisticas de gols dos time pelas ligas que eles participam, ela também poderia ser calculada pela **fixtures_events**, faz relação com **teams** e **leagues**.
 

- **teams_fixtures_stats.py**: Esse arquivo popula a tabela **teams_fixtures_stats**, a tabela também é bastante semelhante a **teams_cards_stats** e a **teams_goals_stats** mas essa trás as informações das partidas dentro de uma liga disputada pelo time, se fosse para calcular ela seria levada mais tabelas em consideração e não apenas a **fixtures_events** diferente das suas outras tabelas "irmãs", ela também faz relação com **teams** e **leagues**.

#### Exemplo de fluxo de comunicação entre as classes.

##### api_request.leagues [response] > handlers.managers.Manager.leagues_management [response] > handlers.parsers.Parsers.leagues_parser [leagues_info] > handlers.managers.Manager.leagues_management [leagues_info] > database.queries.Queries.insert_league [insert_league_query] > handlers.managers.Manager.leagues_management [insert_league_query] > database.connection.DatabaseConnection.\_\_perform__insert_query__ 