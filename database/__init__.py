from sqlalchemy import create_engine
from logging import getLogger

SQLITE_URL = 'sqlite+pysqlite:///C:\\DBs\\ArmDb.db'
engine = create_engine(SQLITE_URL ,echo=False, encoding='utf-8')

logger = getLogger('DB')

def with_session(f):
    def wrapped(*args, **kwargs):
        session = args[-1]
        try:
            result = f(*args, **kwargs)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            logger.error(e)
            return (False, str(e))
        finally:
            session.remove()
    return wrapped
