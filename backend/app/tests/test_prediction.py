import requests

# Define the API endpoint
url = "http://127.0.0.1:5000/vqa"

# Prepare the image file and the question
image_path = './backend/app/tests/image.jpg'
question = "are the lungs normal appearing?"

# Prepare the file and form data
files = {'image': open(image_path, 'rb')}
data = {'question': question}

# Optionally, add headers
headers = {
    'User-Agent': 'MyTestScript/1.0',
}

# Send the POST request with the image and question
response = requests.post(url, files=files, data=data, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.text)