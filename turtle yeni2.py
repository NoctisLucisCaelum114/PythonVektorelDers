while True:
    from turtle import *
    renk = ["red","green","blue","yellow"]

    speed(500)
    for a in range(1):
        pensize(5)
        color("blue")
        for x in range (10):
            speed(600)
            forward(10)
            right(20)
            speed(90)
    for a in range(10):
        speed(500)
        pensize(0)
        color("red")
        goto(0,a)
        for x in range(4):
            forward(100)
            right(90)
            circle(50)

    for a in range(5):
        color("purple")
        speed(200)
        forward(10)
        left(10)
        right(15)
        back(20)
    
    for a in range(20):
        color("brown")
        pensize(5)
        circle(20)
        speed(200)
        circle(100)
        