from sqlalchemy import String,Column,Integer,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
Base = declarative_base()
# this is a class called Car
class Car(Base):
  # defining the table_name called car
  __tablename__='car'
  number_plate = Column(Integer,primary_key=True)
  vehicle_name = Column(String(50),nullable=False)
  plate_name = Column(String(50),nullable=False)
  conductor = Column(String(50),nullable=False)
  driver = Column(String(50),nullable=False)
  age = Column(Integer,nullable=False)
  route = Column(String(50),nullable=False)
  # creating the database engine and the tables
engine = create_engine('sqlite:///motors.db')
Base.metadata.create_all(engine)
  
# creating sample cars objects that will appear on the motors database
Session = sessionmaker(bind=engine)
session = Session()

car1 = Car(
    number_plate=1655,
    vehicle_name="Mermaid",
    plate_name="KCD",
    conductor="Alex Murithii",
    driver="Kimatus Kagwe",
    age=6,
    route="Roysambu_to_CBD"
)

car2 = Car(
    number_plate=7654,
    vehicle_name="Shamiri",
    plate_name="KBB",
    conductor="Alice Njuguna",
    driver="Bob Mwendwa",
    age=4,
    route="Kitusuru_to_Limuru"
)
car3 = Car(
    number_plate=7777,
    vehicle_name="Shoes",
    plate_name="KCC",
    conductor="Bien Marina",
    driver="Lexy Zamilla",
    age=6,
    route="Thika_to_Limuru"
)
car4 = Car(
    number_plate=2400,
    vehicle_name="Africa",
    plate_name="KBX",
    conductor="Ali Joho",
    driver="William Ruto",
    age=10,
    route="Kawangware_to_CBD"
)
car5 = Car(
    number_plate=6789,
    vehicle_name="Sole",
    plate_name="KDS",
    conductor="Jose Ron",
    driver="Pedro William",
    age=3,
    route="Machakos_to_CBD"
)
car6 = Car(
    number_plate=6666,
    vehicle_name="Voice",
    plate_name="KBP",
    conductor="Kingston Odinga",
    driver="Paul Mwendwa",
    age=5,
    route="Kasarani_to_ThikaTown"
)
car7 = Car(
    number_plate=7008,
    vehicle_name="Lopha",
    plate_name="KDH",
    conductor="Isaac Ngeno",
    driver="Brian Kamatu",
    age=6,
    route="Makongeni_to_Kaberia"
)
car8 = Car(
    number_plate=9000,
    vehicle_name="Trans",
    plate_name="KBI",
    conductor="Wamvii Wahu",
    driver="Lilian Kanini",
    age=9,
    route="Langata_to_Eastleigh"
)
# adding the cars to the session and commiting them
# session.add(car1)
# session.add(car2)
# session.add(car3)
# session.add(car4)
# session.add(car5)
# session.add(car6)
# session.add(car7)
# session.add(car8)

# session.commit()
  
