from flask import redirect, request, jsonify, render_template, url_for, flash
from webapp import app, moment, web_session
from database import crud
from webapp.forms import *

from datetime import datetime


@app.route("/")
def index():
    ip = request.remote_addr
    now = moment.create(datetime.now())
    return render_template("web/index.html", time=now, title="Главная")


@app.route("/add_card", methods=["GET", "POST"])
def add_card():
    form = CardForm()
    res = crud.get_all_profs(session=web_session())
    if res[0]:
        all_profs = res[1]
        form.profession.choices = [(p.prof_id, p.prof_name) for p in all_profs]

    if form.validate_on_submit():
        res = crud.add_card(
            form.first_name.data,
            form.last_name.data,
            form.date.data,
            form.service_number.data,
            form.profession.data,
            web_session(),
        )
        return redirect(url_for("index"))
    return render_template("web/add.html", form=form, title="Добавить карточку")


@app.route("/add_profession", methods=["GET", "POST"])
def add_profession():
    form = ProfessionForm()
    res = crud.get_all_items(session=web_session())
    if res[0]:
        all_items = res[1]
        form.items.choices = [
            (i.item_id, f"{i.item_name} ({i.item_count})") for i in all_items
        ]

    if form.validate_on_submit():
        res = crud.get_items(item_ids=form.items.data, session=web_session())
        if res[0]:
            res = crud.add_profession(
                name=form.name.data, items=res[1], session=web_session()
            )
        return redirect(url_for("index"))
    return render_template("web/add.html", form=form, title="Добавить должность")


@app.route("/add_item", methods=["GET", "POST"])
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        res = crud.add_item(
            item_name=form.name.data, item_count=form.count.data, session=web_session()
        )
        return redirect(url_for("index"))
    return render_template("web/add.html", form=form, title="Добавить предмет")


@app.route("/close")
def close_window():
    return render_template("web/close.html")
