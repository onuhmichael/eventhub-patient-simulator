# 🏥 EventHub Patient Simulator
A Python script to simulate real-time patient vital data and send it to Azure Event Hub. It is ideal for testing, monitoring, and streaming data applications.
Simulate real-time patient vitals data and send it to Azure Event Hub for data streaming and analytics.

## 🚀 Features
- Generates random patient vitals data (Heart Rate, Blood Pressure, and SpO₂)
- Sends data to Azure Event Hub at a configurable interval
- Easy to configure using environment variables
- Ideal for IoT, real-time analytics, and Azure monitoring use cases

---

## 🛠️ Prerequisites

1. **Python 3.8+** installed.  
2. **Azure Event Hub** instance configured.  
3. `azure-eventhub` package installed.  

```bash
pip install azure-eventhub
```

---

## 📥 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/eventhub-patient-simulator.git
cd eventhub-patient-simulator
```

2. **Set up virtual environment (optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate     # On Windows
```

3. **Install required packages:**
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

### Set Environment Variables:
Set the following environment variables:
```bash
# Linux/Mac
export EVENT_HUB_CONNECTION_STRING="Your Event Hub Connection String"
export EVENT_HUB_NAME="Your Event Hub Name"

# Windows
set EVENT_HUB_CONNECTION_STRING=Your Event Hub Connection String
set EVENT_HUB_NAME=Your Event Hub Name
```

---

## ▶️ Usage

1. Run the script:
```bash
python simulate_patient_data.py
```

2. To stop the simulation:
- Press `CTRL + C` to terminate the process.

---

## ⚡ Example Output
```bash
Connecting to Event Hub...
✅ Sent: {"timestamp": "2025-03-24T12:00:00Z", "patient_id": "patient_001", "heart_rate": 75, "systolic_bp": 120, "diastolic_bp": 80, "spo2": 98.5}
✅ Sent: {"timestamp": "2025-03-24T12:00:05Z", "patient_id": "patient_001", "heart_rate": 85, "systolic_bp": 115, "diastolic_bp": 78, "spo2": 99.0}
```

---

## 🔥 Advanced Configuration
- **Change interval:** Modify the `interval` value in `send_data_to_event_hub()` if you want to adjust the time between messages.
```python
send_data_to_event_hub(interval=3)  # Sends data every 3 seconds
```

---

## 📄 License
This project is licensed under the MIT License.

---

## 🧑‍💻 Contributing
Feel free to submit issues, feature requests, or pull requests to improve this project!

---

