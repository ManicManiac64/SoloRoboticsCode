"""
This is the robot.py file. It creates objects, executes code during teleop, and runs the robot.
"""

# import modules
import wpilib
import magicbot
import ctre
import constants
import components.swervedrive

class Larry(magicbot.MagicRobot):

    swerve: components.swervedrive.SwerveDrive