import wpilib
import wpimath.controller
import ctre
import magicbot

class SwerveModule:
    #__init__ the module
    def __init__(self, driveMotor, rotationMotor):
        #init drivemotors, rotationmotors, the amount for driving and amount for rotating
        self.driveMotor = driveMotor
        self.rotationMotor = rotationMotor
        self.PIDController = wpimath.controller.PIDController(0.5, 0.0, 0.0) #Proportional-Integral-Derivative
        self.driveAmount = 0
        self.rotationAmount = 0
    def move(self, driveAm, rotationAm):
        #driveAm is just the amount for driving
        #rotationAm is the target angle we want to get to
        pass

    
