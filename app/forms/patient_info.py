from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.core import IntegerField, SelectField
from wtforms.validators import DataRequired


class PatientInfo(FlaskForm):
    age = IntegerField(label="Age", validators=[DataRequired()])
    chest_pain = SelectField(
        label="Cheast Pain",
        validators=[DataRequired()],
        choices=[
            ("anginal pain", "anginal_pain"),
            ("non anginal pain", "non-anginal_pain"),
        ],
    )
    sereum_cholestoral = IntegerField(
        label="Sereum Cholestoral", validators=[DataRequired()]
    )
    resting_ecg = IntegerField(label="Resting ECG", validators=[DataRequired()])
    exercise_induced_angina = IntegerField(
        label="Exercise Induced Angina", validators=[DataRequired()]
    )
    slope = IntegerField(label="Slope", validators=[DataRequired()])
    thal = IntegerField(label="Thal", validators=[DataRequired()])
    gender = IntegerField(label="Gender", validators=[DataRequired()])
    resting_bp = IntegerField(label="Resting BP", validators=[DataRequired()])
    fasting_blood_sugar = IntegerField(
        label="Fasting Blood Sugur", validators=[DataRequired()]
    )
    max_heart_rate = IntegerField(
        label="Maximum Heart Rate", validators=[DataRequired()]
    )
    oldpeak = IntegerField(label="Oldpeak", validators=[DataRequired()])
    ca = IntegerField(label="CA", validators=[DataRequired()])
    searchby = SelectField(
        label="Search By",
        validators=[DataRequired()],
        choices=[
            ("Naive Bayes", "naive_bayes"),
            ("Decision Tree", "decision_tree"),
            ("KNN", "knn"),
        ],
    )
    check = SubmitField(label="Check")
