from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship


class PelaajaBase(SQLModel):
    name: str


class PelaajaIn(PelaajaBase):
    pass


class PelaajaDb(PelaajaBase, table=True):
    id: int = Field(default=None, primary_key=True)
    events: "EventDb" = Relationship(back_populates="pelaaja")


class EventBase(SQLModel):
    type: str
    detail: str


class EventIn(EventBase):
    pass


class EventDb(EventBase, table=True):
    id: int = Field(default=None, primary_key=True)
    timestamp: datetime = Field(default_factory=datetime.now)
    player_id: int = Field(default=None, foreign_key="pelaajadb.id")
    pelaaja: "PelaajaDb" = Relationship(back_populates="events")


class PelaajaWithEvents(PelaajaBase):
    id: int
    events: EventDb = []
