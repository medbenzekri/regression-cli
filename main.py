from time import sleep
from simple_term_menu import TerminalMenu
import keyboard
from util import calculate
import pandas as pd 

def fill(): 
    global n
    n= int(input("enter the size of your matrix eg: 5 -> matrix(5x5) : "))
    listx= [float(input(f"entre the value x n°{i+1} :")) for i in range(0,n) ]
    listy= [float(input(f"entre the value de y n°{i+1} :")) for i in range(0,n) ]
    matrix.append(listx)
    matrix.append(listy)

if input("do you want ot use dummy values (y/n) ? ")=="y" :
    matrix=[[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],[10, 20, 25, 30, 40, 45, 40, 50, 60, 55]]
    x=matrix[0]
    y=matrix[1]
else:
    n=0
    matrix=[]
    print("the matrix is empty !")
    fill()
    x=matrix[0]
    y=matrix[1]

    def insert_menu():
        insert={"[1] fill the list": fill,
            "[2]restore data":calculate.restore,
            "[3] save data ":calculate.save
        }
        return insert

    def plots():
        plots={"[1] plot the function Dx/y":Calculate.plot_Dxy,
               "[2] plot the function Dx/y":Calculate.plot_Dyx,
               "[3] plot all ":Calculate.point_plot
        }

while(True):
    Calculate=calculate(x,y)
    append= lambda :[ list.append(matrix[i],float(input(f"enter the value you want to add to {t} : "))) for i,t in enumerate(["x","y"]) ]
    values = lambda: print(matrix)
        
    options = {"[1] insert data":insert_menu,
            # "[b] calculate the X̄":Calculate.moyen_x,
            # "[c] calculate the Ȳ ":Calculate.moyen_y,
            
            # "[e] list values":values,
            # "[f] calculate cov(x,y)":Calculate.covxy,
            # "[g] calculate var(x)":Calculate.variance_x,
            # "[h] calculate var(y)":Calculate.variance_y,
            # "[i] calculate σ(x)":Calculate.sdx,
            # "[j] calculate σ(y)":Calculate.sdy,
            # "[k] calculate r(x,y)":Calculate.r_status,
            "[2] regresstion function Dx/y": Calculate.regresstion_Dy_x,
            "[3] regresstion function Dy/x":  Calculate.regresstion_Dx_y,
            "[4] show results": Calculate.results,
            "[5] draw plots":
            "[e] exit ":exit
    }
    functions= options.keys()
    terminal_menu = TerminalMenu(options)
    index = terminal_menu.show()
    functions[index]()
    sleep(0.2)
    print("Press esc to exit or any key to continue ...")
    key= keyboard.read_key()




