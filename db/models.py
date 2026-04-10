from sqlmodel import SQLModel, Field


class PelaajaBase(SQLModel):
    name: str
    events: str


class PelaajaIn(PelaajaBase):
    pass


class PelaajaDb(PelaajaBase, table=True):
    id: int = Field(default=None, primary_key=True)


class EventBase(SQLModel):
    type: str
    detail: str
    player_id: int
    timestamp: str


class EventDb(EventBase, table=True):
    player_id: int = Field(default=None, primary_key=True)


class EventIn(EventBase):
    pass
