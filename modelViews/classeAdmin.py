from flask_admin.contrib.sqla import ModelView


class ClasseAdmin(ModelView):
    form_excluded_columns = ["etudiants", "nbrEtudiant"]
    form_columns = ["codClass", "nomClass"]

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.nbrEtudiant = 0