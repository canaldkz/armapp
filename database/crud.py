# from sqlalchemy.exc import IntegrityError
from database import with_session
from database.models import *


@with_session
def add_card(first_name, last_name, date, service_id, prof_id, session):
    card = Card(
        first_name=first_name,
        last_name=last_name,
        service_id=service_id,
        prof_id=prof_id,
        date=date,
    )
    session.add(card)
    return (True, "Ok!")


@with_session
def get_all_cards(session):
    result = session.query(Card).all()
    return (True, result) if result else (False, "Нет карточек")


@with_session
def add_item(item_name, item_count, session):
    item = Item(item_name=item_name, item_count=item_count)
    session.add(item)
    return (True, "Ok!")


@with_session
def get_items(item_ids, session):
    item = session.query(Item).filter(Item.item_id.in_(item_ids)).all()
    return (True, item) if item else (False, "Предметы не найдены")


@with_session
def get_all_items(session):
    items = session.query(Item).all()
    return (True, items) if items else (False, "Нет предметов")


@with_session
def add_profession(name, items, session):
    prof = Profession(prof_name=name, items=list(items))
    session.add(prof)
    return (True, "Ok!")


@with_session
def get_all_profs(session):
    profs = session.query(Profession).all()
    return (True, profs) if profs else (False, "Нет должностей")
