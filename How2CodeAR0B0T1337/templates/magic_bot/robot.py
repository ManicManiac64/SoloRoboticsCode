import wpilib
import magicbot
import components.component
import constants

class RobotName(magicbot.MagicRobot):

    exampleComponent: components.component.Component

    def createObjects(self):
        """
        Create objects. Wow!!!
        """

    def teleopPeriodic(self):
        """
        Called every time robot is in teleop
        """    

        self.exampleComponent.setFunc()

if __name__ == '__main__':
    wpilib.run(RobotName)
