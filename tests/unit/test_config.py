import os
import config

db_in_memory = "mariadb+mariadbconnector:///:memory:"

def test_testing_config(app):
    # Should default to testing config when performing tests
    assert app.config['DEBUG']
    assert app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == db_in_memory

def test_development_config(app):
    app.config.from_object(config.DevelopmentConfig)
    assert app.config['DEBUG']
    assert not app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == db_in_memory
        
def test_production_config(app):
    app.config.from_object(config.ProductionConfig)
    assert not app.config['DEBUG']
    assert not app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] != db_in_memory