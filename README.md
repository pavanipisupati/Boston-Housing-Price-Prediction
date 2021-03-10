# Boston Housing Price Prediction

## How to execute the code
### Software Requirements
1. Python 3.8
2. Scikit-Learn
3. Pandas
4. Matplotlib
5. Seaborn
6. Flask
7. Flask_api
8. Coverage
9. Zappa
10. Docker
11. Postman 

### Steps to deploy in Docker
1. Download the code as zip file to any directory
2. Go to the folder the zip file was downloaded and unzip the file
3. Start the Docker container
4. Open the command prompt and run following commands:
    1. Go to the directory that has unzipped code file 
    2. run `docker build -t Boston-model .` command
    3. run `docker run -d -p 8080:8080 Boston-model` command
5. Open Docker Dashboard and see the boston-model up and running
6. Open Postman and follow:
    1. change the HTTP method to 'POST' from dropdown
    2. set the url as 'http://0.0.0.0:8080/predict' 
    3. In the 'Body' section, change the type to 'JSON'
    4. copy the request JSON from request.json file and paste it in the body.
    5. click 'Send'
7. You can see the response with the predicted house price as a json in 'Response' section.

### Steps to deploy in AWS Lambda using Zappa
1. Zappa requires a virtual environment
2. Create a virtual env for zappa using
    `python -m venv venv`
3. Activate the virtual env by 
    `source venv/bin/activate`
4. Install all the required python modules used by the app as
    `pip install pandas, sklearn,...(use pip for each module separately)`
5. Initialize zappa
    `zappa init`
6. The above command prompts a few questions like dev/production, aws profile, s3-bucket name
7. Specify all the values in the prompts
8. It then generates a 'zappa_settings.json' file based on the values specified
9. Deploy the application
    `zappa deploy dev`
10. It runs and deploys the application and returns a message
    Deployment complete! Link - https://lokd199fea.execute-api.us-east-2.amazonaws.com/dev (changes with every deployment)
11. Open postman and add a request body with POST and the url is:
    https://lokd199fea.execute-api.us-east-2.amazonaws.com/dev/predict
12. We can see the prediction in the response when we send the request.
13. We can undeploy using
    `zappa undeploy dev`

### Unit testing and Code coverage
1. Test files are placed inside the `tests/` folder.
2. The files test the api calls for valid and invalid/incomplete input requests
3. To get the coverage report of the code executed, we need to install coverage
    `pip install coverage`
4. Run the following command to test the api test class
    `coverage run app/server_app.py`
5. Get the coverage report using
    `coverage report -m`
6. A coverage report looks something like this:

