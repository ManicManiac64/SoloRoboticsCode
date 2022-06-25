import magicbot
import ctre

from components.swervedrive import SwerveDrive

class Larry(magicbot.MagicRobot):
    
    self.drivetrain: SwerveDrive

    def createObjects(self):
        self.FLDrive = ctre.WPI_TalonFX(0)
        self.FLSteer = ctre.WPI_TalonFX(4)
        self.FRDrive = ctre.WPI_TalonFX(2)
        self.FRSteer = ctre.WPI_TalonFX(6)
        self.BLDrive = ctre.WPI_TalonFX(1)
        self.BLSteer = ctre.WPI_TalonFX(5)
        self.BRDrive = ctre.WPI_TalonFX(3)
        self.BRSteer = ctre.WPI_TalonFX(7)