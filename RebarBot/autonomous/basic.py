from magicbot import AutonomousStateMachine, timed_state, state

from components.drivetrain import Drivetrain

class Basic(AutonomousStateMachine):

    MODE_NAME = "Basic"
    DEFAULT = True

    drivetrain: Drivetrain

    @timed_state(duration=1, first=True, next_state="driveBackward")
    def driveForward(self):
        self.drivetrain.move(0.4, 0.4)

    @timed_state(duration=2, next_state="stop")
    def driveBackward(self):
        self.drivetrain.move(-1.0, -1.0)
    
    @state
    def stop(self):
        self.drivetrain.move(0.0, 0.0)