class HomeTheaterFacade:
    def __init__(self, amp, tuner, dvd, cd, projector, screen, lights, popper):
        self._amp = amp
        self._tuner = tuner
        self._dvd = dvd
        self._cd = cd
        self._projector = projector
        self._screen = screen
        self._lights = lights
        self._popper = popper

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self._popper.on()
        self._popper.pop()
        self._lights.dim(10)
        self._screen.down()
        self._projector.on()
        self._projector.wide_screen_mode()
        self._amp.on()
        self._amp.set_dvd(self._dvd)
        self._amp.set_surround_sound()
        self._amp.set_volume(5)
        self._dvd.on()
        self._dvd.play(movie)

    def end_movie(self):
        print("Shutting movie theater down...")
        self._popper.off()
        self._lights.on()
        self._screen.up()
        self._projector.off()
        self._amp.off()
        self._dvd.stop()
        self._dvd.eject()
        self._dvd.off()
