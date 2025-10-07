import uuid
import time
import random


class DataGenerator:
    """
    Generates random data that meets a certain specification.
    """
    def __init__(self, device_ids: list[str]):
        if not device_ids:
            raise ValueError("device_ids list cannot be empty.")
        self.device_ids = device_ids

    def generate_data(self) -> dict:
        return {
            "event_id": str(uuid.uuid4()),
            "device_id": random.choice(self.device_ids),
            "event_timestamp": int(time.time() * 1_000_000),  # microseconds
            "metric_value": random.uniform(0.0, 100.0),
        }
