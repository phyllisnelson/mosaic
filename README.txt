## How to Deploy
```
make run

```
## How to Call Api Endpoint
```
curl --location 'http://localhost:8006/electric-ranges?model_year=<int>'
```
### Example
```
curl --location 'http://localhost:8006/electric-ranges?model_year=2025'
```



Task Overview:

You are tasked with building a FastAPI application that accesses an external API containing electric vehicle data from Washington State Department of Licensing. The goal is to build an endpoint that accepts a specific vehicle model year and returns aggregated data for vehicles with that model year grouped by vehicle make.

 

Data Source:

You will be using data from the following API, which provides information on electric vehicles in Washington:

API Documentation: Washington EV Data
The API for the data is available without any authentication. Don’t worry about creating an App Token for this project. 
 

Requirements:

Create an API using FastAPI that contains one endpoint.
The endpoint should accept a parameter that represents a vehicle model year.
For the given vehicle model year, the endpoint should return the number of vehicles and the average electric range for the vehicles aggregated by the vehicle make.
 

Submission:

Please submit the code by providing a public GitHub project link.
This should include instructions on how to run your application.
 

Notes:

We don’t expect you to have to spend more than one hour working on the project.
There are no specific requirements for how your application accepts the model year parameter or the exact format of the response that contains the aggregated data by vehicle make.
You only need to work with the default limit of the first 1,000 records returned from the Washington EV API. Don’t worry about using the limit and offset parameters when making requests.
The expectation isn’t that this needs to be production quality, but you should be prepared to speak about ways you would improve the code if you were given more time.
