import constants

import ctre
import wpimath.controller

class SwerveModule:
    """
    Create a swerve module. __init__ takes drive motor and turn motor (TalonFXs). The drive motor drives the module, and the turn motor turns it using a PID controller.
    """
    def __init__(self, driveMotor: ctre.TalonFX, turnMotor: ctre.TalonFX):

        self.driveMotor = driveMotor
        self.turnMotor = turnMotor
        self.pidController = wpimath.controller.PIDController(constants.kP, constants.kI, constants.kD)

        self.turnMotor.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, 10)

    def optimize(self, pointA, pointB):
        """
        Optimizes the route from pointA (angle in degrees) to pointB (also angle in degrees) so it is quickest. This way the motor spends the shortest time turning the wheel so we can get quick feedback from turning it.
        """
        ...

    def setDirection(self, angle):
        """
        Change the direction the module is facing. Takes angle argument (degrees).
        """
        ...
    
    def setSpeed(self, speed):
        """
        Change the speed of the module. speed argument should be between -1.0 (backward) and 1.0 (forward)
        """
        self.driveMotor.set(speed)

class SwerveDrive:
    """
    Swerve drive component. Now we're gaming
    """