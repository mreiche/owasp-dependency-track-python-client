#!/usr/bin/env bash

PATCH_FILE="$1"
USE_PATCH_FILE="${PATCH_FILE:-patch-v1.json}"

curl -lo openapi-v1.json http://localhost:8080/api/openapi.json
curl -lo schema-v2.yaml http://localhost:8080/api/v2/openapi.yaml
#jq -s 'reduce .[] as $item ({}; . * $item)' openapi.json patch.json > schema.json
jq -s '.[0] * .[1]' openapi-v1.json "${USE_PATCH_FILE}" > schema-v1.json
#jq 'del(.components.schemas.FindingAttribution)' schema-v.json > tmp.json
#mv tmp.json schema.json
openapi-python-client generate --overwrite --path ./schema-v1.json --meta none --config generator-config-v1.yml
openapi-python-client generate --overwrite --path ./schema-v2.yaml --meta none --config generator-config-v2.yml
