from flask_wtf import FlaskForm
from wtforms.fields import (
    BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
)
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime


class AppointmentForm(FlaskForm):
    # title = StringField("Title", validators=[DataRequired()])
    # author = StringField("Author", validators=[DataRequired()])
    # rating = SelectField("Rating",
    #             choices=["New favorite", "Ok", "Bad", "Horrible"])
    # submit = SubmitField("Add Book")
    name = StringField("name", validators=[DataRequired()])
    start_date = DateField("start_date", validators=[DataRequired()])
    start_time= TimeField("start_time", validators=[DataRequired()])
    end_date = DateField("end_date", validators=[DataRequired()])
    end_time= TimeField("end_time", validators=[DataRequired()])
    description = TextAreaField("description", validators=[DataRequired()])
    private = BooleanField("private")
    submit = SubmitField("Add Appointment")

    def validate_end_date(form, field):
        start = datetime.combine(form.start_date.data, form.start_time.data)
        end = datetime.combine(field.data, form.end_time.data)
        if start >= end:
            msg = "End date/time must come after start date/time"
        if start == end:
            msg = "Start time and end time can't be the same"
        raise ValidationError(msg)
