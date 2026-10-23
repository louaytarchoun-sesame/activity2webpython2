from extensions import db

class Matiere(db.Model):
    codeMat = db.Column(db.String(10), primary_key=True)
    intMat = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(40))
    
    absences = db.relationship("Absence", back_populates="matiere")
    
    def __str__(self):
        return self.intMat or self.codeMat