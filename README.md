Problem

Your assignment is to create and submit a working digital version of the aircraft passenger
capacity issue, ZipAirlines, along with instructions for the interviewer to run the code. Please
use Python to create the solution. More detailed requirements are listed below.

Requirements
We are creating a new software for an airline company called “ZipAirlines”.
- The company is assessing 10 different airplanes.
- Each airplane has a fuel tank of (200 liters * id of the airplane) capacity. For example, if
the airplane id = 2, the fuel tank capacity is 2*200 = 400 liters.
- The airplane fuel consumption per minute is the logarithm of the airplane id multiplied by
0.80 liters.
- Each passenger will increase fuel consumption for additional 0.002 liters per minute.

Write a RESTful API using Django Rest Framework to:

● Allow for input of 10 airplanes with user defined id and passenger assumptions
● Print total airplane fuel consumption per minute and maximum minutes able to fly

Deployment instructions:

- clone https://github.com/KhayrulloevDD/ziphr.git repository;
- create virtual environment and activate it(optional);
- install dependencies from the requirements.txt file (pip install -r requirements.txt);
- migrate migrations (python manage.py migrate);
- run the server (python manage.py runserver).

Usage instructions:

 - GET:    http://127.0.0.1:8000/api/v1/zip_airlines/airplanes/ to get list of airplanes
 - POST:   http://127.0.0.1:8000/api/v1/zip_airlines/airplanes/ - to post airplane data
   required data:
    {
        "id": positive integer > 1,
        "passengers": none negative integer,
    }
 - GET:    http://127.0.0.1:8000/api/v1/zip_airlines/airplanes/{id} to get airplane detail data
 - PUT:    http://127.0.0.1:8000/api/v1/zip_airlines/airplanes/{id} to update airplane data
   required data:
    {
        "id": positive integer > 1,
        "passengers": none negative integer,
    }
 - DELETE: http://127.0.0.1:8000/api/v1/zip_airlines/airplanes/{id} to delete airplane data
