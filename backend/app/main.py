from fastapi import FastAPI
from dotenv import load_dotenv
import os

from starlette.middleware.sessions import SessionMiddleware

load_dotenv()

app = FastAPI()

# Session middleware (REQUIRED for OAuth)
app.add_middleware(
    SessionMiddleware,
    secret_key="dev-secret-key-change-later"
)


app.state.GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
app.state.GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

#exception handle
if not app.state.GOOGLE_CLIENT_ID or not app.state.GOOGLE_CLIENT_SECRET:
    raise RuntimeError("Google OAuth env vars not loaded")

# Now import and init OAuth
from app.auth.google import init_oauth
from app.auth.routes import router as auth_router

init_oauth(app)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "backend running"}
