from sqlite3 import Date
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    SubmitField,
    IntegerRangeField,
    DateField,
    SelectMultipleField,
    SelectField,
)
from wtforms.validators import Length, EqualTo, InputRequired, NumberRange


class CardForm(FlaskForm):

    service_number = IntegerField("Табельный номер", validators=[InputRequired()])

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
        "Дата",
        format="%d.%m.%Y",
        validators=[InputRequired()],
        render_kw={"class": "autocomplete datepicker"},
    )
    profession = SelectField("Должность", validators=[InputRequired()])

    submit = SubmitField("Сохранить", render_kw={"class": "btn waves-btn waves-light"})


class ProfessionForm(FlaskForm):
    name = StringField(
        "Наименование",
        validators=[InputRequired(), Length(max=16)],
        render_kw={"class": "autocomplete"},
    )

    items = SelectMultipleField(
        "Предметы", validators=[InputRequired(), Length(min=1)], coerce=int
    )

    submit = SubmitField("Сохранить", render_kw={"class": "btn waves-btn waves-light"})


class ItemForm(FlaskForm):
    name = StringField(
        "Наименование",
        validators=[InputRequired(), Length(max=16)],
        render_kw={"class": "autocomplete"},
    )
    count = IntegerField(
        "Количество", validators=[NumberRange(min=1, max=99), InputRequired()]
    )
    submit = SubmitField("Сохранить", render_kw={"class": "btn waves-btn waves-light"})
