from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(-280, 260)
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "left", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)
