from flask_admin.contrib.sqla import ModelView
from wtforms import FloatField


class AbsenceAdmin(ModelView):
    column_list = ["etudiant", "matiere", "dateA", "nha"]
    
    page_size = 10
    can_set_page_size = True

    column_labels = {
        "etudiant": "Étudiant",
        "matiere": "Matière",
        "dateA": "Date",
        "nha": "Nombre d'heures",
    }
    column_filters = ["dateA", "etudiant", "matiere"]
    
    form_columns = ["etudiant", "matiere", "dateA", "nha"]


    form_extra_fields = {
        "nha": FloatField("Nombre d'heures"),
    }

