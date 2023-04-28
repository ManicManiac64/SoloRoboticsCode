import ctre, wpilib, commands2

class Drivetrain(commands2.SubsystemBase):

    def __init__(self):

        super().__init__()

        self.FLMotor = ctre.TalonFX(0)
        self.BLMotor = ctre.TalonFX(1)
        self.FRMotor = ctre.TalonFX(2)
        self.BRMotor = ctre.TalonFX(3)

        self.BLMotor.follow(self.FLMotor)
        self.BRMotor.follow(self.FRMotor)

        self.FRMotor.setInverted(True)

        self.FLMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.BLMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.FRMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.BRMotor.setNeutralMode(ctre.NeutralMode.Brake)

    def joystickDriving(self, leftJoy, rightJoy):
        leftJoy = 0 if abs(leftJoy) <= 0.05 else leftJoy
        rightJoy = 0 if abs(leftJoy) <= 0.05 else rightJoy

        leftJoy  *= -1
        rightJoy *= -1

        self.FLMotor.set(ctre.ControlMode.PercentOutput, leftJoy)
        self.FRMotor.set(ctre.ControlMode.PercentOutput, rightJoy)

        