from flask import Blueprint, jsonify, abort, make_response, request
from os import abort
from app.models.planet import Planet
from app import db

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_model_by_id(cls, id):
    #handle invalid planet id, return 400
    try:
        id = int(id)
    except: 
        abort(make_response({"msg": f"{cls.__name__}{id} is invalid."}, 400))
    model = cls.query.get(id)

    if model is None:
        abort(make_response({"msg": f"{cls.__name__} {id} not found."}, 404))

    return model 


    
@planets_bp.route("", methods=["GET"])
def get_all_planets():
    
    title_query = request.args.get("name")

    if title_query:
        planets = Planet.query.filter_by(name=title_query)
    #grab all info from the instance planet table
    else:
        planets = Planet.query.all()
        
    all_planets = [planet.to_dict() for planet in planets]
    return jsonify(all_planets), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def single_planet(planet_id):
    planet = validate_model_by_id(Planet, planet_id)
    return jsonify(planet.to_dict()), 200

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    get_planet = Planet.query.get(planet_id)
    planet = validate_model_by_id(Planet, planet_id)

    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.position = request_body["position"]
    planet.moon_count = request_body["moon_count"]

    db.session.commit()
    
    return jsonify(planet.to_dict()), 200

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_single_planet(planet_id):
    planet = validate_model_by_id(Planet, planet_id)

    db.session.delete(planet)    
    db.session.commit()

    return f"Planet at id:{planet_id} was sucessfully deleted", 200

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        position=request_body["position"],
                        moon_count=request_body["moon_count"])
    db.session.add(new_planet)
    db.session.commit()

    return {
        "id": new_planet.id,
        "name": new_planet.name,
        "msg": "Successfully created"
    }, 201