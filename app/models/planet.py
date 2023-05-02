from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    position = db.Column(db.Integer)
    moon_count = db.Column(db.String)

    def make_dict(self):
        return {"id": self.id,
                "name": self.name,
                "position": self.position,
                "moon_count": self.moon_count} 