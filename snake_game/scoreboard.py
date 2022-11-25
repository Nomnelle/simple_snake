from turtle import Turtle

ALIGNEMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = self.read_data_file()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 280)
        self.print_score()

    def increase_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(
            arg=f"Score : {self.score}, High score : {self.high_score}",
            align=ALIGNEMENT,
            font=FONT,
        )

    def new_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_new_high_score(self.high_score)
        self.score = 0
        self.print_score()

    def read_data_file(self):
        with open("data.txt") as data:
            content = data.read()

        high_score = int(content)
        return high_score

    def write_new_high_score(self, n_high_score):
        with open("data.txt", "w") as data:
            str_high_score = str(n_high_score)
            data.write(str_high_score)
