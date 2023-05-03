import commands2, wpilib, constants

from subsystems.drivetrain import Drivetrain
from commands.joystickDrive import JoystickDrive

class RobotContainer:

    def __init__(self):

        self.driverController = wpilib.XboxController(constants.DRIVERCONTROLLERPORT)
        self.drivetrain = Drivetrain()
        self.sendableChooser = wpilib.SendableChooser()

        self.drivetrain.setDefaultCommand(JoystickDrive(self.drivetrain, lambda: self.driverController.getLeftY(), lambda: self.driverController.getRightY()))
        

    def getAutonomousCommand(self):

        return self.sendableChooser.getSelected()