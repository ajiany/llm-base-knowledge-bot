import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

class Config(BaseModel):
    app_name: str
    project_env: str
    api_version: str

def get_config() -> Config:
    return Config(
        app_name=os.getenv("APP_NAME", "LLM-BASE_KNOWLEDGE-BOT"),
        project_env=os.getenv("PROJECT_ENV", "dev"),
        api_version=os.getenv("API_VERSION", "0.0.1")
    )

class Healthz(BaseModel):
    name: str
    env: str
    version: str

@app.get("/healthz")
def handle_healthz() -> Healthz:
    config = get_config()
    return Healthz(
        name=config.app_name,
        env=config.project_env,
        version=config.api_version
    )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)