# Football data

## Oque é

Este é um script de populamento que coleta dados de futebol. Ele usa a [API FOOTBALL](https://www.api-football.com/documentation-v3#section/Introduction) que tem plano free então você (com paciencia) pode popular
seu banco sem precisar gastar, o ideal é que você assine a API de acordo com a sua demanda. O plano free tem o limite de 200 requests diarias que esgota com bastante facilidade. Essa API tem dados de diferentes ligas então pode você analisar os dados
das ligas que bem entender, mas claro, como mencionado anteriormente você pode assinar a API para aumentar o seu limite de requests e conseguir popular e atualizar as suas informações de maneira mais rápida.  
O banco usado foi o **PostgreSQL** mas claro, você pode adaptar o código e o build do banco para a sua preferencia.

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


### database dir
O arquivo **connection.py** tem uma classe de conexão com o banco com 3 metodos para centralizar a execução de statements dentro do banco, isso evita a abertura de muita conexões ou erro de sessão em uma conexão.

O arquivo **data_from_db.py** é o centralizador de queries de consulta e execução, ele tem uma classe com metodos que não recebem parametros,
geralmente retornam uma lista de ids e que possuem um for loop simples para retornar a lista da maneira correta.

O arquivo **queries** é o centralizador dos statements tanto de insert, quanto de update e consulta. Todos os statements devem ser definidos como um metodo ou uma variavel de classe nessa classe onde os managers ou data_from_db vai consumir
para realizar as consultas ou inserts.


## Fluxo de "populamento" do banco.

#### league > teams - stadiums > players > fixtures > fixtures_stats > fixtures_events > fixtures_lineups > teams_squad > players_stats > teams_cards_stats > teams_goals_stats > teams_fixtures_stats