import math

import magicbot
from wpilib import ADXRS450_Gyro
import ctre
import constants

def deadband(x):
    return x if abs(x) > constants.kdeadband else 0

class SwerveModule:
    """
    Create a swerve module. __init__ takes drive motor and turn motor (TalonFXs). The drive motor drives the module, and the turn motor turns it using a PID controller.
    """
    #static methods can be called as a class (SwerveModule.method()) or as an object (flmodule.method()) but cannot access attributes
    
    @staticmethod
    def joystickToDegrees(x: float, y: float, rcw: float) -> float:
        initialValue = math.degrees(math.atan2(x, -y))
        #if x is negative (left) add 360 to the initial value
        if math.copysign(1, x) == -1:
            return initialValue + 360.0
        #if value is 360 make it 0, otherwise just return the value
        return initialValue if initialValue != 360.0 else 0.0
    
    
    @staticmethod
    def sensorUnitsToDegrees(su: float) -> float:
        return su * (360/2048)
    
    @staticmethod
    def degreesToSensorUnits(deg: float) -> float:
        return deg * (2048/360)

    @staticmethod
    def closestAngle(a: float, b: float) -> float:
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

    def __init__(self, driveMotor: ctre.TalonFX, turnMotor: ctre.TalonFX):

        self.driveMotor = driveMotor
        self.turnMotor = turnMotor

    def setDirection(self, angle: float):
        """
        Change the direction the module is facing. Takes angle argument (degrees).
        """
        
        self.turnMotor.set(ctre.ControlMode.MotionMagic, self.degreesToSensorUnits(angle))
        
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

    modules = {"FL" : FLModule, "BL" : BLModule, "FR" : FRModule, "BR" : BRModule}
    angles = {"FL" : 0, "BL" : 0, "FR" : 0, "BR" : 0}
    speeds = magicbot.will_reset_to({"FL" : 0, "BL" : 0, "FR" : 0, "BR" : 0})
    
    def setup(self):
        self.gyro.calibrate()

    def move(self, leftX, leftY, rightX):
        """
        Move the swerve drive. This doesn't actually move anything, but it 
        """
        #rotation is not complete yet so we'll leave this as zero for now
        rightX = 0

        #deadband values
        leftX = deadband(leftX)
        leftY = deadband(leftY)
        rightX = deadband(rightX)

        #iterate through keys in dict (we can access each module this way)
        for key in self.modules.keys():
            
            #the module is the value in self.modules corresponding to the key
            module = self.modules[key]
            module: SwerveModule #just for that sweet syntax highlighting
            
            #requestedAngle is the joystickInput given converted to degrees
            requestedAngle = SwerveModule.joystickToDegrees(leftX, leftY, rightX)
            
            """
            to find magnitude use the pythagorean theorem. imagine a triangle
            on the joystick with the points not opposite the hypotenuse at (0, 0)
            and (leftX, leftY). we can find the hypotenuse (or the magnitude here)
            by using the pythagorean theorem (a^2 + b^2 = c^2, or sqrt(a^2 + b^2) = c)
            """

            magnitude = math.sqrt((leftX ** 2 + leftY ** 2))

            #if magnitude is over 1 scale it down to 1
            if magnitude >= 1.0:
                magnitude = 1.0
            
            #the current angle is the current sensor units converted to degrees
            currentAngle = SwerveModule.sensorUnitsToDegrees(module.turnMotor.getSelectedSensorPosition())
            
            #the opposite angle is the angle opposite the requested angle on the unit circle (45 maps to 225 and vice versa for example, as well as 270 and 90)
            oppositeAngle = abs(requestedAngle) - 180.0 if abs(requestedAngle) >= 180.0 else abs(requestedAngle) + 180.0

            #do things if magnitude isn't zero (this way angles don't reset to zero when we let go of the joystick)
            if magnitude != 0.0:
                #if the difference between currentAngle and requestedAngle is faster than the opposite angle
                if abs(currentAngle - requestedAngle) <= abs(currentAngle - oppositeAngle):
                    #use the requestedAngle and positive magnitude
                    self.angles[key] = requestedAngle
                    self.speeds[key] = magnitude
                #otherwise
                else:
                    #use the oppositeAngle (it's faster) and negative magnitude.
                    """
                    We can turn to 270 degrees, or we can turn to 90 degrees. 
                    The wheel, however, will be facing the other direction, so we reverse 
                    the magnitude.
                    """
                    self.angles[key] = oppositeAngle
                    self.speeds[key] = -magnitude

    #execute function is called automatically                
    def execute(self):
        #just like before, iterate through the keys
        for key in self.modules.keys():
            
            #module is the key in self.modules ("FL", "FR", etc.)
            module = self.modules[key]
            module: SwerveModule #sweet sweet syntax highlighting

            #set the direction by converting the angle to sensor units and then multiplying by the ratio of the gears in the module.
            module.setDirection(SwerveModule.degreesToSensorUnits(self.angles[key]) * constants.kgearRatio)
            #set speed
            module.setSpeed(self.speeds[key])

