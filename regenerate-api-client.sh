#!/usr/bin/env bash

openapi-python-client generate --overwrite --url http://localhost:8081/api/openapi.json --meta none --config generator-config.yml
