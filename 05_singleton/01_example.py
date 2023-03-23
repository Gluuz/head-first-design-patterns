# In this example, the Singleton class has a private static
# variable called __instance, which stores the single instance
# of the class. The __init__ method is responsible for ensuring
# that only one instance of the class is created and stored in
# this static variable. The get_instance method is responsible
# for returning the existing instance, or creating a new one if it does not exist yet.

class Singleton:
    __instance = None  # private static variable that stores the single instance

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("An instance of this class already exists")
        else:
            Singleton.__instance = self

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance


