from flask import current_app as app
from flask import  render_template_string
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin

@app.route('/')
def home_page():
    return render_template_string("""
            {% extends "flask_user_layout.html" %}
            {% block content %}
                <h2>{%trans%}Home page{%endtrans%}</h2>
                <p><a href={{ url_for('user.register') }}>{%trans%}Register{%endtrans%}</a></p>
                <p><a href={{ url_for('user.login') }}>{%trans%}Sign in{%endtrans%}</a></p>
                <p><a href={{ url_for('user.edit_user_profile') }}>{%trans%}Edit my profile{%endtrans%}</a> </p>
                <p><a href={{ url_for('user.change_password') }}>{%trans%}Change Password{%endtrans%}</a> (login_required)</p>
                <p><a href={{ url_for('user.forgot_password') }}>{%trans%}Forgot Password{%endtrans%}</a></p>
                <p><a href={{ url_for('user.logout') }}>{%trans%}Sign out{%endtrans%}</a></p>
            {% endblock %}
            """)
