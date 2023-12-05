import random
import string
import datetime
import json


# Function to generate a random flight number
def generate_flight_number():
    return "".join(random.choices(string.ascii_uppercase, k=2)) + str(
        random.randint(1000, 9999)
    )


# Function to generate a random flight status
def generate_flight_status():
    return random.choice([0, 1])  # 0: Normal, 1: Delayed, 2: Cancelled


# Function to generate a random time
def generate_time():
    return datetime.time(random.randint(0, 23), random.randint(0, 59)).strftime("%H:%M")


# Function to generate mock data
def generate_mock_data():
    flight_number = generate_flight_number()
    flight_status = generate_flight_status()
    planned_departure_time = generate_time()

    if flight_status == 0:  # Normal status
        actual_departure_time = planned_departure_time
    elif flight_status == 1:  # Delayed status
        delay_minutes = random.randint(10, 120)  # Simulating delay of 10 to 120 minutes
        planned_departure = datetime.datetime.strptime(planned_departure_time, "%H:%M")
        actual_departure = planned_departure + datetime.timedelta(minutes=delay_minutes)
        actual_departure_time = actual_departure.time().strftime("%H:%M")
    else:  # Cancelled status
        actual_departure_time = "N/A"

    return {
        "flight_number": flight_number,
        "flight_status": flight_status,
        "planned_departure_time": planned_departure_time,
        "actual_departure_time": actual_departure_time,
    }


# Generate mock data rows and write to a JSON file
num_rows = 1000  # Number of rows in the dataset
output_filename = "mock_dataset.json"

data = []
for _ in range(num_rows):
    data_row = generate_mock_data()
    data.append(data_row)

with open(output_filename, "w") as file:
    json.dump(data, file, indent=4)

print(f"Mock dataset generated and saved to '{output_filename}'")
