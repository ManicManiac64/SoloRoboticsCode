"""
right now there's nothing here, this is just a skeleton of what a magicbot robot.py program
would ideally look like
"""

#import the needed modules
import wpilib
import magicbot
import ctre

class MagicRobot(magicbot.MagicRobot):
  def createObjects(self):
    '''To-do: Create stuff'''
  def teleopInit(self):
    '''When teleop starts, this will be called'''
  def teleopPeriodic(self):
    '''For every certain time interval teleop occurs, this is called'''

if __name__ == '__main__':
  wpilib.run(MagicRobot)
