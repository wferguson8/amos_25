from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from supabase import create_client, Client

app = FastAPI()

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

@app.get("/")
def redir():
    # Redirect root path to /docs (or any other path)
    return RedirectResponse(url="/docs")


@app.get("/health")
def health():
    # Basic healthcheck endpoint
    return JSONResponse(content={"status": "ok"})

@app.get("/state_summary")
def state_summary(state: str) -> JSONResponse:
    try:
        response = (
            supabase.table("summary")
            .select("*")
            .execute()
        )

        print(response)

        df = pd.DataFrame(response.data)

        output = df[df['state'] == state].to_dict()

        return JSONResponse(output)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("winner_summary")
def winner_summary():
    try:
        response = (
            supabase.table("planets")
            .select("*")
            .execute()
        )
        return JSONResponse(response.data[0])  # Should just be one row
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
