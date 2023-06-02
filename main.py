from fastapi import FastAPI
from pydantic import BaseModel
from car import Car,session
from typing import List,Optional

app = FastAPI()
class CarSchema(BaseModel):
  number_plate:int
  vehicle_name:str
  plate_name:str
  conductor:str
  driver:str
  age:int
  route:str
  class Config:
    orm_mode = True
    # this is the class for the updated data
class UpdatedCarSchema(BaseModel):
  number_plate:Optional[int] = None
  vehicle_name:Optional[str] = None
  plate_name:Optional[str] = None
  conductor:Optional[str] = None
  driver:Optional[str] = None
  age:Optional[int] = None
  route:Optional[str] = None
  class Config:
    orm_mode = True

  # this is the route to get all the cars

@app.get('/')
def get_all_cars() -> List[CarSchema]:
  cars = session.query(Car).all()
  return cars
# this is the route to get a single car by their respective id
@app.get('/cars{id}')
def get_single_car(id:int) ->CarSchema:
  single = session.query(Car).filter_by(number_plate=id).first()
  return single
# this is the route to add a new car with its details
@app.post('/add_car')
def add_car(car:CarSchema) ->CarSchema:
  vehicle =Car(**dict(car))
  session.add(vehicle)
  session.commit()
  return vehicle
  # this is the route for updating the whole existing car details
@app.put('/add_car/{car_id}')
def update_car(car_id:int,payload:UpdatedCarSchema) -> CarSchema:
  existed_car = session.query(Car).filter_by(number_plate=car_id).first()
  if existed_car is None:
    return {"error":"The car has not been found"}
  for key,value in payload.dict().items():
    setattr(existed_car,key,value)
  session.commit()
  return existed_car
# this is the route for deleting a car and its details
@app.delete('/car/delete{id}')
def delete_car(id:int) -> None:
  matatu = session.query(Car).filter_by(number_plate=id).first()
  session.delete(matatu)
  session.commit()
  return {"detail":f"Vehicle with the number_plate {id} has succesfully been deleted"}
# this is for updating specific details of the car
@app.patch('/cars/update/{id}')
def updating_car(id:int,payload:UpdatedCarSchema) -> CarSchema:
  updated_vehicle = session.query(Car).filter_by(number_plate=id).first()
  for key,value in payload.dict(exclude_unset=True).items():
    setattr(updated_vehicle,key,value)
  session.commit()
  return updated_vehicle
