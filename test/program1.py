# program1.py
import requests

def perform_work_on_data_1(data):
    # Your logic to process data in Program 1
    # For example, let's assume it just adds a prefix
    return f"Processed by Program 1: {data}"

# Assuming you have some data to start with
initial_data = "Hello, World!"

# Step 1: Perform some work on the data
processed_data_1 = perform_work_on_data_1(initial_data)

# Step 2: Send the processed data to the middleware
response = requests.post("http://localhost:5000/process_data", json={"data": processed_data_1})

# Step 4: Display the final output
print("Final Output:", response.json()["result"])
