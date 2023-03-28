from light import Light
from light_on_command import LightOnCommand
from simple_remote_control import SimpleRemoteControl


class RemoteControlTest:
    def main(self):
        # the remote is our Invoker; it will be passed a command
        # object that can be used to make requests
        remote = SimpleRemoteControl()
        # now we create a Light object, this will be the Receiver of the request
        light = Light()
        # create a command and pass it to the Receiver
        light_on = LightOnCommand(light)

        # pass the command to the Invoker
        remote.set_command(light_on)
        # we simulate the button being pressed
        remote.button_was_pressed()



if __name__ == "__main__":
    RemoteControlTest().main()

