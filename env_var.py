from dotenv import load_dotenv

load_dotenv()


def getVar(var_name: str):
    import os
    return os.getenv(var_name)


def getHeaders():
    return {
        "x-rapidapi-key": getVar("API_TOKEN")
    }
