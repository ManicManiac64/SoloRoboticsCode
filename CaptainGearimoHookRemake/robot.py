import wpilib
import ctre
import magicbot

import constants
import components.drivetrain
import components.climber
import components.intake
import components.launcher

class CaptainHook(magicbot.MagicRobot):

    drivetrain: components.drivetrain.Drivetrain
    climber: components.climber.Climber
    intake: components.intake.Intake
    launcher: components.launcher.Launcher

    def createObjects(self):
        
        self.FLMotor = ctre.WPI_TalonFX(constants.kfrontLeftPort)
        self.BLMotor = ctre.WPI_TalonFX(constants.kbackLeftPort)
        self.FRMotor = ctre.WPI_TalonFX(constants.kfrontRightPort)
        self.BRMotor = ctre.WPI_TalonFX(constants.kbackRightPort)

        self.SCMotor = ctre.WPI_TalonFX(constants.kshortClimberPort)
        self.TCMotor = ctre.WPI_TalonFX(constants.ktiltedClimberPort)

        self.intakeSolenoid = wpilib.DoubleSolenoid(constants.ksolenoidModule, wpilib.PneumaticsModuleType.CTREPCM, constants.kintakeSolenoidIn, constants.kintakeSolenoidOut)
        self.bottomMotor = ctre.WPI_TalonFX(constants.kbottomIntakePort)
        self.topMotor = ctre.WPI_TalonFX(constants.ktopIntakePort)

        self.launcherSolenoid = wpilib.DoubleSolenoid(constants.ksolenoidModule, wpilib.PneumaticsModuleType.CTREPCM, constants.klauncherSolenoidIn, constants.klauncherSolenoidOut)

        self.driverController = wpilib.XboxController(constants.kdriverControllerPort)
        self.functionsController = wpilib.XboxController(constants.kfunctionsControllerPort)

    def teleopPeriodic(self):

        if self.driverController.getLeftBumper() or self.driverController.getRightBumper():
            self.drivetrain.userDrive(-self.driverController.getLeftY(), -self.driverController.getRightY(), 0.5)
        else:
            self.drivetrain.userDrive(-self.driverController.getLeftY(), -self.driverController.getRightY(), 1)

        self.climber.changePercent(-self.functionsController.getLeftY() * constants.kclimbPercent, -self.functionsController.getRightY() * constants.kclimbPercent)
        
        if self.functionsController.getXButtonPressed():
            self.intake.toggle()
        
        if self.functionsController.getLeftBumper():
            self.intake.spinBottom(0.3)
        
        if self.functionsController.getRightBumper():
            self.intake.spinBottom(-0.3)
        
        if self.functionsController.getLeftBumperReleased() or self.functionsController.getRightBumperReleased():
            self.intake.spinBottom(0.0)

        if self.functionsController.getYButton():
            self.intake.spinTop(0.25)
        
        if self.functionsController.getAButton():
            self.intake.spinTop(-0.25)
        
        if self.functionsController.getYButtonReleased() or self.functionsController.getAButtonReleased():
            self.intake.spinTop(0.0)

if __name__ == '__main__':
    wpilib.run(CaptainHook)