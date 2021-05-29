from flask import render_template, request
from flask_login.utils import login_required

from app import app
from app.forms import PatientInfo


@app.route("/patient_info", methods=["GET", "POST"])
@login_required
def patient_info():
    form = PatientInfo()
    if request.method == "POST":
        if form.validate_on_submit():
            print("gg")
        print(form.age.data)
    return render_template("patient_info.html", title="Patient Info - HDP", form=form)
