# ctre is used to control CTRE-branded stuff, like the TalonFX (TM)
# constants of course stores all the constants we use (stuff that doesn't change, stays constant)
# math does math stuff, like atan (arctan if you're a mathematician)

import wpilib
import wpimath.controller
import ctre
import constants
import math

# deadbands basically create a range around 0 and if a value is in that range we'll change the value to 0
# for example we could have a deadband between -0.05 and 0.05 and say if a value is in that range, we'll just round it to 0
# this helps get rid of tiny movements

def deadband(x):
    return x if abs(x) > constants.deadband else 0

# swerve module class

class SwerveModule:
    
    @staticmethod
    def sensorUnitsToDegrees(su: float) -> float:
        IAmCoolerThanCaden = (su * (360/2048))
        return (IAmCoolerThanCaden / constants.STEERINGRATIO) % 360
    
    @staticmethod
    def degreesToSensorUnits(deg: float) -> float:
        IAmCoolerThanNathan =  (deg * (2048/360))
        return (IAmCoolerThanNathan * constants.STEERINGRATIO) % 2048

    def __init__(self, driveMotorID: int, turnMotorID: int):
        
        self.driveMotor = ctre.TalonFX(driveMotorID)
        self.turnMotor = ctre.TalonFX(turnMotorID)
        
        self.turnMotor.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, 10)

        self.turnMotor.config_kF(0, constants.F, 10)

        self.turnMotor.config_kP(0, constants.P, 10)

        self.turnMotor.config_kI(0, constants.I, 10)

        self.turnMotor.config_kD(0, constants.D, 10)

        self.turnMotor.config_IntegralZone(0, constants.IZONE, 10)

        # MOTOR CONFIG
        self.turnMotor.configNominalOutputForward(0, 10)
        self.turnMotor.configNominalOutputReverse(0, 10)

        self.turnMotor.configPeakOutputForward(1, 10)
        self.turnMotor.configPeakOutputReverse(-1, 10)

        self.turnMotor.selectProfileSlot(0, 0)

        self.turnMotor.configMotionCruiseVelocity(constants.CRUISEVEL, 10)
        self.turnMotor.configMotionAcceleration(constants.CRUISEACCEL, 10)

        self.turnMotor.setNeutralMode(ctre.NeutralMode.Brake)

        self.turnMotor.setSelectedSensorPosition(0.0, 0, 10)
        
        self.reversedAngle = False

    def setSpeed(self, magnitude):
        
        self.driveMotor.set(ctre.TalonFXControlMode.PercentOutput, magnitude * 0.2)

    def setDirection(self, angle):
        
        self.turnMotor.set(ctre.TalonFXControlMode.MotionMagic, self.degreesToSensorUnits(angle))

class SwerveDrive:
    
    """
    Create stuff like motors, solenoids here
    """

    FRModule: SwerveModule
    FLModule: SwerveModule
    BLModule: SwerveModule
    BRModule: SwerveModule

    def setup(self):
        """
        Setup things created in the beginning of the class.
        """
        self.modules = {"FR" : self.FRModule, "FL" : self.FLModule, "BL" : self.BLModule, "BR" : self.BRModule}
        self.speeds = {"FR" : 0, "FL" : 0, "BL" : 0, "BR" : 0}
        self.angles = {"FR" : 0, "FL" : 0, "BL" : 0, "BR" : 0}

    def move(self, leftX, leftY, rightX, gyroAngle):
        """
        Set values to be used in execute here.
        """
        
        leftX = deadband(leftX)
        leftY = deadband(leftY)
        rightX = deadband(rightX)

        # temp = leftY * math.cos(gyroAngle) + leftX * math.sin(gyroAngle)
        # leftX = -leftY * math.sin(gyroAngle) + leftX * math.cos(gyroAngle)
        # leftY = temp

        a = leftX - rightX * (constants.L / constants.R)
        b = leftX + rightX * (constants.L / constants.R)
        c = leftY - rightX * (constants.W / constants.R)
        d = leftY + rightX * (constants.W / constants.R)

        self.speeds["FR"] = (b ** 2 + c ** 2) ** 0.5
        self.speeds["FL"] = (b ** 2 + d ** 2) ** 0.5
        self.speeds["BL"] = (a ** 2 + d ** 2) ** 0.5
        self.speeds["BR"] = (a ** 2 + c ** 2) ** 0.5
        
        #modulo 360 changes negative angles to positive
        self.angles["FR"] = (math.degrees(math.atan2(b, c))) % 360
        self.angles["FL"] = (math.degrees(math.atan2(b, d))) % 360
        self.angles["BL"] = (math.degrees(math.atan2(a, d))) % 360
        self.angles["BR"] = (math.degrees(math.atan2(a, c))) % 360

        #optimize speeds
        maxi = max(self.speeds.values())

        if maxi >= 1:
            for key in self.speeds.keys():
                self.speeds[key] /= maxi

        #optimize angles
        #the key to this is finding 4 differences, going clockwise or counter, and forward or reversing the wheel's speed
        for key in self.modules.keys():
            module = self.modules[key]
            
            #again modulo 360 changes negative angles to positive (and positive to positive, of course)
            a = SwerveModule.sensorUnitsToDegrees(module.turnMotor.getSelectedSensorPosition())
            bForward = self.angles[key]
            
            #clockwise and forward distance
            cloFor = bForward - a if a <= bForward else (360 - a) + bForward
            #counter and forward distance
            couFor = a - bForward if bForward <= a else (360 - bForward) + a
            
            #reverse angle
            bReverse = (bForward + 180) % 360
            #clockwise and reverse distance
            cloRev = bReverse - a if a <= bReverse else (360 - a) + bReverse
            #counter and reverse distance
            couRev = a - bReverse if bReverse <= a else (360 - bReverse) + a
            
            #find minimum
            minimum = min(cloFor, couFor, cloRev, couRev)
            
            if minimum == cloFor:
                self.angles[key] = bForward
                self.speeds[key] *= 1
                module.reversedAngle = False
                
            elif minimum == couFor:
                self.angles[key] = bForward
                self.speeds[key] *= 1
                module.reversedAngle = True
                
            elif minimum == cloRev:
                self.angles[key] = bReverse
                self.speeds[key] *= -1
                module.reversedAngle = False
                
            elif minimum == couRev:
                self.angles[key] = bReverse
                self.speeds[key] *= -1
                module.reversedAngle = True
                
    def execute(self):
        """
        Called every loop.
        """
        
        for key in self.modules.keys():
            self.modules[key].setSpeed(self.speeds[key])
            self.modules[key].setDirection(self.angles[key])

            wpilib.SmartDashboard.putNumber(f"Angles/{key}", SwerveModule.degreesToSensorUnits(self.angles[key]))
            wpilib.SmartDashboard.putNumber(f"Actual/{key}", self.modules[key].turnMotor.getSelectedSensorPosition())