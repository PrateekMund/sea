import turtle
import random

def tree(n):
    jiaodu = random.randrange(5, 40, 5) # 随机树枝角度
    lr = random.randrange(75, 90, 10)/100 # 随机树枝长度递减比例
    lsize1 = random.randrange(2, 4, 1) # 随机树叶大小
    cuxi = random.randrange(7, 9, 1)/10 # 随机树枝粗细递减大小
    turtle.pensize(n / 15 * cuxi) # 画笔大小
    if n > 20:
# 右边树
        turtle.forward(n)
        turtle.right(jiaodu)
        tree(n*lr)
# 左边树
        turtle.left(jiaodu*2)
        tree(n*lr)
# 返回
        turtle.right(jiaodu)
        turtle.backward(n)
# 树叶
    else :
        turtle.pensize(1)
        turtle.fillcolor("limegreen")
        turtle.pencolor("green")
        turtle.begin_fill()
        turtle.circle(lsize1)
        turtle.end_fill()
# 树枝颜色
    if n > 15 :
        turtle.pencolor("chocolate")
# 落叶
def luoye(midu):
    turtle.fillcolor("limegreen")
    turtle.pencolor("green")

    for i in range(50):
        lsize2 = random.randrange(2, 5, 1)  # 随机落叶大小
        lx =   random.randrange(-400, 400, midu)  # 随机落叶x坐标
        ly =  random.randrange(-220, -180, midu)   # 随机落叶x坐标
        turtle.penup()
        turtle.goto(lx, ly)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(lsize2)
        turtle.end_fill()

def main():

    turtle.left(90)
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.speed(0)
    turtle.pencolor("chocolate")
    tree(100)
    luoye(10)
    turtle.exitonclick()

if __name__ == '__main__':
    main()
