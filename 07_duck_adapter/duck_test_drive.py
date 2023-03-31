from mallard_duck import MallardDuck
from wild_turkey import WildTurkey
from turkey_adapter import TurkeyAdapter


def test_duck(duck):
    duck.quack()
    duck.fly()


if __name__ == "__main__":
    duck = MallardDuck()
    turkey = WildTurkey()

    # wrap the turkey in a TurkeyAdapter which makes it look like a Duck
    turkey_adapter = TurkeyAdapter(turkey)

    # let's test the Turkey
    print("The Turkey says...")
    turkey.gobble()
    turkey.fly()

    # test the duck
    print("\nThe Duck says...")
    test_duck(duck)

    # the big test: we try to pass off the turkey as a duck
    print("\nThe TurkeysAdapter says...")
    test_duck(turkey_adapter)
