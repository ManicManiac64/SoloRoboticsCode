import wpilib, commands2

from robotcontainer import RobotContainer

class MyRobot(commands2.TimedCommandRobot):

    def robotInit(self):
        self.robotContainer = RobotContainer()

    def robotPeriodic(self):

        commands2.CommandScheduler.getInstance().run()

    def teleopPeriodic(self):
        
        pass

if __name__ == "__main__":
    wpilib.run(MyRobot)