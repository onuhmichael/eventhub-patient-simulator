# Import required modules
# azure.eventhub: Library to interact with Azure Event Hub
from azure.eventhub import EventHubProducerClient, EventData
# json: Allows conversion between Python dictionaries and JSON format
import json
# time: Provides time-related functions, e.g., time delay and timestamps
import time
# random: Generates random values for simulating patient vitals
import random
# os: Allows interaction with the operating system, e.g., accessing environment variables
import os

# Load Event Hub Configuration from Environment Variables
# EVENT_HUB_CONNECTION_STRING and EVENT_HUB_NAME should be set in the environment
# These variables contain the connection string and the name of the Event Hub
CONNECTION_STRING = os.getenv("EVENT_HUB_CONNECTION_STRING")
EVENT_HUB_NAME = os.getenv("EVENT_HUB_NAME")

# Validate connection parameters
# Check if the connection string and event hub name are available
if not CONNECTION_STRING or not EVENT_HUB_NAME:
    # Raise an error if the variables are not set
    raise ValueError("Please set the environment variables 'EVENT_HUB_CONNECTION_STRING' and 'EVENT_HUB_NAME'")

# Generate simulated patient vitals data
def generate_patient_data(patient_id="patient_001"):
    """
    Generate random patient vitals data to simulate real-time monitoring.
    
    Args:
    - patient_id (str): Unique identifier for the patient. Default is "patient_001".
    
    Returns:
    - dict: Simulated patient data in JSON-compatible dictionary format.
    """
    return {
        # Generate the current timestamp in ISO 8601 format (UTC time)
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        
        # Assign the provided or default patient ID
        "patient_id": patient_id,
        
        # Generate a random heart rate between 50 and 120 bpm
        "heart_rate": random.randint(50, 120),
        
        # Generate a random systolic blood pressure between 90 and 160 mmHg
        "systolic_bp": random.randint(90, 160),
        
        # Generate a random diastolic blood pressure between 60 and 100 mmHg
        "diastolic_bp": random.randint(60, 100),
        
        # Generate a random SpO₂ (oxygen saturation) between 85.0 and 100.0%
        # Rounded to 2 decimal places for realistic data
        "spo2": round(random.uniform(85.0, 100.0), 2)
    }

# Send data to Azure Event Hub at regular intervals
def send_data_to_event_hub(interval=5):
    """
    Continuously send simulated patient data to Azure Event Hub.
    
    Args:
    - interval (int): Time in seconds between sending each batch of data.
    """
    # Create an Event Hub Producer Client using the connection string and Event Hub name
    producer = EventHubProducerClient.from_connection_string(
        conn_str=CONNECTION_STRING, eventhub_name=EVENT_HUB_NAME
    )
    print("Connecting to Event Hub...")

    try:
        # Infinite loop to continuously send data until interrupted
        while True:
            # Create a batch to hold the events (data messages)
            event_data_batch = producer.create_batch()
            
            # Generate simulated patient data
            data = generate_patient_data()
            
            # Convert the Python dictionary (data) to a JSON string
            message = json.dumps(data)
            
            # Add the JSON message to the batch
            event_data_batch.add(EventData(message))
            
            # Send the batch of events to the Event Hub
            producer.send_batch(event_data_batch)
            
            # Print confirmation message to console
            print(f"✅ Sent: {message}")
            
            # Wait for the specified interval before sending the next batch
            time.sleep(interval)

    # Graceful shutdown if the user interrupts (e.g., CTRL+C)
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
    
    # Ensure that the producer is properly closed even if an error occurs
    finally:
        producer.close()

# Main entry point
# This ensures that the script only runs when executed directly (not imported as a module)
if __name__ == "__main__":
    try:
        # Start sending data with a default interval of 5 seconds
        send_data_to_event_hub(interval=5)
    
    # Catch any unexpected errors and print a user-friendly message
    except Exception as e:
        print(f"❗ An error occurred: {e}")
