import os, sys

from flask import Flask
from flask_moment import Moment

from sqlalchemy.orm import scoped_session, sessionmaker
from database import engine

base_dir = "."
if hasattr(sys, "_MEIPASS"):
    base_dir = os.path.join(sys._MEIPASS)

app = Flask(
    __name__,
    static_folder=os.path.join(base_dir, "static"),
    template_folder=os.path.join(base_dir, "templates"),
)

moment = Moment(app)

app.config["SESSION_COOKIE_SECURE"] = False
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.secret_key = "CZ3EL5IH12ASMQ6RRXV3458JBC2GPDK0JL3RCKPGU648NBO5"

session_factory = sessionmaker(engine, autocommit=False, autoflush=False)
web_session = scoped_session(session_factory=session_factory)

from webapp import routes
