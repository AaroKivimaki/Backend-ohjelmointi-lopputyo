from fastapi import HTTPException, status
from ..db.models import PelaajaDb, PelaajaIn, EventDb, EventIn
from sqlmodel import Session, select

pelaajat = [{"id": 0, "name": "pelaaja1"}, {"id": 1, "name": "pelaaja2"}]


def create_pelaaja(session: Session, pelaaja_in: PelaajaIn):
    pelaaja = PelaajaDb.model_validate(pelaaja_in)
    session.add(pelaaja)
    session.commit()
    session.refresh(pelaaja)
    return pelaaja


def get_pelaajat(session: Session, name: str | None = None):
    if name:
        statement = select(PelaajaDb).where(PelaajaDb.name == name)
        return session.exec(statement).all()
    return session.exec(select(PelaajaDb)).all()


def get_pelaaja_by_id(session: Session, pelaaja_id: int):
    pelaaja = session.get(PelaajaDb, pelaaja_id)
    if not pelaaja:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pelaaja not found"
        )
    return pelaaja


def create_event_for_pelaaja(session: Session, event_in: EventIn):
    event = EventDb.model_validate(EventIn)
    session.add(event)
    session.commit()
    session.refresh(event)
    return event
