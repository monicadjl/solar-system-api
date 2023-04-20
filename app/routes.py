from flask import Blueprint, jsonify

class Planet():
    def __init__(self, id, name, position, moon_count=0):
        self.id = id
        self.name = name 
        self.position = position
        self.moon_count = moon_count

planets = [
    Planet(1, "Mercury", 1),
    Planet(2, "Venus", 2),
    Planet(3, "Earth", 3, 1),
    Planet(4, "Mars", 4, 2),
    Planet(5, "Jupiter", 5, 95),
    Planet(6, "Saturn", 6, 83),
    Planet(7, "Uranus", 7, 27),
    Planet(8, "Neptune", 8, 14),
    Planet(9, "Pluto", 9, 5)
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planet_dict = [vars(planet) for planet in planets]
    return jsonify(planet_dict), 200