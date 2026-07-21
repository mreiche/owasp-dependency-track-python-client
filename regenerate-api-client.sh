#!/usr/bin/env bash

PATCH_FILE="$1"
USE_PATCH_FILE="${PATCH_FILE:-patch-full.json}"

curl -lo openapi.json http://localhost:8080/api/openapi.json
#curl -lo openapi.yaml http://localhost:8080/api/v2/openapi.yaml
#jq -s 'reduce .[] as $item ({}; . * $item)' openapi.json patch.json > schema.json
#jq -s '.[0] * .[1]' openapi.json "${USE_PATCH_FILE}" > schema.json
#jq 'del(.components.schemas.FindingAttribution)' schema.json > tmp.json
#mv openapi.json schema.json
openapi-python-client generate --overwrite --path ./openapi.json --meta none --config generator-config.yml
