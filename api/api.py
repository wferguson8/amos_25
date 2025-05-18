from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from supabase import create_client, Client

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://localhost:63342"] to be stricter
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
def state_summary() -> JSONResponse:
    try:
        response = supabase.table("summary").select("*").execute()

        # Check for errors in response
        if not response.data:
            raise Exception("No data returned from Supabase.")

        df = pd.DataFrame(response.data)

        # Ensure state codes are uppercase
        df["state"] = df["state"].str.upper()

        # Set 'state' as index and convert to dict of dicts
        summaries = df.set_index("state")[["sims_p", "sims_v", "sims_c", "sims_w"]].to_dict(orient="index")

        return JSONResponse(summaries)
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
