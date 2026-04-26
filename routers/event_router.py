from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..db.database import get_session
from ..db.models import EventDb
from ..crud import event_crud as crud

router = APIRouter(prefix="/events", tags=["events"])


@router.get("", response_model=list[EventDb])
def get_events(level_type: str | None = None, session: Session = Depends(get_session)):
    return crud.get_events(session, level_type)
