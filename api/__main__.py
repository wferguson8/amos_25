
import uvicorn
from api import app  # Assumes your FastAPI instance is in app.py

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000)