from src import create_app
import pytest

@pytest.fixture(scope="module")
def test_app():

    app = create_app()
    app.config.from_object('config.TestingConfig')
    with app.app_context():
        yield app