from flask import render_template

def login_view():
    return render_template('auth/login.html')

def register_view():
    return render_template('auth/register.html')