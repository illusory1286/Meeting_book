# ======ORM======
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import MeetingRoom, User, Reservation, Base

# 初始化資料庫連線
DATABASE_URL = "sqlite:///./meeting_room_reservation.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()

# 資料庫依賴


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 會議室API


@app.post("/rooms/", response_model=MeetingRoom)
def create_room(room: MeetingRoom, db: Session = Depends(get_db)):
    db_room = MeetingRoom(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room


@app.get("/rooms/{room_id}", response_model=MeetingRoom)
def get_room(room_id: int, db: Session = Depends(get_db)):
    room = db.query(MeetingRoom).filter(MeetingRoom.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

# 預約API


@app.post("/reservations/", response_model=Reservation)
def create_reservation(reservation: Reservation, db: Session = Depends(get_db)):
    db_reservation = Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation


@app.get("/reservations/{reservation_id}", response_model=Reservation)
def get_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation = db.query(Reservation).filter(
        Reservation.id == reservation_id).first()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation
