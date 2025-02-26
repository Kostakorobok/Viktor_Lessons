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
        
    
my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(35)
my_new_car.read_odometer()

my_used_car = Car("subaru", "outback", 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
