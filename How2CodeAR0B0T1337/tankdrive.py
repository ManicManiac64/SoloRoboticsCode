from turtle import left, right
import wpilib
import wpilib.drive
import ctre

class TankBot(wpilib.TimedRobot):

    def robotInit(self):

        self.FLMotor = ctre.TalonFX(0)
        self.BLMotor = ctre.TalonFX(1)
        self.FRMotor = ctre.TalonFX(2)
        self.BRMotor = ctre.TalonFX(3)

        self.BLMotor.follow(self.FLMotor)
        self.BRMotor.follow(self.FRMotor)

        self.FLMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.BLMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.FRMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.BRMotor.setNeutralMode(ctre.NeutralMode.Brake)

        self.driverController = wpilib.XboxController(0)

    def teleopPeriodic(self):

        self.FLMotor.set(ctre.ControlMode.PercentOutput, -self.driverController.getLeftY())
        self.FRMotor.set(ctre.ControlMode.PercentOutput, -self.driverController.getRightY())

if __name__ == "__main__":
    wpilib.run(TankBot)