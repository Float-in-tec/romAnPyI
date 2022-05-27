from app import db

class MaiorRomano(db.Model):
    number = db.Column(db.String)
    value = db.Column(db.Integer, primary_key=True)
    def to_dict(self):
        return {
            "number": self.number,
            "value": self.value,
        }