class Amplifier:
    def __init__(self):
        self.name = "Top-O-Line Amplifier"

    def on(self):
        print(self.name + " on")

    def set_dvd(self, dvd):
        print(self.name + " setting DVD player to Top-O-Line DVD Player")

    def set_surround_sound(self):
        print(self.name + " surround sound on (5 speakers, 1 subwoofer)")

    def set_volume(self, i):
        print(self.name + " setting volume to 5")

    def off(self):
        print(self.name + " off")
