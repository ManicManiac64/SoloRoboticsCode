import wpilib, ctre

class Robot(wpilib.TimedRobot):

    def robotInit(self):
        self.FLmotor = ctre.TalonFX(0)
        self.BLmotor = ctre.TalonFX(1)
        self.FRmotor = ctre.TalonFX(2)
        self.BRmotor = ctre.TalonFX(3)

        self.BLmotor.follow(self.FLmotor)
        self.BRmotor.follow(self.FRmotor)

        self.FLmotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.BLmotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.FRmotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.BRmotor.setNeutralMode(ctre.NeutralMode.Brake)

        self.FRmotor.setInverted(True)

        self.driverController = wpilib.XboxController(0)

    def teleopPeriodic(self):
        LeftY = -(self.driverController.getLeftY())
        RightY = -(self.driverController.getRightY())

        LeftY = 0 if abs(LeftY) <= 0.05 else LeftY
        RightY = 0 if abs(RightY) <= 0.05 else RightY

        self.FLmotor.set(ctre.TalonFXControlMode.PercentOutput, LeftY)
        self.FRmotor.set(ctre.TalonFXControlMode.PercentOutput, RightY)

        wpilib.SmartDashboard.putNumber("left", LeftY)
        wpilib.SmartDashboard.putNumber("Right", RightY)


if __name__ == "__main__":
    wpilib.run(Robot)