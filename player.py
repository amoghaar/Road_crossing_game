from turtle import Turtle

# Constants for the starting position, move distance, and finish line y-coordinate
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """A class representing the player turtle in the game."""

    def __init__(self):
        """Initialize the Player object."""
        super().__init__()
        self.shape("turtle")  # Set the shape of the turtle
        self.penup()  # Lift the pen to avoid drawing a line
        self.starting_point()  # Set the starting point for the player

    def starting_point(self):
        """Set the starting point of the player."""
        self.goto(STARTING_POSITION)  # Move the player to the starting position
        self.left(90)  # Turn the player to face upwards

    def move(self):
        """Move the player forward by a specified distance."""
        self.forward(MOVE_DISTANCE)  # Move the player forward by MOVE_DISTANCE units

    def level_up(self):
        """Reset the player to the starting position for a new level."""
        self.goto(STARTING_POSITION)  # Move the player to the starting position
