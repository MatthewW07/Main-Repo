
import turtle as trtl

spider = trtl.Turtle()
spider.pensize(40)

spider.speed(0)

# create body
spider.circle(20)


# initialize leg variables
# w = legs
legs = 10
# y = legLength
legLength = 70
# z = legAngle
legAngle = 360 / (legs + 2)
spider.pensize(5)


# create the legs
# n = leg
curLeg = 0
while (curLeg < legs):
    spider.goto(0,20)
    if curLeg > (legs/2):
        spider.setheading(legAngle * curLeg)
    else:
        spider.setheading(legAngle * curLeg - 45)
    spider.fd(legLength)
    curLeg += 1


# eyes
eyeAngle = 50
eye = 0
while eye < 2:
    spider.goto(0,20)
    spider.pendown()
    spider.setheading(eyeAngle * eye + 60)
    spider.fd(20)
    spider.color("red")
    spider.circle(5)
    spider.penup()
    spider.color("black")
    eye += 1


spider.hideturtle()

# end loop
wn = trtl.Screen()
wn.mainloop()