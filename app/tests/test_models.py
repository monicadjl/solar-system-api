from app.models.planet import Planet
import pytest

def test_to_dict_no_missing_data(client):
    # Arrange
    test_data = Planet( id = 1, 
                       name = "Susi",
                       position = 3,
                       moon_count = 32)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Susi"
    assert result["position"] == 3
    assert result["moon_count"] == 32

def test_to_dict_missing_id(client):
    test_data = Planet( name = "Susi",
                       position = 3,
                       moon_count = 32)
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["name"] == "Susi"
    assert result["position"] == 3
    assert result["moon_count"] == 32


def test_to_dict_missing_name(client):
    # Arrange
    test_data = Planet( id = 1, 
                       position = 3,
                       moon_count = 32)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["position"] == 3
    assert result["moon_count"] == 32

def test_to_dict_missing_position(client):
    test_data = Planet( 
     id = 1,
     name = "Susi",
     moon_count = 32)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Susi"
    assert result["moon_count"] == 32

def test_from_dict_returns_planet():
    # Arrange
    planet_data = {
       "name": "Susi",
       "position": 3,
       "moon_count": 32
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Susi"
    assert new_planet.position == 3
    assert new_planet.moon_count == 32

def test_from_dict_with_no_name(client):
    # Arrange
    test_data = {
       "position": 3,
       "moon_count": 32
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        new_planet = Planet.from_dict(test_data)

def test_from_dict_with_no_position(client):
    # Arrange
    test_data = {
       "name": "Susi",
       "moon_count": 32
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'position'):
        new_planet = Planet.from_dict(test_data)

def test_from_dict_with_extra_keys(client):
    test_data = {
       "name": "Susi",
       "position": 3,
       "moon_count": 32,
       "extra": 'hello'
    }

    # Act
    new_planet = Planet.from_dict(test_data)

    # Assert
    assert new_planet.name == "Susi"
    assert new_planet.position == 3
