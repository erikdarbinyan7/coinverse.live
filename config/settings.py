import os
from fastapi_utils.inferring_router import InferringRouter
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

ALLOWED_HOSTS = ["127.0.0.1", "0.0.0.0", "localhost", "*.example.com"]

DEBUG = True
IS_PUBLIC = False

MAIL = "oodarbinyan@gmail.com"
APP_PASSWORD = "nosmrepgjfmgazgn"

app = FastAPI(debug=DEBUG, title='coinverse.ai')
router = InferringRouter()

path = os.path.abspath("Front/static")
templates_path = os.path.abspath("Front/templates")

app.mount("/static", StaticFiles(directory=path), name="static")
app.add_middleware(GZipMiddleware, minimum_size=1400)

state_param = "hjkasdbjilsdncuinllamsn"
client_id = "1sad1axsSxswCWWeccsc"

origins = ["https://coinverse.ai","https://www.coinverse.ai"]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

templates = Jinja2Templates(directory=templates_path)

app.add_middleware(SessionMiddleware, secret_key="my-secret-key")
import apps.auth.controllers
app.include_router(router)
