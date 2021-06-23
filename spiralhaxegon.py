import turtle
hex = turtle.Pen()
colors = ["red","yellow","pink","blue",'green',"grey"]
turtle.bgcolor("black")
for i in range(360):
    hex.pencolor(colors[i%6])
    hex.width(i%100+1)
    hex.forward(i)
    hex.left(56)

