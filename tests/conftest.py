import pytest
from prices import create_app

@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    testing_client = app.test_client()
    context = app.app_context()
    context.push()

    yield testing_client

    context.pop()