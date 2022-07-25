from re import S
import magicbot
import ctre
import constants
import math

def deadband(x):
    return x if abs(x) > constants.deadband else 0

class SwerveModule:
    
    @staticmethod
    def sensorUnitsToDegrees(su: float) -> float:
        return su * (360/2048)
    
    @staticmethod
    def degreesToSensorUnits(deg: float) -> float:
        return deg * (2048/360)

    def __init__(self, driveMotorID: int, turnMotorID: int):
        
        self.driveMotor = ctre.TalonFX(driveMotorID)
        self.turnMotor = ctre.TalonFX(turnMotorID)        

    def setSpeed(self, magnitude):
        
        self.driveMotor.set(ctre.TalonFXControlMode.PercentOutput, magnitude)

    def setDirection(self, angle):

        self.turnMotor.set(ctre.TalonFXControlMode.Position, self.degreesToSensorUnits(angle))

class SwerveDrive:
    
    """
    Create stuff like motors, solenoids here
    """

    FRModule: SwerveModule
    FLModule: SwerveModule
    BLModule: SwerveModule
    BRModule: SwerveModule

    speeds = {"FR" : 0, "FL" : 0, "BL" : 0, "BR" : 0}
    angles = {"FR" : 0, "FL" : 0, "BL" : 0, "BR" : 0}

    def setup(self):
        """
        Setup things created in the beginning of the class.
        """
        self.modules = {"FR" : self.FRModule, "FL" : self.FLModule, "BL" : self.BLModule, "BR" : self.BRModule}

    def move(self, leftX, leftY, rightX, gyroAngle):
        """
        Set values to be used in execute here.
        """
        
        leftX = deadband(leftX)
        leftY = deadband(leftY)
        rightX = deadband(rightX)

        temp = leftY * math.cos(gyroAngle) + leftX * math.sin(gyroAngle)
        leftX = -leftY * math.sin(gyroAngle) + leftX * math.cos(gyroAngle)
        leftY = temp

        a = leftX - rightX * (constants.L / constants.R)
        b = leftX + rightX * (constants.L / constants.R)
        c = leftY - rightX * (constants.W / constants.R)
        d = leftY + rightX * (constants.W / constants.R)

        self.speeds["FR"] = (b ** 2 + c ** 2) ** 0.5
        self.speeds["FL"] = (b ** 2 + d ** 2) ** 0.5
        self.speeds["BL"] = (a ** 2 + d ** 2) ** 0.5
        self.speeds["BR"] = (a ** 2 + c ** 2) ** 0.5

        self.angles["FR"] = (math.degrees(math.atan2(b, c)) + 360) % 360
        self.angles["FL"] = (math.degrees(math.atan2(b, d)) + 360) % 360
        self.angles["BL"] = (math.degrees(math.atan2(a, d)) + 360) % 360
        self.angles["BR"] = (math.degrees(math.atan2(a, c)) + 360) % 360

        #optimize speeds
        maxi = max(self.speeds.values())

        if maxi >= 1:
            for key in self.speeds.keys():
                self.speeds[key] /= maxi

        #optimize angles
        for key in self.modules.keys():
            module = self.modules[key]
            a = SwerveModule.sensorUnitsToDegrees(module.turnMotor.getSelectedSensorPosition())
            b = self.angles[key]
        
            dir = (b % 360.0) - (a % 360.0)

            if (abs(dir) > 180.0):
            
                dir = -(math.copysign(1, dir) * 360.0) + dir

            self.angles[key] = (dir + 360) % 360

    def execute(self):
        """
        Called every loop.
        """

        for key in self.modules.keys():
            self.modules[key].setSpeed(self.speeds[key])
            self.modules[key].setDirection(self.angles[key])