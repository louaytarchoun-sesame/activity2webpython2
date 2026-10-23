from flask_admin.contrib.sqla import ModelView
from sqlalchemy import inspect


class EtudiantAdmin(ModelView):
    form_excluded_columns = ["absences"]
    form_columns = ["nce", "nom", "prenom", "dateNais", "lieuNais", "classe"]

    def on_model_change(self, form, model, is_created):
        if is_created:
            classe = form.classe.data
            if classe is not None:
                classe.nbrEtudiant = (classe.nbrEtudiant or 0) + 1
            return

        class_history = inspect(model).attrs.classe.history
        old_class = class_history.deleted[0] if class_history.deleted else None
        new_class = form.classe.data

        if old_class and old_class != new_class:
            old_class.nbrEtudiant = max((old_class.nbrEtudiant or 0) - 1, 0)

        if new_class and new_class != old_class:
            new_class.nbrEtudiant = (new_class.nbrEtudiant or 0) + 1

    def on_model_delete(self, model):
        if model.classe is not None:
            model.classe.nbrEtudiant = max((model.classe.nbrEtudiant or 0) - 1, 0)