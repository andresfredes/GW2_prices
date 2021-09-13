from sqlalchemy import inspect
import pytest

def test_db_exists(db):
    assert db.engine.connect()

@pytest.mark.parametrize("table", [
    "items", "faves", "recipes", "price_history"
])
def test_db_create(db, table):
    inspector = inspect(db.engine)
    assert inspector.has_table(table)