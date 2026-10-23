from flask_admin.contrib.sqla import ModelView

class MatiereAdmin(ModelView):
    form_excluded_columns = ["absences"]
    
    form_columns = ["codeMat", "intMat", "description"]