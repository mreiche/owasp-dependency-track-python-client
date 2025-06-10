#!/usr/bin/env bash

curl -lo openapi.json http://localhost:8081/api/openapi.json
#jq -s 'reduce .[] as $item ({}; . * $item)' openapi.json patch.json > schema.json
jq -s '.[0] * .[1]' openapi.json patch.json > schema.json
jq 'del(.components.schemas.FindingAttribution)' schema.json > tmp.json
mv tmp.json schema.json
openapi-python-client generate --overwrite --path ./schema.json --meta none --config generator-config.yml
