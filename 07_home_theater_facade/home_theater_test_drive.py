from home_theater_facade import HomeTheaterFacade
from amplifier import Amplifier
from tuner import Tuner
from dvd_player import DvdPlayer
from cd_player import CdPlayer
from projector import Projector
from screen import Screen
from theater_lights import TheaterLights
from popcorn_popper import PopcornPopper


if __name__ == "__main__":
        amp = Amplifier()
        tuner = Tuner()
        dvd = DvdPlayer()
        cd = CdPlayer()
        projector = Projector()
        screen = Screen()
        lights = TheaterLights()
        popper = PopcornPopper()

        homeTheater = HomeTheaterFacade(amp, tuner, dvd, cd, projector, screen, lights, popper)

        homeTheater.watch_movie("Xpto Movie")
        homeTheater.end_movie()
