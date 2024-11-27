# brainagric

This is the Brain Agriculture Technical Test!

This is a demo of Web API implementation using Django DRF (Django REST framework). It was implemented in less than 3 days!

* Usage of solution:
- The solution can be tested online in the following link: http://206.81.10.170:8008/api/ (if you have issues to access the solution, please let me know)
- Please see below a list of available APIs:
{
    "List Rural Producers": "producers/ [GET]",
    "Add a Rural Producer": "producers/ [POST]",
    "Update a Rural Producer": "producers/<id> [PUT]",
    "Delete a Rural Producer": "producers/<id> [DELETE]",
    "List Rural Producers by State": "producers/list/state",
    "List Rural Producers by Crop": "producers/list/crop",
    "List Rural Producers by Area Usage": "producers/list/area"
}

About the solution's description, please see details below:

* It consists of a rural producer registration with the following data:

- CPF or CNPJ
- Name of the producer
- Name of the farm
- City
- State
- Total area in hectares of the farm
- Agricultural area in hectares
- Area of ​​vegetation in hectares
- Crops planted (Soybean, Corn, Cotton, Coffee, Sugarcane)

* Business requirements

The user must be able to register, edit, and delete rural producers.
The system must validate incorrectly entered CPF and CNPJ.
The sum of the agricultural area and vegetation must not be greater than the total area of ​​the farm
Each producer can plant more than one crop on their farm.
The platform should have a Dashboard that displays:
Total number of farms in quantity
Total number of farms in hectares (total area)
Pie chart by state.
Pie chart by crop.
Pie chart by land use (Agricultural area and vegetation)

* Back-end requirements

- Save the data in a Postgres database using Django as the Backend layer, and provide the endpoints to register, edit, and delete rural producers, in addition to the endpoint that returns the totals to the dashboard.
- The creation of the "mock" data structures is part of the evaluation.

Any additional questions, please send me a message by LinkedIn. Thanks!




