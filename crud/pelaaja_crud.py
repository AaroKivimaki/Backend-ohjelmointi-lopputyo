from fastapi import HTTPException, status
from ..db.models import PelaajaDb, PelaajaIn, EventDb, EventIn
from sqlmodel import Session, select


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


def get_pelaaja_by_id(session: Session, id: int):
    pelaaja = session.get(PelaajaDb, id)
    if not pelaaja:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pelaaja not found"
        )
    return pelaaja


def get_events_by_player_id(session: Session, id: int, level_type: str | None = None):
    pelaaja = session.get(PelaajaDb, id)
    if not pelaaja:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pelaaja not found"
        )
    if id:
        if level_type:
            if level_type == "level_started" or level_type == "level_solved":
                statement = select(EventDb).where(
                    EventDb.player_id == id, EventDb.type == level_type
                )
                return session.exec(statement).all()
            else:
                raise HTTPException(status_code=400)
        else:
            statement = select(EventDb).where(EventDb.player_id == id)
            return session.exec(statement).all()
    return session.exec(select(EventDb)).all()


def create_event_for_pelaaja(session: Session, event_in: EventIn, player_id: int):
    pelaaja = session.get(PelaajaDb, player_id)
    if not pelaaja:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pelaaja not found"
        )

    event = EventDb.model_validate(event_in)
    event.player_id = player_id

    session.add(event)
    session.commit()
    session.refresh(event)
    return event
