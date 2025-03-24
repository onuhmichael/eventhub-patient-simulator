from azure.eventhub import EventHubProducerClient, EventData
import json
import time
import random
import os

# Load Event Hub Configuration from Environment Variables
CONNECTION_STRING = os.getenv("EVENT_HUB_CONNECTION_STRING")
EVENT_HUB_NAME = os.getenv("EVENT_HUB_NAME")

# Validate connection parameters
if not CONNECTION_STRING or not EVENT_HUB_NAME:
    raise ValueError("Please set the environment variables 'EVENT_HUB_CONNECTION_STRING' and 'EVENT_HUB_NAME'")

# Generate simulated patient vitals data
def generate_patient_data(patient_id="patient_001"):
    """Generate random patient vitals data."""
    return {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "patient_id": patient_id,
        "heart_rate": random.randint(50, 120),  # Random heart rate
        "systolic_bp": random.randint(90, 160),  # Random systolic blood pressure
        "diastolic_bp": random.randint(60, 100),  # Random diastolic blood pressure
        "spo2": round(random.uniform(85.0, 100.0), 2)  # Random SpO₂ levels
    }

# Send data to Event Hub
def send_data_to_event_hub(interval=5):
    """Send simulated data to Azure Event Hub at regular intervals."""
    producer = EventHubProducerClient.from_connection_string(conn_str=CONNECTION_STRING, eventhub_name=EVENT_HUB_NAME)
    print("Connecting to Event Hub...")

    try:
        while True:
            event_data_batch = producer.create_batch()
            data = generate_patient_data()
            message = json.dumps(data)
            event_data_batch.add(EventData(message))
            producer.send_batch(event_data_batch)
            print(f"✅ Sent: {message}")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
    finally:
        producer.close()

# Main entry point
if __name__ == "__main__":
    try:
        send_data_to_event_hub(interval=5)
    except Exception as e:
        print(f"❗ An error occurred: {e}")

