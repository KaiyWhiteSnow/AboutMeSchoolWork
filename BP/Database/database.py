from contextlib import contextmanager

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.orm.state import InstanceState

engine = create_engine("sqlite:///database.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

from Database.Models.user import Base as UserBase
UserBase.metadata.create_all(engine)


# Function to get a session with rollback capability
@contextmanager
def get_session() -> Session: # type: ignore
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()