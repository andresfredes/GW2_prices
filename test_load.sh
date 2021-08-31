#!/bin/bash

export FLASK_APP=prices.py
export FLASK_ENV=testing

export DB_USERNAME=andres
export DB_PASSWORD=andres
export DB_HOSTPORT=localhost
export DB_NAME=gw2p

pytest .