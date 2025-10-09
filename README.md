# Message Bus vs ZeroBus: Streaming Ingestion Performance Comparison

A Databricks demo application that compares the performance and implementation approaches for streaming data ingestion using traditional message bus connectors versus the new ZeroBus API.

## Overview

This project demonstrates the use of ZeroBus for directly writing to a UC table via the Python SDK and the REST API.

Running the main application will send data to the created or configured UC table. This repo includes helper steps to create an appriopriate catalog, schema, and table but you can adapt it however you want.

## Demo Behaviour
The demo application will send `AirQuality` messages to a UC table and include the source of the data. It has the following format:
```
{
    "timestamp": datetime,
    "device_name": str,
    "temp": float,
    "humidity": float,
    "source": str
}
```

## Instructions

1. Create a target table in your Databricks workspace - modify the following SQL code as needed:
```sql
CREATE CATALOG IF NOT EXISTS m_demo_catalog;
CREATE SCHEMA IF NOT EXISTS m_demo_catalog.demo_schema;
CREATE TABLE IF NOT EXISTS m_demo_catalog.demo_schema.air_quality (
    timestamp TIMESTAMP,
    device_name STRING,
    temp DOUBLE,
    humidity DOUBLE,
    source STRING
)
```

2. Create a .env file by copying the contents of `env.example` and filling in the required values.

3. Ensure that you have added granted the necessary permissions to your Databricks SP:
    - `USE CATALOG` on the target catalog
    - `USE SCHEMA` on the target schema
    - `MODIFY` on the target table
    - `SELECT` on the target table (for verification)

4. Activate your `uv` virtual environment from the root of the repo:
```bash
uv venv
source .venv/bin/activate
```

5. Create the protobuf files:
The provided script `create_proto.sh` uses the `generate_proto` tool from the Zerobus SDK to create the necessary Python files from your table definition in Unity Catalog.

Navigate to the `src` directory and run the script:
```bash
cd src
./create_proto.sh
cd ..
```
*Note: This script generates an authentication token from your Service Principal to authenticate with Unity Catalog, as the `generate_proto` tool expects a token.*

6. Run the demo applications:
You can now run the example scripts to send data to your table.

   **Python SDK Example**
   This script uses the asynchronous Zerobus Python SDK to send 10,000 records.
   ```bash
   python src/python_sdk_example.py
   ```

   **REST API Example**
   This script uses `requests` to send 10,000 records via the Zerobus REST API.
   ```bash
   python src/rest_api_example.py
   ```
   > **Note:** As of this writing, the REST API endpoint for the staging environment is not resolving correctly, and this script currently fails with a `NameResolutionError`. The correct endpoint is being investigated.




