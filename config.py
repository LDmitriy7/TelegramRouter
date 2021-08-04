import os

from dotenv import load_dotenv

load_dotenv()

APP_HOST = os.environ['APP_HOST']
APP_PORT = os.environ['APP_PORT']
TELEGRAM_ROUTE = os.environ['TELEGRAM_ROUTE']
QUERY_PROXY_KEY = os.environ['QUERY_PROXY_KEY']

SSL_CERT_FILE = os.getenv('SSL_CERT_FILE')
SSL_KEY_FILE = os.getenv('SSL_KEY_FILE')
