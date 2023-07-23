Hello there!

I hope this message finds you well. I wanted to share with you the basic 
implementation of the assignment you requested. As per your requirements,
I have implemented the tasks in a serial manner. However, I would like 
to point out that the implementation can be improved significantly by implementing 
CPU-heavy tasks in parallel. Unfortunately, due to time constraints, 
I was only able to implement it in a serial manner.


Kindly follow the steps to setup and run the application

- Open terminal 
- setup a virtualenv for best practice
- python -m venv env
- activate the env
- env\Scripts\activate.bat
- pip install -r requirements.txt
- python app.py


To use the API , use any API testing platform eg.POSTMAN

- make a new GET request with URL: http://127.0.0.1:5000/asset_report
- Provide epoch time in Query params , as start_time & end_time

Given it's a long running task we can also implement it in a async manner 
with celery, but i've gone ahead with a basic request-respone due to time 
boundaries. 

**IT CAN TAKE 2-3Mins FOR 3-4 MONTHS OF DATA 