#!/bin/bash

newrelic-admin run-program uvicorn --factory app:create_app --host=0.0.0.0 --port="$PORT"
