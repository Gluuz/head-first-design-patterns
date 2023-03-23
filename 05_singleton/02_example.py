# In this example, the Singleton class has a private inner class called
# __Singleton, which is responsible for creating the single instance of the class.
# The private static variable __instance stores this single instance.
# The __init__ method is responsible for creating the single instance of
# the class if it does not exist yet. The get_instance method is responsible
# for returning the existing instance, or creating a new one if it does not exist yet.

class Singleton:
    class __Singleton:
        def __init__(self):
            self.value = None

    __instance = None  # private static variable that stores the single instance

    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = Singleton.__Singleton()

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance
