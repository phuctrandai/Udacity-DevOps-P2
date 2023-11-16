from locust import HttpUser, task, between

class PredictionUser(HttpUser):
    wait_time = between(1, 3)  # Wait time between requests in seconds

    @task
    def predict(self):
        # Define the payload for the prediction request
        payload = {
            "CHAS":{
                "0":0
            },
            "RM":{
                "0":6.575
            },
            "TAX":{
                "0":296.0
            },
            "PTRATIO":{
                "0":15.3
            },
            "B":{
                "0":396.9
            },
            "LSTAT":{
                "0":4.98
            }
        }

        # Send a POST request to the prediction API endpoint
        headers = {"Content-Type": "application/json"}
        response = self.client.post("https://wa-udacity-devops-p2.azurewebsites.net/predict", json=payload, headers=headers)

        # Validate the response if needed
        if response.status_code == 200:
            response.success()
            # Extract and print the prediction result
            prediction_result = response.json()
            print(f"Prediction Result: {prediction_result}")
        else:
            response.failure("Failed")
            print(f"Error: {response.status_code}, {response.text}")

# Run Locust with the following command:
# locust -f locustfile.py
