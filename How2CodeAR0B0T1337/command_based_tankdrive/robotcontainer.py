import wpilib
import commands2

import constants

from subsystems.drivetrain import Drivetrain
from commands.joystick_drive import JoystickDrive

class RobotContainer:
    def __init__(self):

        self.driverController = wpilib.XboxController(constants.kdriverControllerPort)
        
        self.drive = Drivetrain()

        self.drive.setDefaultCommand(JoystickDrive(self.drive, lambda: self.driverController.getLeftY(), lambda: self.driverController.getRightY()))