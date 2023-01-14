# ExpenseTrackingApi
This is a RESTful API that allows clients to send income and expense data. The API has the following endpoints:

POST /income - This endpoint allows clients to submit income data. The client is expected to send a JSON payload in the request body containing the income data.

POST /expense - This endpoint allows clients to submit expense data. The client is expected to send a JSON payload in the request body containing the expense data.

GET /income - This endpoint retrieves all the income data that was previously submitted to the API.

GET /expense - This endpoint retrieves all the expense data that was previously submitted to the API.



The response from the API will be in JSON format, and the HTTP status code of the response will indicate the success or failure of the operation.

## Development

1.git clone this repository

2.cd into the local repository

3.Create virtual enviornment: python -m venv env

4.Install python dependencies: pip install -r requierments.txt

5.cd in to app.py

6.Flask Shell > from app import db > db.create_all()

7.python app.py


