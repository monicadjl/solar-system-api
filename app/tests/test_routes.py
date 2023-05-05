


#get all books and return no records
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


#get one planet by id
def test_get_one_planets(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
                "id" : 1,
                "name" : "susi",
                "position": 3,
                "moon_count": 32
    }

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
    assert response_body["position"] == 44
    assert response_body["name"] == "selene"

    
