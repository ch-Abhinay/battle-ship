import random as rd
import tkinter as tk
def game():
    def emptyGrid(rows,cols):
        grid=[]
        for i in range(rows):
            tem=[]
            for j in range(cols):
                tem.append(1)
            grid.append(tem)
        #print(grid)
        return grid
    def createship(grid,rows,cols):
        y=rd.randint(0,rows-1)
        x=rd.randint(1,cols-2)
        a=rd.randint(0,1)
        if grid[x][y]!=SHIP_UNCLICKED:
            if a==0:
                grid[x][y]=SHIP_UNCLICKED
                grid[x-1][y]=SHIP_UNCLICKED
                grid[x+1][y]=SHIP_UNCLICKED
            else:
                if y-1>=0 and y+1<=cols-1:
                    grid[x][y]=SHIP_UNCLICKED
                    grid[x][y-1]=SHIP_UNCLICKED
                    grid[x][y+1]=SHIP_UNCLICKED
                else:
                    return createship(grid,rows,cols)
            return grid
    def addShips(grid,rows,cols):
        y=rd.randint(0,rows-1)
        x=rd.randint(1,cols-2)
        a=rd.randint(0,1)
        if grid[x][y]!=SHIP_UNCLICKED:
            if a==0 and grid[x-1][y]!=SHIP_UNCLICKED and grid[x+1][y]!=SHIP_UNCLICKED:
                grid[x][y]=SHIP_UNCLICKED
                grid[x-1][y]=SHIP_UNCLICKED
                grid[x+1][y]=SHIP_UNCLICKED
            else:
                if y-1>=0 and y+1<=cols-1 and grid[x][y-1]!=SHIP_UNCLICKED and grid[x][y+1]!=SHIP_UNCLICKED:
                    grid[x][y]=SHIP_UNCLICKED
                    grid[x][y-1]=SHIP_UNCLICKED
                    grid[x][y+1]=SHIP_UNCLICKED
                else:
                    return addShips(grid,rows,cols)
            #print(grid)
            return grid
    def result(userscore,compscore):
        if userscore>compscore:
            userLabel.configure(text='user is the winner')
            print('user is the winner by ',userscore,'points')
        elif userscore==compscore:
            userLabel.configure(text='tie')
            compLabel.configure( text='tie')
            print('tie')
        else:
            compLabel.configure(text='computer is the winner')
            print('computer is the winner by ',compscore,'points')

    def compships(grid,rows,cols):
        comy=int(input('select coloum:'))
        comx=int(input('select row:'))
        ore=int(input('select oreantation 0 or 1'))
        if ore==0 and comx-1>=0 and comx+1<=rows-1 :
            grid[comx][comy]=SHIP_UNCLICKED
            grid[comx-1][comy]=SHIP_UNCLICKED
            grid[comx+1][comy]=SHIP_UNCLICKED
        else:
            if comy-1>=0 and comy+1<=cols-1:
                grid[comx][comy]=SHIP_UNCLICKED
                grid[comx][comy-1]=SHIP_UNCLICKED
                grid[comx][comy+1]=SHIP_UNCLICKED
            else:
                return compships(grid,rows,cols)
        return grid
    def drawGrid(canvas, grid):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                x0, y0 = col * 20, row * 20
                x1, y1 = x0 + 20, y0 + 20
                if grid[row][col] == EMPTY_UNCLICKED:
                    canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
                elif grid[row][col] == SHIP_UNCLICKED:
                    canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
                elif grid[row][col] == EMPTY_CLICKED:
                    canvas.create_rectangle(x0, y0, x1, y1, fill="white")
                else:
                    canvas.create_rectangle(x0, y0, x1, y1, fill="red")

    def onClick(event):
        global usercount
        global userscore
        row, col = event.y // 20, event.x // 20
        if userGrid[row][col] == SHIP_UNCLICKED:
            userGrid[row][col] = SHIP_CLICKED
            drawGrid(userCanvas, userGrid)
            userCanvas.update()
            userLabel.configure(text="Hit!")
            userscore+=1
            if userscore==n*3:
                result(userscore,compscore)
        elif userGrid[row][col]== SHIP_CLICKED:
            pass
        else:
            userLabel.configure(text="Miss!")
            userGrid[row][col]= EMPTY_CLICKED
            drawGrid(userCanvas, userGrid)
            userCanvas.update()
        comclick(x,y)
        usercount+=1

    def comclick(rows,cols):
        global compcount
        global compscore
        xcom=rd.randint(0,rows-1)
        ycom=rd.randint(0,cols-1)
        if compGrid[ycom][xcom]== SHIP_UNCLICKED:
            compGrid[ycom][xcom] = SHIP_CLICKED
            drawGrid(compCanvas, compGrid)
            compCanvas.update()
            compLabel.configure(text="Hit!")
            compscore+=1
            if compscore==n*3:
                result(userscore,compscore)
        elif compGrid[ycom][xcom]== EMPTY_CLICKED:
            comclick(rows,cols)
        elif compGrid[ycom][xcom] == SHIP_CLICKED:
            pass
        else:
            compLabel.configure(text="Miss!")
            compGrid[ycom][xcom]= EMPTY_CLICKED
            drawGrid(compCanvas, compGrid)
            compCanvas.update()
        compcount+=1
    x=int(input('no of rows(min 5 rows):'))
    y=int(input('no of coloums(min 5 cols):'))
    # Main program
    root = tk.Tk()
    root.title("Battleship")

    # Set up the user grid
    userFrame = tk.Frame(root)
    userLabel = tk.Label(userFrame, text="user")
    userLabel.pack()
    userCanvas = tk.Canvas(userFrame, width=200, height=200)
    userCanvas.pack()
    a=emptyGrid(x,y)
    n=int(input('no of ships'))
    for i in range(n):
        b=addShips(a,x,y)
    userGrid =b
    drawGrid(userCanvas, userGrid)
    userCanvas.bind("<Button-1>", onClick)
    userFrame.pack(side= tk.LEFT)
    # Set up the user grid
    compFrame = tk.Frame(root)
    compLabel = tk.Label(compFrame, text="comp")
    compLabel.pack()
    compCanvas = tk.Canvas(compFrame, width=200, height=200)
    compCanvas.pack()
    d=emptyGrid(x,y)
    for i in range(n):
        c=compships(d,x,y)
    compGrid =c
    drawGrid(compCanvas, compGrid)
    compCanvas.bind("<Button-1>", onClick)
    compFrame.pack(side= tk.RIGHT)
    root.mainloop()
while True:
    compcount=0
    usercount=0
    compscore=0
    userscore=0
    EMPTY_UNCLICKED = 1
    SHIP_UNCLICKED = 2
    EMPTY_CLICKED = 3
    SHIP_CLICKED = 4
    ans=input('do u want to play(y/n):')
    if ans=='y':
        game()
    elif ans=='n':
        break
    else:
        print('i did not get u')