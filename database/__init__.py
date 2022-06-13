from sqlalchemy import create_engine
from logging import getLogger

SQLITE_URL = "sqlite+pysqlite:///C:\\DBs\\ArmDb.db"
engine = create_engine(SQLITE_URL, echo=False, encoding="utf-8")

logger = getLogger("DB")


def with_session(f):
    def wrapped(*args, **kwargs):
        try:
            session = kwargs.get("session", None)
            if not session:
                session = args[-1]
        except IndexError:
            return (False, "Session argument required!")
        try:
            result = f(*args, **kwargs)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            logger.error(e)
            return (False, str(e))

    return wrapped
