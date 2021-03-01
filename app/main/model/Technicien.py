from .. import db


class Technicien(db.Model):
    """ Technicien Model for storing technicien related details """
    __tablename__ = "technicien"
    __table_args__ = {'extend_existing': True}

    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # email = db.Column(db.String(255), unique=True, nullable=False)
    # registered_on = db.Column(db.DateTime, nullable=False)
    # admin = db.Column(db.Boolean, nullable=False, default=False)
    # public_id = db.Column(db.String(100), unique=True)
    # username = db.Column(db.String(50), unique=True)
    # password_hash = db.Column(db.String(100))

    # dfdsfdsf

    code = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    intervention = db.Column(db.String(200))

    def __repr__(self):
        return "<Intervention '{}'>".format(self.code)
