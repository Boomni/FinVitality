#!/usr/bin/python3
""" View for the loans page"""
from app.api.v1 import app_views
from flask import session, redirect, request, render_template
from app.api.v1.models.loans import Loan
from app.api.v1.models.users import User
from app.api.v1.models.loan_applications import LoanApplication
from app.api.v1.models import storage


@app_views.route('/user/loans', methods=['GET'], strict_slashes=False)
def loans_packages():
    """ displays a HTML page with a list of loans """
    if not session.get('logged_in'):
        return redirect('/login')
    user_email = session['email']
    session_data = storage.get_session()

    if session_data:
        user = session_data.query(User).filter(User.email
                                               == user_email).first()

        if user:
            profile_data = {
                'firstname': user.firstname,
                'lastname': user.lastname,
            }
    loans = storage.all(Loan).values()
    loans = sorted(loans, key=lambda k: k.title)
    return render_template('loans.html', loans=loans, profile_data=profile_data)


@app_views.route('/user/loans/apply', methods=['POST'], strict_slashes=False)
def submit_loan_application():
    if not session.get('logged_in'):
        return redirect('/login')
    user_email = session['email']
    session_data = storage.get_session()
    if session_data:
        user = session_data.query(User).filter(User.email
                                               == user_email).first()


    firstname = request.form.get("first_name")
    lastname = request.form.get('last_name')
    gender = request.form.get('gender')
    marital_status = request.form.get('marital_status')
    date_of_birth = request.form.get('date_of_birth')
    email = request.form.get('email')
    mobile_number = request.form.get("mobile_number")
    num_dependents = request.form.get("num_dependents")
    annual_income = request.form.get("annual_income")
    bank_name = request.form.get("bank_name")
    bvn = request.form.get("bvn")
    account_number = request.form.get("account_number")
    occupation = request.form.get("occupation")
    office_address = request.form.get("office_address")
    loan_credit_facility = request.form.get("loan_credit_facility")
    loan_amount = request.form.get("loan_amount")
    payment_tenure = request.form.get("payment_tenure")
    loan_purpose = request.form.get("loan_purpose")
    agreement = request.form.get("agreement")

    loan_application = LoanApplication(
        firstname=firstname,
        lastname=lastname,
        gender=gender,
        marital_status=marital_status,
        date_of_birth=date_of_birth,
        email=email,
        mobile_number=mobile_number,
        num_dependents=num_dependents,
        annual_income=annual_income,
        bank_name=bank_name,
        bvn=bvn,
        account_number=account_number,
        occupation=occupation,
        office_address=office_address,
        loan_credit_facility=loan_credit_facility,
        loan_amount=loan_amount,
        payment_tenure=payment_tenure,
        loan_purpose=loan_purpose,
    )
    if user:
        loan_application.user_id = user.id
    else:
        print(f"User with email '{user_email}' not found in the database.")
        # Redirect or handle the error appropriately
        return redirect("/user/dashboard")

    # Save the loan application in the database
    storage.new(loan_application)
    storage.save()

    # Redirect to a success page or dashboard
    return redirect("/user/dashboard")