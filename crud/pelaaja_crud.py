from fastapi import HTTPException, status
from ..db.models import PelaajaDb, PelaajaIn
from sqlmodel import Session, select

pelaajat = [{"id": 0, "name": "pelaaja1"}, {"id": 1, "name": "pelaaja2"}]


def create_pelaaja(session: Session, pelaaja_in: PelaajaIn):
    pelaaja = PelaajaDb.model_validate(pelaaja_in)
    session.add(pelaaja)
    session.commit()
    session.refresh(pelaaja)
    return pelaaja


def get_pelaajat(session: Session, event: str | None = None):
    if event:
        statement = select(PelaajaDb).where(PelaajaDb.event == event)
        return session.exec(statement).all()
    return session.exec(select(PelaajaDb)).all()
