#Swerve Drive Component
import wpilib
import wpimath.geometry
import wpimath.kinematics
import wpimath.controller
import ctre

import constants

#swerve module class
class SwerveModule:
    def __init__(self, driveMotor: ctre.WPI_TalonFX, rotateMotor: ctre.WPI_TalonFX):
        
        self.driveMotor = driveMotor
        self.rotateMotor = rotateMotor
        self.pidController = wpimath.controller.PIDController(constants.kP, constants.kI, constants.kD)

class SwerveDrive:

    FLDrive: ctre.WPI_TalonFX
    FLSteer: ctre.WPI_TalonFX
    FRDrive: ctre.WPI_TalonFX
    FRSteer: ctre.WPI_TalonFX
    BLDrive: ctre.WPI_TalonFX
    BLSteer: ctre.WPI_TalonFX
    BRDrive: ctre.WPI_TalonFX
    BRSteer: ctre.WPI_TalonFX

    def setup(self):
        self.moduleList = [
            SwerveModule(FLDrive, FLSteer),
            SwerveModule(FRDrive, FRSteer),
            SwerveModule(BLDrive, BLSteer),
            SwerveModule(BRDrive, BRSteer)
        ]