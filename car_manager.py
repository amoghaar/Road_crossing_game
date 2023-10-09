from turtle import Turtle
import random

# Possible colors for the cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# Initial move distance for cars and increment for each level
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    """A class representing the car manager in the game."""

    def __init__(self):
        """Initialize the CarManager object."""
        super().__init__()
        self.all_cars = []  # List to store all car objects
        self.car_speed = STARTING_MOVE_DISTANCE  # Initial car speed

    def creating_cars(self):
        """Create a car with a certain probability."""
        random_num = random.randint(0, 6)  # Generate a random number
        if random_num == 1:
            ammu = Turtle("square")  # Create a car object
            ammu.penup()
            ammu.shapesize(stretch_wid=1, stretch_len=2)
            ammu.color(random.choice(COLORS))  # Randomly select a color for the car
            random_y = random.randint(-250, 250)
            ammu.goto(x=300, y=random_y)  # Set the car's initial position
            self.all_cars.append(ammu)  # Add the car to the list of all cars

    def move(self):
        """Move all cars backward."""
        for car in self.all_cars:
            car.backward(self.car_speed)  # Move each car backward

    def level_up_speed(self):
        """Increase the car speed for a new level."""
        self.car_speed += MOVE_INCREMENT  # Increase the car speed for the next level
