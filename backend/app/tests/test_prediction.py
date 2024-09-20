# Example usage
import requests

# Define the API endpoint
url = "http://localhost:5000/vqa"

# Prepare the image file and the question
image_path = './backend/app/tests/image.jpg'
question = "are the lungs normal appearing?"

# Prepare the file and form data
files = {'image': open(image_path, 'rb')}
data = {'question': question}

# Send the POST request with the image and question
response = requests.post(url, files=files, data=data)

# Print the response from the server
print(response.json())
