from flask import Blueprint, jsonify, abort, make_response, request
from os import abort
from app.models.planet import Planet
from app import db


# class Planet():
#     def __init__(self, id, name, position, moon_count=0):
#         self.id = id
#         self.name = name 
#         self.position = position
#         self.moon_count = moon_count

#We need to migrate this data to our SQL. 
# planets = [
#     Planet(1, "Mercury", 1),
#     Planet(2, "Venus", 2),
#     Planet(3, "Earth", 3, 1),
#     Planet(4, "Mars", 4, 2),
#     Planet(5, "Jupiter", 5, 95),
#     Planet(6, "Saturn", 6, 83),
#     Planet(7, "Uranus", 7, 27),
#     Planet(8, "Neptune", 8, 14),
#     Planet(9, "Pluto", 9, 5)
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# def validate_planet(planet_id):
#     #handle invalid planet id, return 400
#     try:
#         planet_id = int(planet_id)
#     except: 
#         abort(make_response({"msg": f"planet id: {planet_id} is invalid."}, 400))
#     #search for planet_id in data and return planet
#     for planet in planets:
#             if planet.id == planet_id:
#                 abort(make_response(jsonify(vars(planet)), 200))
#     #return 404 for nonexistant planet
#     abort(make_response({"msg": f"planet id: {planet_id} not found."}, 404))

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planet_dict = [vars(planet) for planet in planets]
    return jsonify(planet_dict), 200

@planets_bp.route("/<planet_id>", methods=["GET"] )
def single_planet(planet_id):
    planet = validate_planet(planet_id)
    return planet

@planets_bp.route("", methods=['POST'])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                         position=request_body["position"], 
                         moon_count=request_body["moon_count"])
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} sucessfully created", 201)
