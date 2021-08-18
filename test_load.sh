#!/bin/bash

export FLASK_APP=prices.py
export FLASK_ENV=testing
pytest .