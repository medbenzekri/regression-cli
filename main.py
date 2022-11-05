from time import sleep
from simple_term_menu import TerminalMenu
import keyboard
from util import calculate
n=3
matrix=[[0,1,2,3,4,5,6,7,8,9],[10,20,25,30,40,45,40,50,60,55]]
x=matrix[0]
y=matrix[1]
xory=TerminalMenu(["[x] append to x"," [y] append to y"])
while(True):
    Calculate=calculate(x,y)
    append= lambda :[ list.append(matrix[i],float(input(f"enter the value you want to add to {t} : "))) for i,t in enumerate(["x","y"]) ]
    values = lambda: print(matrix)
    def fill(): 
        global n
        n= int(input("enter the size of your matrix eg: 5 -> matrix(5x5) : "))
        listx= [float(input(f"entre the value x n°{i+1} :")) for i in range(0,n) ]
        listy= [float(input(f"entre the value de y n°{i+1} :")) for i in range(0,n) ]
        matrix.append(listx,listy)
        

    options = ["[a] add values to the matrix",
            "[b] calculate the X̄", 
            "[c] calculate the Ȳ ", 
            "[d] fill the list",
            "[e] list values",
            "[f] calculate cov(x,y)",
            "[g] calculate var(x)",
            "[h] calculate var(y)",
            "[i] calculate σ(x)",
            "[j] calculate σ(y)",
            "[k] calculate r(x,y)",
            "[l] linear regresstion function ",
            "[m] plot points",
            "[n] exit "
            ]
    functions= [append,Calculate.moyen_x,
                Calculate.moyen_y,fill,
                values,Calculate.covxy,
                Calculate.variance_x,Calculate.variance_y,Calculate.sdx,
                Calculate.sdy,Calculate.r_status,
                Calculate.regresstion_eq,
                Calculate.point_plot,
                exit]
    terminal_menu = TerminalMenu(options)
    index = terminal_menu.show()
    functions[index]()
    sleep(0.2)
    input("Press esc to exit or any key to continue ...")
    #key= keyboard.read_key()




