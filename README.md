# fastapi_code_chalenge
A Car Management API

This is an api for managing a public transport company,it allows the user to get by id ,get all cars,add,update,delete the records for the car using the HTTP requests

# FEATURES
# ADD A NEW CAR:
Sending the POST request to the "/add_car" endpoint with the car details in the request body adds the records of the car into the database
# UPDATE EXISTING CAR:
Sending the PUT request to the "add_car/{car_id}" endpoint with the car id in the url and the updated car details updates the car details into the database
# DELETE CAR:
Sending the DELETE request to the "/car/delete{id}" endpoint  with the car id in the url deletes the selected car and its details
# GET ALL CARS
sending the GET request to the '/' endpoint shows all the instances of cars available in the database
# GET CAR BY ID(single_car)
sending the GET request to the '/cars{id}' endpoint with the car id in the url allows one to aquire a single car with its details from the whole list of cars
