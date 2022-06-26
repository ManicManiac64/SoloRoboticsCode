import wpilib
import magicbot
import ctre
import components.swervedrive
import constants

class Larry(magicbot.MagicRobot):

    #beans. swervedrive is a SwerveDrive, how cool is that woah. i mean not that cool but-
    swervedrive: components.swervedrive.SwerveDrive

    #Create objects. Do it now.
    def createObjects(self):
        #modules (the order is driveMotor, then turnMotor)
        self.FLModule = components.swervedrive.SwerveModule(
            ctre.TalonFX(constants.kFLD), ctre.TalonFX(constants.kFLT)
            )
        self.BLModule = components.swervedrive.SwerveModule(
            ctre.TalonFX(constants.kBLD), ctre.TalonFX(constants.kBLT)
            )
        self.FRModule = components.swervedrive.SwerveModule(
            ctre.TalonFX(constants.kFRD), ctre.TalonFX(constants.kFRT)
            )
        self.BRModule = components.swervedrive.SwerveModule(
            ctre.TalonFX(constants.kBRD), ctre.TalonFX(constants.kBRT)
            )
        
        self.driverController = wpilib.XboxController(constants.kdriverControllerPort)