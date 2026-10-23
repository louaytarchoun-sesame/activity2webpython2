from flask import Flask, render_template
from flask_babel import Babel
from extensions import db 
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)

app.config['SECRET_KEY'] = 'scol_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:louuu@localhost:3306/scol'
app.config['BABEL_DEFAULT_LOCALE'] = 'fr'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

babel = Babel(app)
db.init_app(app)

from models.User import User
from models.Classe import Classe
from models.Etudiant import Etudiant
from models.Matiere import Matiere
from models.Absence import Absence

admin = Admin(app, index_view=AdminIndexView(name='Admin Panel'))


from modelViews.absenceAdmin import AbsenceAdmin
from modelViews.absenceAdmin import AbsenceAdmin
from modelViews.etudiantAdmin import EtudiantAdmin
from modelViews.matiereAdmin import MatiereAdmin
from modelViews.classeAdmin import ClasseAdmin
from modelViews.userAdmin import UserAdmin


admin.add_view(UserAdmin(User, db.session))
admin.add_view(EtudiantAdmin(Etudiant, db.session))
admin.add_view(MatiereAdmin(Matiere, db.session))
admin.add_view(ClasseAdmin(Classe, db.session))
admin.add_view(AbsenceAdmin(Absence, db.session))


app.app_context().push()

with app.app_context():
    db.create_all()
    
    
@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)