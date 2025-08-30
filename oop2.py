import json
from os import makedirs
from os.path import *
import uuid

class Ride:
    #class variable (static variable)
    company_name = "GoRide"
    dir_name = "rides_data"

    #constructor
    def __init__(self, distance):
        self.distance = distance #instance variable
        self.base_fare = 2.0
        self.fare_multiplier = 1.0
        self._driver_rating = 4.8 #protected, convention(_var)
        self.__driver_phone = "012-3456789" #private, convention(__var)
        self.file_name = "ride_data.json"

    #instance method, need to put self as first param
    def calculate_fare(self):
        return self.distance * self.base_fare
    
    #getter
    def get_driver_rating(self):
        return self._driver_rating
    
    #setter
    def set_driver_rating(self, rating):
        if 1 <= rating <=5:
            self._driver_rating = rating
        else:
            raise ValueError("Rating must be between 1 to 5")

    def get_driver_phone(self):
        return self.__driver_phone
    
    def set_driver_phone(self, phone):
        if phone and len(phone) >= 10:
            self.__driver_phone = phone
        else:
            raise ValueError("Phone must be at least 10 characters")
        

    def to_dict(self):
        return {
            "distance": self.distance,
            "base_fare": self.base_fare,
            "fare_multiplier": self.fare_multiplier,
            "driver_rating": self.get_driver_rating(),
            "driver_phone" : self.get_driver_phone()
        }


    @classmethod
    def from_dict(cls, data):
        #static method, to create ride object, without initialize ride = Ride()
        ride = cls(data["distance"])
        ride.base_fare = data["base_fare"]
        ride.fare_multiplier = data["fare_multiplier"]
        ride.set_driver_rating(data["driver_rating"])
        ride.set_driver_phone(data["driver_phone"])
        return ride # !important
    
    def save_to_file(self):
        try:
            data = self.to_dict()
            file_path = join(dirname(abspath(__file__)), self.file_name)
            with open(file_path, "w") as file:
                json.dump(data, file, indent=2)

            print("Ride data saved")
        except Exception as e:
            print(f"Failed to save ride: {e}")


    def save_to_dir(self):
        try:
            target_dir = join(dirname(abspath(__file__)), self.dir_name)
            makedirs(target_dir, exist_ok=True)

            file_name = f"ride_{uuid.uuid4().hex}.json"
            file_path = join(target_dir, file_name)

            data = self.to_dict()
            data['class'] = self.__class__.__name__

            with open(file_path, "w") as file:
                json.dump(data, file, indent=2)
            
            print("ride saved successfully")
        except Exception as e:
            print(f"File save fail: {e}")

    @classmethod
    def load_all_from_dir(cls):
        try:
            target_dir = join(dirname(abspath(__file__)), cls.dir_name)
            if not exists(target_dir):
                return []
            entries = [f for f in os.listdir(target_dir) if f.endswitch(".json")]
            rides = []
            mapping = {
                "Ride" : Ride,
                "EconomicRide" : EconomicRide,
                "PremiumRide" : PremiumRide
            } 

            for en in entries:
                path = join(target_dir,en)
                try:
                    with open(path, "r") as file:
                        data = json.load(file)
                    cls_name = mapping[data['class']] if data['class'] in mapping else Ride
                    ride = cls_name.from_dict(data)
                    rides.append(ride)
                except Exception as e:
                    print(e)
                return rides
        except Exception as e:
            print(f"fail to load from dir {e}")
                


    def load_from_file(self):
        try:
            file_path = join(dirname(abspath(__file__)), self.file_name)
            with open(file_path, "r") as file:
                data = json.load(file)
            self.distance = data.get('distance', self.distance)
            #data.get() will not throw error when key not found
            #data.get(key, fallback_value)
            self.base_fare = data["base_fare"]
            self.fare_multiplier = data["fare_multiplier"]
            self.set_driver_rating(data["driver_rating"])
            self.set_driver_phone(data["driver_phone"])
        except FileNotFoundError as e:
            print("File not found")
        except Exception as e:
            print(f"Failed to load ride: {e}")


    @staticmethod
    def validate_distance(distance):
        return distance and distance > 0
    

    def __str__(self): #toString()
        return f"Distance: {self.distance}km, Fare: {self.calculate_fare()}km"
    
class PremiumRide(Ride): #inheritance, syntax Child(Parent)
    def __init__(self, distance):
        super().__init__(distance) #must call parent constructor
        self.fare_multiplier = 1.5
        self.include_wifi = True
        
    def calculate_fare(self): #method overriding
        return super().calculate_fare() * self.fare_multiplier
    
    def offer_snack(self):
        return "Snack Offered"
    
class EconomicRide(Ride):
    def __init__(self, distance):
        super().__init__(distance)
        self.fare_multiplier = 0.8

    def calculate_fare(self):
        return super().calculate_fare() * self.fare_multiplier

print(f"current __name__ value: {__name__}") #__main__

if(__name__ == "__main__"):
    ride = Ride(10) #! no new keyword
    print(f"static var: {Ride.company_name}")

    #! fake encapsulation!!!
    print(f"Protected: {ride._driver_rating}") #works!
    #! python mangling
    #_var becomes _ClassName_var
    print(f"Private phone: {ride._Ride__driver_phone}") #works!

    economic = EconomicRide(10)
    premium = PremiumRide(10)

    print(f"{economic}")
    print(f"{premium}")
    print(f"Snack: {premium.offer_snack()}")

    #ride.save_to_file()
    ride.save_to_dir()
    premium.save_to_dir()
    economic.save_to_dir()
    rides = Ride.load_all_from_dir()
    for r in rides:
        print(r)



    #ride.load_from_file()
    print(f"fromfile: {ride}")
