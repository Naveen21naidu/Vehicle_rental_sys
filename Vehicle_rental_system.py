class Vehicle:
    def __init__(self,name,brand,rent_per_day):
        self.name=name
        self.brand=brand
        self.rent_per_day=rent_per_day 
        self.__available=True  

    def mark_rented(self):
        if not self.__available:
            return False 
        self.__available=False
        return True

    def mark_available(self):
        self.__available=True 

    def is_available(self):
        return self.__available
    
    def calculate_rent(self,days):
        return self.rent_per_day*days
    
    def display(self):
        return f'{self.name}-{self.brand}:Rent {self.rent_per_day}/day'

class Car(Vehicle):

    def __init__(self,name,brand,rent_per_day,seats,fuel_type):
        super().__init__(name,brand,rent_per_day)
        self.seats=seats
        self.fuel_type=fuel_type 

    def calculate_rent(self, days):
        extra=250
        if self.seats>4:
            extra=350
        return super().calculate_rent(days)+extra 
class Bike(Vehicle):
    def __init__(self, name, brand, rent_per_day,engine_cc):
        super().__init__(name, brand, rent_per_day)
        self.engine_cc=engine_cc 

    #no need to override as there is no change in method 
    # def calculate_rent(self, days):
    #     return super().calculate_rent(days) 

class Customer:
    def __init__(self,name,phno):
        self.name=name
        self.phno=phno 
        self.rented_vehicle=None

    def rent_vehicle(self,vehicle,days):
        if vehicle is None:
            return 'Vehicle not found'
        
        if self.rented_vehicle is not None:
            return 'Already rented'
        
        if vehicle.is_available():
            vehicle.mark_rented()
            rent=vehicle.calculate_rent(days)
            self.rented_vehicle=vehicle 
            return f"Rented {vehicle.name}-{vehicle.brand} for ₹{rent}"
        return "Not Available"

    def return_vehicle(self):
        if self.rented_vehicle is None:
            return 'No Vehicle to return'
        self.rented_vehicle.mark_available()
        returned_name=self.rented_vehicle.name 
        self.rented_vehicle=None 
        return f'{returned_name} returend successfully'
    
class RentalSystem:
    def __init__(self):
        self.vehicles=[]

    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)

    def show_available_vehicles(self):
        available=[]
        for v in self.vehicles:
            if v.is_available():
                available.append(v.display())
        return available 
    
    def find_available_vehicle(self,name):
        for v in self.vehicles:
            if v.name.lower()==name.lower() and v.is_available():
                return v
        return None 


if __name__ == "__main__":

    system = RentalSystem()

    # Predefined vehicles
    system.add_vehicle(Car("Car", "Honda", 2000, 5, "Petrol"))
    system.add_vehicle(Car("Car", "Toyota", 2200, 7, "Diesel"))
    system.add_vehicle(Bike("Bike", "Yamaha", 800, 150))
    system.add_vehicle(Bike("Bike", "RoyalEnfield", 1200, 350))

    print("Welcome to Vehicle Rental System")

    name = input("Enter your name: ")
    phno = input("Enter phone number: ")

    customer = Customer(name, phno)

    while True:
        print("\n1. Show Available Vehicles")
        print("2. Rent Vehicle")
        print("3. Return Vehicle")
        print("4. Exit")

        choice = input("Enter choice: ")

        #Show vehicles
        if choice == '1':
            available = []
            for i, v in enumerate(system.vehicles):
                if v.is_available():
                    print(f"{i+1}. {v.display()}")
                    available.append(v)

            if not available:
                print("No vehicles available")

        #Rent vehicles
        elif choice == '2':
            available = []
            for i, v in enumerate(system.vehicles):
                if v.is_available():
                    print(f"{i+1}. {v.display()}")
                    available.append((i, v))

            if not available:
                print("No vehicles available")
                continue

            try:
                index = int(input("Select vehicle number: ")) - 1
                days = int(input("Enter number of days: "))

                if index < 0 or index >= len(system.vehicles):
                    print("Invalid selection")
                    continue

                vehicle = system.vehicles[index]

                if not vehicle.is_available():
                    print("Vehicle already rented")
                    continue

                result = customer.rent_vehicle(vehicle, days)
                #print(f"Rented {vehicle.name}-{vehicle.brand} for ₹{result}")
                print(result)

            except ValueError:
                print("Invalid input")

        #Return vehicle
        elif choice == '3':
            print(customer.return_vehicle())

        #Exit
        elif choice == '4':
            print("Thank you for using system")
            break

        else:
            print("Invalid choice")