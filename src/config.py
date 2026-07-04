from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parents[1]

load_dotenv(BASE_DIR/".env")

USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")

URL_LOGIN = (BASE_DIR / "web" / "login.html").as_uri()
PLANILHA = BASE_DIR / "data" / "input" / "NotasEmitir.xlsx"
PASTA_DOWNLOAD = BASE_DIR / "data" / "output"