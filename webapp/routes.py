from flask import redirect, request, jsonify, render_template, url_for, flash
from webapp import app, moment, web_session
from database import crud
from webapp.forms import *

from datetime import datetime


def notify(result):
    if result[0]:
        flash('Ok!')
    else:
        flash(result[1])


@app.route("/")
def index():
    ip = request.remote_addr
    now = moment.create(datetime.now())
    return render_template('web/index.html', time=now)


@app.route("/add_employee", methods=["GET", "POST"])
def add_employee():
    form = EmployeeForm()
    if form.validate_on_submit():
        res = crud.add_employee(form.first_name.data, form.last_name.data, form.date.data, web_session)
        notify(res)
        return redirect(url_for('index'))
    return render_template('web/add_employee.html', form=form)


@app.route("/close")
def close_window():
    return render_template("web/close.html")
