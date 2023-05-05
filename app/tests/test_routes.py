#get all books and return no records
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets_with_populated_db(client, two_saved_planets):
    response = client.get('/planets')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [
        {
            "id": 1,
            "name": "susi",
            "position": 3,
            "moon_count": 32
        },
        {
            "id": 2,
            "name": "monica",
            "position" : 666,
            "moon_count": 69
        },
    ]


#get one planet by id
def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
                "id":1,
                "name":"susi",
                "position":3,
                "moon_count":32
    }

#create one planet
def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
                "name": "selene",
                "position": 44,
                "moon_count": 92347 }
    )
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert "msg" in response_body      
    assert response_body["id"] == 1
    assert response_body["name"] == "selene"

def test_update_one_planet_updates_planet_in_db(client, two_saved_planets):
    response = client.put("/planets/1", json={
        "name": "updated_name",
        "position": 1,
        "moon_count": 1
        }
    )

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["id"] == 1
    assert response_body["name"] == "updated_name"
    assert response_body["position"] == 1