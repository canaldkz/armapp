from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    Date,
    Table,
)
from database import engine

base = declarative_base()

rel_table = Table(
    "prof-item",
    base.metadata,
    Column("prof_id", ForeignKey("professions.prof_id")),
    Column("item_id", ForeignKey("items.item_id")),
)


class Card(base):
    __tablename__ = "cards"

    card_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(16), nullable=False)
    last_name = Column(String(16), nullable=False)
    service_id = Column(Integer)
    # division = Column(String(16))
    prof_id = Column(Integer, ForeignKey("professions.prof_id"))
    date = Column(Date, nullable=False)


class Profession(base):
    __tablename__ = "professions"

    prof_id = Column(Integer, primary_key=True, autoincrement=True)
    prof_name = Column(String)

    items = relationship("Item", secondary=rel_table)


class Item(base):
    __tablename__ = "items"

    item_id = Column(Integer, primary_key=True, autoincrement=True)
    item_name = Column(String(16))
    item_count = Column(Integer)


base.metadata.create_all(engine)
