# Boston Housing Price Prediction

## How to execute the code
### Software Requirements
1. Python 3.8
2. Scikit-Learn
3. Pandas
4. Matplotlib
5. Flask
6. Docker
7. Postman 

### Steps
1. Download the code as zip file to any directory
2. Go to the folder the zip file was downloaded and unzip the file
3. Start the Docker container
4. Open the command prompt and run following commands:
    1. Go to the directory that has unzipped code file 
    2. run 'docker build -t Boston-model .' command
    3. run 'docker run -d -p 8080:8080 Boston-model' command
5. Open Docker Dashboard and see the boston-model up and running
6. Open Postman and follow:
    1. change the HTTP method to 'POST' from dropdown
    2. set the url as 'http://0.0.0.0:8080/predict' 
    3. In the 'Body' section, change the type to 'JSON'
    4. copy the request JSON from request.json file and paste it in the body.
    5. click 'Send'
7. You can see the response with the predicted house price as a json in 'Response' section.
