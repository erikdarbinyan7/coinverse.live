from fastapi import Request
from fastapi_utils.cbv import cbv
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, Response, JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
# from fastapi import status
# from apps.auth.models import User
# from config.db import Session, get_db, Base, engine
from config.settings import (
    router,
    app,
    templates_path, MAIL, APP_PASSWORD,
)

# Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory=templates_path)

limiter = Limiter(key_func=get_remote_address, retry_after="20seconds")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@cbv(router)
class Authorization:
    @router.get(path="/", tags=["Home"], response_class=HTMLResponse)
    @limiter.limit("15/15seconds")
    def home(self, request: Request):
        return templates.TemplateResponse("index.html", {"request": request})

    @router.post(path="/", tags=["Home"])
    @limiter.limit("15/15seconds")
    async def home_post(self, request: Request):
        pass