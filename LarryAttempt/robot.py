import wpilib
import magicbot
import ctre
import components.swervedrive
import constants

class Larry(magicbot.MagicRobot):

    #beans. drive is a SwerveDrive, how cool is that woah. i mean not that cool but-
    drive: components.swervedrive.SwerveDrive

    #Create objects. Do it now.
    def createObjects(self):
        #modules (the order is driveMotor, then turnMotor)
        self.FLModule = components.swervedrive.SwerveModule(
            ctre.TalonFX(constants.kFLD), ctre.TalonFX(constants.kFLT),
            )
        self.BLModule = components.swervedrive.SwerveModule(
            ctre.TalonFX(constants.kBLD), ctre.TalonFX(constants.kBLT),
            )
        self.FRModule = components.swervedrive.SwerveModule(
            ctre.TalonFX(constants.kFRD), ctre.TalonFX(constants.kFRT),
            )
        self.BRModule = components.swervedrive.SwerveModule(
            ctre.TalonFX(constants.kBRD), ctre.TalonFX(constants.kBRT),
            )
        
        #controller
        self.driverController = wpilib.XboxController(constants.kdriverControllerPort)

        #gyro (for field centric drive)
        self.gyro = wpilib.ADXRS450_Gyro()

    #called every couple of milliseconds during teleop
    def teleopPeriodic(self):
        #change swerve drive values based on leftX leftY and rightX values
        self.drive.move(self.driverController.getLeftX(), self.driverController.getLeftY(), self.driverController.getRightX())

        #execute is called automatically
if __name__ == "__main__":
    wpilib.run(Larry)

