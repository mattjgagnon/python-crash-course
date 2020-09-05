from car import Car
from battery import Battery

class ElectricCar(Car):
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize aspects of a car, specific to electric vehicles."""
        super().__init__(make, model, year)
        self.battery = Battery()
