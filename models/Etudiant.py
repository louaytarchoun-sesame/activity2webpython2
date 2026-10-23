from extensions import db

class Etudiant(db.Model):
    nce = db.Column(db.String(5), primary_key=True)
    nom = db.Column(db.String(15))
    prenom = db.Column(db.String(15))
    dateNais = db.Column(db.Date())
    lieuNais = db.Column(db.String(15))

    classe_id = db.Column(
        db.String(10),
        db.ForeignKey('classe.codClass', onupdate='CASCADE', ondelete='SET NULL'),
        nullable=True
    )
    classe = db.relationship("Classe", back_populates='etudiants', passive_deletes=True)

    absences = db.relationship("Absence", back_populates="etudiant")

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.classe.nomClass if self.classe else 'Aucune classe'})"