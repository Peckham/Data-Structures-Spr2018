import turtle

def tree(branchLen,t):
    if branchLen > 5:
        # TO DO
        # Complete the tree branching algorithm
        t.forward(branchLen)
        t.right(25)
        tree(branchLen - 5, t)
        t.left(50)
        tree(branchLen - 5, t)
        t.right(25)
        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.backward(100)
    t.color("green")
    tree(100,t)
    myWin.exitonclick()

main()
