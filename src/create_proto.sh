#!/bin/bash

source ../.venv/bin/activate

source .env

# Define an array of required variable names
required_vars=("DATABRICKS_HOST" "DATABRICKS_CLIENT_ID" "DATABRICKS_CLIENT_SECRET" "CATALOG" "SCHEMA" "TABLE")

# Loop through the array and check if each variable is set
for var_name in "${required_vars[@]}"; do
    if [ -z "${!var_name}" ]; then
        echo "Error: Required variable $var_name is not set. Check your .env file."
        exit 1
    fi
done

# Get SP token for generate_proto
SP_TOKEN=$(curl --request POST \
    --url "$DATABRICKS_HOST/oidc/v1/token" \
    --user "$DATABRICKS_CLIENT_ID:$DATABRICKS_CLIENT_SECRET" \
    --data "grant_type=client_credentials&scope=all-apis" | jq -r '.access_token')

if [ -z "$SP_TOKEN" ]; then
    echo "Error: Failed to get SP token. Check credentials and host."
    exit 1
fi

# Create the protobuf file
# Replace AirQuality with your name as required.
generate_proto \
    --uc-endpoint $DATABRICKS_HOST \
    --uc-token $SP_TOKEN \
    --table $CATALOG.$SCHEMA.$TABLE \
    --proto-msg "AirQuality" \
    --output "air_quality.proto"


# Compile the protobuf file
python3 -m grpc_tools.protoc -I. --python_out=. air_quality.proto
