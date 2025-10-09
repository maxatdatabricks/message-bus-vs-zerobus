import asyncio
from datetime import datetime, timezone
import os
import sys
import time

import air_quality_pb2
from dotenv import load_dotenv
from loguru import logger
from zerobus_sdk import StreamConfigurationOptions, TableProperties, get_zerobus_token
from zerobus_sdk.aio import ZerobusSdk

# --- Logging Setup ---
logger.remove()
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
)

# --- Configuration ---
load_dotenv()
REQUIRED_VARS = [
    "DATABRICKS_HOST",
    "DATABRICKS_CLIENT_ID",
    "DATABRICKS_CLIENT_SECRET",
    "ZEROBUS_WORKSPACE_ID",
    "CATALOG",
    "SCHEMA",
    "TABLE",
]
config = {var: os.getenv(var) for var in REQUIRED_VARS}

if not all(config.values()):
    missing_vars = [var for var, value in config.items() if not value]
    logger.error(f"Missing required environment variables: {', '.join(missing_vars)}")
    sys.exit(1)

TABLE_FQN = f"{config['CATALOG']}.{config['SCHEMA']}.{config['TABLE']}"
ZEROBUS_SERVER_ENDPOINT = (
    f"{config['ZEROBUS_WORKSPACE_ID']}.zerobus.us-west-2.staging.cloud.databricks.com"
)

# --- Python ZeroBus SDK Client ---
sdk_handle = ZerobusSdk(ZEROBUS_SERVER_ENDPOINT)
AirQuality = air_quality_pb2.AirQuality  # pylint: disable=no-member
table_properties = TableProperties(TABLE_FQN, AirQuality.DESCRIPTOR)


async def send_sdk_records():
    """Initializes a stream and sends 10,000 records using the Python SDK."""
    logger.info("Starting Python SDK example...")

    options = StreamConfigurationOptions(
        token_factory=lambda: get_zerobus_token(
            TABLE_FQN,
            config["ZEROBUS_WORKSPACE_ID"],
            config["DATABRICKS_HOST"],
            config["DATABRICKS_CLIENT_ID"],
            config["DATABRICKS_CLIENT_SECRET"],
        )
    )

    stream = await sdk_handle.create_stream(table_properties, options)
    logger.info(f"Stream created with ID: {stream.stream_id}")

    num_records = 10_000
    start_time = time.time()

    for i in range(num_records):
        record = AirQuality(
            timestamp=int(datetime.now(timezone.utc).timestamp() * 1_000_000),
            device_name=f"device_sdk_{i}",
            temp=20 + (i % 10),
            humidity=50 + (i % 20),
            source="python_sdk",
        )
        await stream.ingest_record(record)
        if (i + 1) % 1000 == 0:
            logger.info(f"Sent {i + 1}/{num_records} records...")

    logger.info("All records sent. Flushing stream...")
    await stream.flush()
    await stream.close()

    end_time = time.time()
    duration = end_time - start_time
    logger.info(
        f"Successfully sent {num_records} records in {duration:.2f} seconds ({num_records / duration:.2f} records/sec)."
    )
    logger.info("Python SDK example finished.")


if __name__ == "__main__":
    asyncio.run(send_sdk_records())
