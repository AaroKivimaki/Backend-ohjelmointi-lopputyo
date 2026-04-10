from fastapi import APIRouter, status, Depends
from ..db.models import PelaajaDb, PelaajaIn
from ..crud import pelaaja_crud as crud
from ..db.database import get_session
from sqlmodel import Session

router = APIRouter(prefix="/pelaajat", tags=["pelaajat"])


@router.post("", response_model=PelaajaDb, status_code=status.HTTP_201_CREATED)
def create_pelaaja(pelaaja_in: PelaajaIn, session: Session = Depends(get_session)):
    return crud.create_pelaaja(session, pelaaja_in)


@router.get("", response_model=list[PelaajaDb])
def get_pelaajat(event: str | None = None, Session=Depends(get_session)):
    return crud.get_pelaajat(event)
