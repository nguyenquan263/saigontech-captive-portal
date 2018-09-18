from preparation.init import db, ma

class info(db.Model):
    __tablename__ = 'infos'

    name = db.Column(db.String(50), nullable = False)
    is_student = db.Column(db.Integer, nullable = False)
    phone = db.Column(db.String(15), nullable = False, primary_key = True)
    need = db.Column(db.String(100), nullable = False)

    def __init__(self, name, is_student, phone, need):
        self.name = name
        self.is_student = is_student
        self.phone = phone
        self.need = need

class info_schema(ma.Schema):
    class Meta:
        fields = ('name', 'is_student', 'phone', 'need')

db.create_all()