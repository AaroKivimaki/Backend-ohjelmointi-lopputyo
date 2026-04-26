from fastapi import APIRouter, status, Depends
from ..db.models import PelaajaDb, PelaajaIn, EventIn, EventDb, PelaajaWithEvents
from ..crud import pelaaja_crud as crud
from ..db.database import get_session
from sqlmodel import Session

router = APIRouter(prefix="/players", tags=["players"])


@router.post("", response_model=PelaajaDb, status_code=status.HTTP_201_CREATED)
def create_pelaaja(pelaaja_in: PelaajaIn, session: Session = Depends(get_session)):
    return crud.create_pelaaja(session, pelaaja_in)


@router.get("", response_model=list[PelaajaDb])
def get_pelaajat(name: str | None = None, session: Session = Depends(get_session)):
    return crud.get_pelaajat(session, name)


@router.get(
    "/{id}",
    response_model=PelaajaWithEvents,
    responses={404: {"description": "Player not found"}},
)
def get_pelaaja_by_id(id: int, session: Session = Depends(get_session)):
    return crud.get_pelaaja_by_id(session, id)


@router.get("/{id}/events", response_model=list[EventDb])
def get_events_by_player_id(
    id: int, level_type: str | None = None, session: Session = Depends(get_session)
):
    return crud.get_events_by_player_id(session, id, level_type)


@router.post(
    "/{id}/events",
    response_model=EventDb,
    status_code=status.HTTP_201_CREATED,
)
def create_event_for_pelaaja(
    player_id: int, event_in: EventIn, session: Session = Depends(get_session)
):
    return crud.create_event_for_pelaaja(session, event_in, player_id)
