import turtle

drawer = turtle.Turtle()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def drawLine(point, size, leftAngle):
    drawer.up()
    drawer.goto(point.x, point.y)
    drawer.down()
    drawer.left(leftAngle)
    drawer.forward(size)


drawer.color("green")
drawer.forward(80)
# drawLine(Point(-200,0), 400, 0)
# drawer.color("brown")
# drawLine(Point(325, 0), 250, 90)

turtle.done()

#je n'arrive pas à utiliser turtle, comme si je n'avais pas la librairie mais
#elle est bien installé sur mon environnement anaconda
# de plus il me dit que turtle n'as pas de method color x)
# meme en reprenant vos codes