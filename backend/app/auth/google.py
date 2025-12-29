from authlib.integrations.starlette_client import OAuth

oauth = OAuth()

def init_oauth(app):
    oauth.register(
        name="google",
        client_id=app.state.GOOGLE_CLIENT_ID,
        client_secret=app.state.GOOGLE_CLIENT_SECRET,
        server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
        client_kwargs={
            "scope": "openid email profile"
        }
    )
