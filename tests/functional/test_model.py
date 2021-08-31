from prices import db

def test_db_create(test_client):
    with test_client:
        assert db.engine.table_names()