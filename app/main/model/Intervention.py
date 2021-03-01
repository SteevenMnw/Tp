from .. import db


class Intervention(db.Model):
    """ Intervention Model for storing intervention related details """
    __tablename__ = "intervention"
    __table_args__ = {'extend_existing': True}

    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # email = db.Column(db.String(255), unique=True, nullable=False)
    # registered_on = db.Column(db.DateTime, nullable=False)
    # admin = db.Column(db.Boolean, nullable=False, default=False)
    # public_id = db.Column(db.String(100), unique=True)
    # username = db.Column(db.String(50), unique=True)
    # password_hash = db.Column(db.String(100))rogramm

    # dfdsfdsf

    code = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ref_client = db.Column(db.String(50), unique=True, nullable=False)
    piece = db.Column(db.String(100))
    probleme = db.Column(db.String(250))
    reussi = db.Column(db.Boolean, nullable=False, default=False)

    # @property
    # def password(self):
    #     raise AttributeError('password: write-only field')

    # @password.setter
    # def password(self, password):
    #     self.password_hash = flask_bcrypt.generate_password_hash(
    #         password).decode('utf-8')

    def __repr__(self):
        return "<Intervention '{}'>".format(self.code)
