from fastapi import APIRouter, status
from ..db.models import EventDb, EventIn
from ..crud import event_crud as crud

router = APIRouter(prefix="/events", tags=["events"])


@router.get("", response_model=list[EventDb])
def get_events():
    return crud.get_events()
