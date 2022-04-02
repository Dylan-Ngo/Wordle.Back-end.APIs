import contextlib
import logging.config
import sqlite3


from fastapi import FastAPI, Depends
from pydantic import BaseSettings


class Settings(BaseSettings):
    answer_database: str
    logging_config: str

    class Config:
        env_file = ".env"

def get_db():
    with contextlib.closing(sqlite3.connect(settings.answer_database)) as db:
        db.row_factory = sqlite3.Row
        yield db
    

def get_logger():
    return logging.getLogger(__name__)


settings = Settings()
app = FastAPI()

logging.config.fileConfig(settings.logging_config)

@app.get("/games/{game_id}")
def check_guess(
    game_id: int,
    guess : str,
    db: sqlite3.Connection = Depends(get_db)
):
    answer = ""
    for row in db.execute("SELECT * FROM answers WHERE game_id = ? LIMIT 1", [game_id]):
        answer = row['answer']

    my_list = []
 
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            my_list.append({f"{guess[i]}" : "green"})
        elif guess[i] in answer:
            my_list.append({f"{guess[i]}" : "yellow"})
        else:
            my_list.append({f"{guess[i]}" : "gray"})
    return {"response": my_list}
