from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    position = db.Column(db.Integer)
    moon_count = db.Column(db.Integer)

    def to_dict(self):
        new_dict = {}
        new_dict["id"] = self.id
        new_dict["name"] = self.name
        new_dict["position"] = self.position
        new_dict["moon_count"] = self.moon_count
        return new_dict
    
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"], 
                            position=planet_data["position"],
                            moon_count=planet_data["moon_count"])
        return new_planet