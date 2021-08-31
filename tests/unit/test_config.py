import os

def test_testing_config(app):
    # Should default to testing config when performing tests
    assert app.config['DEBUG']
    assert app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == (
        "mariadb+mariadbconnector://"
        f"andres:{os.environ.get('DB_PASSWORD')}@localhost/gw2p"
    )