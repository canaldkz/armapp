from sqlite3 import Date
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, IntegerRangeField, DateField
from wtforms.validators import Length, EqualTo, InputRequired


class EmployeeForm(FlaskForm):
    first_name = StringField(
        "Имя",
        name="Имя",
        validators=[InputRequired(), Length(max=16)],
        render_kw={"class": "autocomplete"},
    )
    last_name = StringField(
        "Фамилия",
        name="Фамилия",
        validators=[InputRequired(), Length(max=16)],
        render_kw={"class": "autocomplete"},
    )
    date = DateField(
        "Дата", format="%d.%m.%Y", validators=[InputRequired()], render_kw={"class": "autocomplete datepicker"}
    )
    submit = SubmitField("Сохранить", render_kw={
        "class": "btn waves-btn waves-light"
    })
