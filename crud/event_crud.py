from ..db.models import EventDb, EventIn

events = [
    {
        "id": 0,
        "type": "level_started",
        "detail": "level_1212_001",
        "timestamp": "2023-01-13 12:01:22",
        "player_id": 1,
    }
]

# def create_event(manu_in: ManufacturerIn):
#     new_id = max([s["id"] for s in manus]) + 1
#     manu = ManufacturerDb(id=new_id, **manu_in.model_dump())
#     manus.append(manu.model_dump())
#     return manu


def get_events():
    return events
