import wpilib
import ctre
import commands2

import constants

class Drivetrain(commands2.SubsystemBase):
    
    def __init__(self):
        
        super().__init__()

        self.FLMotor = ctre.TalonFX(constants.kFL)
        self.BLMotor = ctre.TalonFX(constants.kBL)
        self.FRMotor = ctre.TalonFX(constants.kFR)
        self.BRMotor = ctre.TalonFX(constants.kBR)

        self.BLMotor.follow(self.FLMotor)
        self.BRMotor.follow(self.FRMotor)

        self.FLMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.BLMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.FRMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.BRMotor.setNeutralMode(ctre.NeutralMode.Brake)

        self.FRMotor.setInverted(True)
        self.BRMotor.setInverted(True)

    def userDrive(self, leftY: float, rightY: float):
        
        self.FLMotor.set(ctre.ControlMode.PercentOutput, -leftY)
        self.FRMotor.set(ctre.ControlMode.PercentOutput, -rightY)