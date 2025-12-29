from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from .google import oauth

router = APIRouter(prefix="/auth")

@router.get("/login")
async def login(request: Request):
    redirect_uri = "http://127.0.0.1:8000/auth/callback"
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/callback")
async def callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user = token.get("userinfo")
    return user
