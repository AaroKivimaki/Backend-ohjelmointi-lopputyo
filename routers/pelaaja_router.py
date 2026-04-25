from fastapi import APIRouter, status, Depends
from ..db.models import PelaajaDb, PelaajaIn, EventIn, EventDb
from ..crud import pelaaja_crud as crud
from ..db.database import get_session
from sqlmodel import Session

router = APIRouter(prefix="/pelaajat", tags=["pelaajat"])


@router.post("", response_model=PelaajaDb, status_code=status.HTTP_201_CREATED)
def create_pelaaja(pelaaja_in: PelaajaIn, session: Session = Depends(get_session)):
    return crud.create_pelaaja(session, pelaaja_in)


@router.get("", response_model=list[PelaajaDb])
def get_pelaajat(name: str | None = None, session: Session = Depends(get_session)):
    return crud.get_pelaajat(session, name)


@router.get(
    "/{pelaaja_id}",
    response_model=PelaajaDb,
    responses={404: {"description": "Pelaaja not found"}},
)
def get_pelaaja_by_id(pelaaja_id: int, session: Session = Depends(get_session)):
    return crud.get_pelaaja_by_id(session, pelaaja_id)


@router.post("", response_model=PelaajaDb, status_code=status.HTTP_201_CREATED)
def create_event_for_pelaaja(
    event_in: EventIn, session: Session = Depends(get_session)
):
    return crud.create_pelaaja(session, event_in)
