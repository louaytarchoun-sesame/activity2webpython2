from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash

from forms.userForm import UserForm
from models.User import User


class UserAdmin(ModelView):
    form = UserForm

    page_size = 5
    can_set_page_size = True

    # Ne pas afficher le mot de passe dans la liste
    column_exclude_list = ["password"]

    def validate_form(self, form):
        if not super().validate_form(form):
            return False

        username = form.username.data.strip() if form.username.data else ""
        email = form.email.data.strip().lower() if form.email.data else ""

        form.username.data = username
        form.email.data = email

        current_user = getattr(form, "obj", None)

        existing_username = User.query.filter_by(username=username).first()
        if existing_username and (current_user is None or existing_username.username != current_user.username):
            form.username.errors.append("This username is already used.")
            return False

        existing_email = User.query.filter_by(email=email).first()
        if existing_email and (current_user is None or existing_email.email != current_user.email):
            form.email.errors.append("This email is already used.")
            return False

        return True

    # Hash du mot de passe avant enregistrement
    def on_model_change(self, form, model, is_created):
        if form.password.data:
            model.password = generate_password_hash(
                form.password.data
            )