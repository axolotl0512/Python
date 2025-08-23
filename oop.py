import json
from os.path import join, dirname, abspath

class Ride:
    #class variable ( static variable )
    company_name = "GoRide"

    #constructor
    def __init__(self, distance):
        self.distance = distance #instance variable
        self.base_fare = 2.0
        self.fare_multiplier = 1.0
        self._driver_rating = 4.8 #protected use 1 _
        self.__driver_phone = "0123456798" #private, use 2 _
        self.file_name = "ride_data.json"

    def calculate_fare(self):
         return self.distance * self.base_fare
    
    #getter
    def get_driver_rating(self):
         return self._driver_rating
    
    #setter
    def set_driver_rating(self, rating):
         if 1<= rating <= 5:
            self._driver_rating = rating
         else:
              raise ValueError("Rating must be between 1-5")

    def get_driver_phone(self):
         return self.__driver_phone
    
    def set_driver_phone(self,phone):
         if phone and len(phone)>= 10:
            self.__driver_phone = phone

         else:
              raise ValueError("Phone must be at least 10 character")

    def to_dict(self):
         return{
              "distance": self.distance,
              "base_fare": self.base_fare,
              "fare_multiplier": self.fare_multiplier,
              "driver_rating": self.get_driver_rating(),
              "driver_phone": self.get_driver_phone()
         }
    
    #classmethod
    def from_dict(cls, data):
         #static method, to create ride object, without initialize ride = Ride()

         ride = cls(data["distance"])
         ride.base_fare= data["base_fare"]
         ride.fare_multiplier = data["fare_multiplier"]
         ride.set_driver_rating(data["driver_rating"])
         ride.set_driver_phone(data["driver_phone"])
         return ride #important
    
    def save_to_file(self):
         try:
              data= self.to_dict()
              file_path = join(dirname(abspath(__file__)), self.file_name)
              with open(file_path, "w") as file:
                   json.dump(data, file, indent = 2)

              print("Ride data saved")
         except Exception as e:
              print(f"Failed to save ride : {e}")

    def load_from_file(self):
         try:
              file_path = join(dirname(abspath(__file__)), self.file_name)
              with open(file_path, "r") as file:
                   data = json.load(file)

              #data.get() will not throw error when key not found
              # data.get(key, fallback(value))
              self.distance =  data["distance"]
              self.base_fare = data["base_fare"]
              self.fare_multiplier = data["fare_multiplier"]
              self.set_driver_rating(data["driver_rating"])
              self.set_driver_phone(data["driver_phone"])
         except FileNotFoundError as e:
              print("File not found")
         except Exception as e:
              print(f"Failed to load file {e}")


    #staticmethod
    def validate_distance(distance):
         return distance and distance > 0
              
    
    def __str__(self):
         return f"Distance: {self.distance}km, Fare: {self.calculate_fare()}"
    
class PremiumRide(Ride): #inheritance, syntax Child(Parent)
     def __init__(self, distance):
          super().__init__(distance)
          self.fare_multiplier = 1.5
          self.include_wifi = True

     def calculate_fare(self):
          return super().calculate_fare() * self.fare_multiplier
     
     def offer_snack(self):
          return "SNcAk ofFerEd"
     
class EconomicRide(Ride):
     def __init__(self, distance):
          super().__init__(distance)
          self.fare_multiplier = 0.8

     def calculate_fare(self):
          return super().calculate_fare() * self.fare_multiplier
        
        
print(f"current __name__ value: {__name__}") #__main__

if(__name__ =="__main__"):
      ride = Ride(10) #! no new keyword
      print(f"static var: {Ride.company_name}")

      #! fake encapsulation
      print(f"protected: {ride._driver_rating}") #works! ??
      #! python mangling
      print (f"Private Phone: {ride._Ride__driver_phone}") #works !

      economic = EconomicRide(10)
      premium = PremiumRide(10)

      print(f"{economic}")
      print(f"{premium}")
      print(f"Snack: {premium.offer_snack()}")

      #ride.save_to_file()
      ride.load_from_file()
      print(f"fromfile:{ride}")

