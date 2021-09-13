import pytest

@pytest.fixture(scope="module")
def app():
    from prices import create_app
    _app = create_app()
    return _app

@pytest.fixture(scope="module")
def app_context(app):
    with app.app_context():
        yield app

@pytest.fixture(scope="module")
def test_client(app_context):
    return app_context.test_client()

@pytest.fixture(scope="module")
def db(app_context):
    from prices import db as _db
    import prices.model as model
    _db.create_all()
    populate(_db)
    
    yield _db

    _db.session.remove()
    _db.drop_all()
    _db.get_engine(app_context).dispose()


def populate(db):
    pass
    """
    with db.session.begin():
        db.session.add(TEST_ITEMS)
        db.session.add(TEST_FAVOURITES)
        db.session.add(TEST_RECIPES)
        db.session.add(TEST_PRICE_HISTORIES)
    """

# from functools import wraps
# """ Wraps the __init__ method of a class that only requires it for populating
# test database. True data will be added by different program."""
# def auto_init(init):
#     @wraps(init)
#     def wrapper(self, **kwargs):
#         for k, v in kwargs.items():
#             setattr(self, k, v)
#         return init(self, **kwargs)
#     return wrapper