from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
import os
import pandas as pd
from sqlalchemy import create_engine

app = FastAPI()

DB_CONNECTION = os.getenv("DB_CONNECTION")
engine = create_engine(DB_CONNECTION)


@app.get("/")
def redir():
    # Redirect root path to /docs (or any other path)
    return RedirectResponse(url="/docs")


@app.get("/healthcheck")
def healthcheck():
    # Basic healthcheck endpoint
    return JSONResponse(content={"status": "ok"})

@app.get("/state_summary")
def state_summary(state: str) -> JSONResponse:
    try:
        df = pd.read_sql("SELECT * FROM summary", con=engine)
        row = df.loc[state, :].to_dict()
        return JSONResponse(row)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("winner_summary")
def winner_summary():
    try:
        df = pd.read_sql("SELECT * FROM winner", con=engine).to_dict()
        return JSONResponse(df)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
