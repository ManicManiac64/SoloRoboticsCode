import wpilib
import ctre
import magicbot

class SwerveModule:

    def __init__(self, driveID, turnID, encoderID):

        self.driveMotor = ctre.TalonFX(driveID)
        self.turnMotor = ctre.TalonFX(turnID)
        self.encoder = ctre.CANCoder(encoderID)

class SwerveDrive:

    pass