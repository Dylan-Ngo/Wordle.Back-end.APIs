import contextlib
import logging.config
import sqlite3


from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseSettings


class Settings(BaseSettings):
    word_database: str
    logging_config: str

    class Config:
        env_file = ".env"

def get_db():
    with contextlib.closing(sqlite3.connect(settings.word_database)) as db:
        db.row_factory = sqlite3.Row
        yield db
    

def get_logger():
    return logging.getLogger(__name__)


settings = Settings()
app = FastAPI()

logging.config.fileConfig(settings.logging_config)

@app.get("/validate")
def validate_guess(
    guess : str,
    db: sqlite3.Connection = Depends(get_db)
):
    cur = db.execute("SELECT * FROM words WHERE word = ?", [guess])
    words = cur.fetchall()

    if len(guess) != 5:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"{guess} not five letters. Removed {guess}"
        )
    elif not guess.isascii() or not guess.isalpha():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"{guess} not entirely letters. Removed {guess}"
        )
    elif not words:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"{guess} not found in dictionary. Removed {guess}"
        )
    
    valid_guess = ""
    for word in words:
        valid_guess = word['word']
    return {"response": f"Valid guess. Added {valid_guess} to check against answer"}
