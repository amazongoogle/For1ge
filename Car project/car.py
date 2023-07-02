class Serviceable:
    def needs_service(self):
        raise NotImplementedError("Subclasses must implement needs_service method.")


class Engine(Serviceable):
    def __init__(self, fuel_level):
        self.fuel_level = fuel_level

    def needs_service(self):
        return self.fuel_level < 10


class Battery(Serviceable):
    def __init__(self, charge_level):
        self.charge_level = charge_level

    def needs_service(self):
        return self.charge_level < 20


class Car:
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()


# Create instances of Engine and Battery
engine = Engine(5)  # Fuel level: 5
battery = Battery(15)  # Charge level: 15

# Create a Car instance
car = Car(engine, battery)

# Check if the car needs service
if car.needs_service():
    print("The car needs service.")
else:
    print("The car does not need service.")

