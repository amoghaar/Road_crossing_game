from turtle import Turtle

# Font settings for the scoreboard
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """A class representing the scoreboard in the game."""

    def __init__(self):
        """Initialize the Scoreboard object."""
        super().__init__()
        self.hideturtle()  # Hide the turtle icon
        self.color("black")  # Set the color of the text
        self.penup()  # Lift the pen to avoid drawing a line
        self.level = -1  # Initialize the level to -1 (before the game starts)
        self.goto(x=-290, y=260)  # Set the initial position for the scoreboard
        self.level_increase()  # Call the level_increase method to display the initial level

    def level_increase(self):
        """Increase the level and update the display on the scoreboard."""
        self.level += 1  # Increase the level by 1
        self.clear()  # Clear the previous level display
        self.write(f"Level : {self.level}", align="left", font=FONT)  # Display the updated level

    def game_over(self):
        """Display 'Game Over' message on the scoreboard."""
        self.goto(x=0, y=0)  # Set the position for the 'Game Over' message
        self.write(f"Game Over", align="center", font=FONT)  # Display the 'Game Over' message
