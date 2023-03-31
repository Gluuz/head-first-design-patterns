class DvdPlayer:
    def __init__(self):
        self.name = "Top-O-Line DVD Player"
        self.movie_on_air = ""

    def on(self):
        print(self.name + " on")

    def play(self, movie):
        print(self.name + " playing " + movie)
        self.movie_on_air = movie

    def stop(self):
        print(self.name + " stopped " + self.movie_on_air)
        self.movie_on_air = ""

    def eject(self):
        print(self.name + " eject")

    def off(self):
        print(self.name + " off")
