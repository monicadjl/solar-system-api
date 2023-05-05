import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})
    #make sure that after every request is finished, clean up database.
    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    #take data and yield while you run test
    with app.app_context():
        db.create_all()
        #run test, yield app
        yield app
    #after test is ran, drop all that data
    with app.app_context():
        db.drop_all()

#this fixture creates a dummy client and calls any requests
#to test our apps.
@pytest.fixture
def client(app):
    return app.test_client()

#create data for tests to use on tests. 
@pytest.fixture
def two_saved_planets(app):
    # Arrange
    susi_planet = Planet(id=1,
                name="susi",
                position=3,
                moon_count=32) 
    
    monica_planet = Planet(id=2,
                name="monica",
                position=666,
                moon_count=69)

    db.session.add_all([susi_planet, monica_planet])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()