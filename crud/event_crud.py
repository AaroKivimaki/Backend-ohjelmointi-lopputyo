from sqlmodel import Session, select
from fastapi import HTTPException
from ..db.models import EventDb


def get_events(session: Session, level_type: str):
    if level_type:
        if level_type == "level_started" or level_type == "level_solved":
            statement = select(EventDb).where(EventDb.type == level_type)
            return session.exec(statement).all()
        else:
            raise HTTPException(status_code=400)
    return session.exec(select(EventDb)).all()
