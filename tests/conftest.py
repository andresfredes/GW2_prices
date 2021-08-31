import pytest
from prices import create_app, db

@pytest.fixture(scope='module')
def app():
    app = create_app()
    return app

@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    testing_client = app.test_client()
    context = app.app_context()
    context.push()
    with context:
        db.create_all()
        yield testing_client
        db.drop_all()
    context.pop()