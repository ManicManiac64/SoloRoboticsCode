import wpilib

#THIS IS WOEFULLY BAD

class Launcher:
    """
    Launcher component. It goes up. Then it goes down. Launches balls into the lower hub.
    """

    launcherSolenoid: wpilib.DoubleSolenoid
    
    isDown = True

    def toggle(self):
        """
        Toggle launcher solenoid.
        """
        self.isDown = not self.isDown

    def execute(self):
        ...

