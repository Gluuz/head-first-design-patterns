from observer import Observer
from display_element import DisplayElement


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.temperature = 0.0
        self.humidity = 0.0
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print("Current conditions: %.1fF degrees and %.1f%% humidity" % (self.temperature, self.humidity))
