import turtle

skor = 0

skorCiz = turtle.Turtle()
skorCiz.speed(0)
skorCiz.color("white")
skorCiz.penup()
skorCiz.setposition(-290,270)
skorMetin = "Skor: %s" %skor
skorCiz.write(skorMetin,False,align="left", font=("Arial", 14, "normal"))
skorCiz.hideturtle()