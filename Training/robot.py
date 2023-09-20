import wpilib
import ctre

class TrainingBot(wpilib.TimedRobot):

    def robotInit(self):

        self.FLMotor = ctre.TalonFX(0)
        self.BLMotor = ctre.TalonFX(1)
        self.FRMotor = ctre.TalonFX(2)
        self.BRMotor = ctre.TalonFX(3)

        self.BLMotor.follow(self.FLMotor)
        self.BRMotor.follow(self.FRMotor)

        self.FRMotor.setInverted(True)

        self.dawg = wpilib.XboxController(0)

    def teleopPeriodic(self):

        self.left = -(self.dawg.getLeftY())
        self.right = -(self.dawg.getRightY())

        self.FLMotor.set(ctre.TalonFXControlMode.PercentOutput, 0.2 * self.left)
        self.FRMotor.set(ctre.TalonFXControlMode.PercentOutput, 0.2 * self.right)

if __name__ == "__main__":

    wpilib.run(TrainingBot)