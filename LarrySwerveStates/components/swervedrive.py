import math

import magicbot
import wpilib
import wpimath.controller
import ctre

import constants

class SwerveModule:
    """
    Create a swerve module.
    """

    def __init__(self, driveMotor: ctre.TalonFX, turnMotor: ctre.TalonFX, reversedDrive: bool, reversedTurn: bool):

        self.driveMotor = driveMotor
        self.turnMotor = turnMotor

        self.sensor = ctre.TalonFXSensorCollection(self.turnMotor)
        self.sensor.setIntegratedSensorPositionToAbsolute(10)
        self.turnMotor.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, 10)

        self.driveMotor.setInverted(reversedDrive)
        self.turnMotor.setInverted(reversedTurn)

        self.turningPID = wpimath.controller.PIDController(constants.kP, 0.0, 0.0)
        self.turningPID.enableContinuousInput(-math.pi, math.pi)

    def getTurnPos(self):
        self.turnMotor.getSelectedSensorPosition()