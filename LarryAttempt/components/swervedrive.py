from wpilib import ADXRS450_Gyro
import constants

import math

import ctre
import wpimath.controller

class SwerveModule:
    """
    Create a swerve module. __init__ takes drive motor and turn motor (TalonFXs). The drive motor drives the module, and the turn motor turns it using a PID controller.
    """
    #static methods can be called as a class (SwerveModule.method()) or as an object (flmodule.method()) but cannot access attributes
    @staticmethod
    def sensorUnitsToDegrees(su):
        return su * (360/2048)
    
    @staticmethod
    def degreesToSensorUnits(deg):
        return deg * (2048/360)

    def __init__(self, driveMotor: ctre.TalonFX, turnMotor: ctre.TalonFX):

        self.driveMotor = driveMotor
        self.turnMotor = turnMotor
        self.pidController = wpimath.controller.PIDController(constants.kP, constants.kI, constants.kD)

        self.turnMotor.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, 10)

    def closestAngle(self, a, b):
        """
        Find the closest direction to go to get from angle a to angle b. Returns an angle in degrees.
        """
        #modulus is just so the angles are under 360. this is really b - a (difference between angles)
        direc = (b % 360) - (a % 360)
        #if distance is over 180 we can go the other way
        if abs(direc) > 180.0:
            #let's say the direc is 270. we take the inverse of 360 (taking the sign of our angle) 
            #and then add direc onto it to get our new angle
            direc = -(math.copysign(1, direc) * 360.0) + direc
        return direc

    def optimize(self, pointA, pointB):
        """
        Optimizes the route from pointA (angle in degrees) to pointB (also angle in degrees) so it is quickest. This way the motor spends the shortest time turning the wheel so we can get quick feedback from turning it.
        """
        #closest angle
        direc = self.closestAngle(pointA, pointB)
        #TODO further optimize angle 
        return direc

    def setDirection(self, angle):
        """
        Change the direction the module is facing. Takes angle argument (degrees).
        """
        ...

    def setSpeed(self, speed):
        """
        Change the speed of the module. speed argument should be between -1.0 (backward) and 1.0 (forward)
        """
        self.driveMotor.set(ctre.ControlMode.PercentOutput, speed)

class SwerveDrive:
    """
    Swerve drive component. Now we're gaming
    """
    FLModule: SwerveModule
    BLModule: SwerveModule
    FRModule: SwerveModule
    BRModule: SwerveModule
    gyro: ADXRS450_Gyro

    #TODO have values set here that can be changed in move and then passed to the motors in execute

    def move(self, leftX, leftY, rightX):
        """
        Move the swerve drive. This doesn't actually move anything, but it 
        """
        ...
    
    def execute(self):
        ...

