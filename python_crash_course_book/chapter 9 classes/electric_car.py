class Car:
    """A simple attempt to represent a car."""

    def __init__ (self, model, manufacturer, year):
        """initialise attributes to describe a car"""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 34

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print statement showing car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add given amount to the odometer reading"""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75
        self.odometer_reading = 2000
        self.battery = Battery()

    def read_odometer(self):
        return super().read_odometer()
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This car doesn't need a gas tank!")

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size = 75):
        """Initialise the battery's attributes"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Prints statement describing the battery size."""
        print(f"This car has {self.battery_size} - kWh battery.")

my_petrol_car = Car("Honda", "Accord", 2012)
print(my_petrol_car.get_descriptive_name())
my_petrol_car.read_odometer()
print("\nUpdating odometer to 1000km...\n")
my_petrol_car.update_odometer(1000)
my_petrol_car.read_odometer()
my_petrol_car.increment_odometer(50), my_petrol_car.increment_odometer(50)
my_petrol_car.read_odometer()

my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.read_odometer()
my_tesla.fill_gas_tank()
my_tesla.increment_odometer(200)
my_tesla.read_odometer()
my_tesla.battery.describe_battery()

