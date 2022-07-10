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
            ctre.TalonFX(constants.FLD), ctre.TalonFX(constants.FLT),
            )
        self.BLModule = components.swervedrive.SwerveModule(
            ctre.TalonFX(constants.BLD), ctre.TalonFX(constants.BLT),
            )
        self.FRModule = components.swervedrive.SwerveModule(
            ctre.TalonFX(constants.FRD), ctre.TalonFX(constants.FRT),
            )
        self.BRModule = components.swervedrive.SwerveModule(
            ctre.TalonFX(constants.BRD), ctre.TalonFX(constants.BRT),
            )
        
        #controller
        self.driverController = wpilib.XboxController(constants.DRIVER_CONTROLLER_PORT)

        #gyro (for field centric drive)
        self.gyro = wpilib.ADXRS450_Gyro()

    #called every couple of milliseconds during teleop
    def teleopPeriodic(self):
        #change swerve drive values based on leftX leftY and rightX values
        self.drive.move(self.driverController.getLeftX(), self.driverController.getLeftY(), self.driverController.getRightX())

        #execute is called automatically
if __name__ == "__main__":
    wpilib.run(Larry)

