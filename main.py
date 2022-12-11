from time import sleep
import keyboard
from util import calculate,menu
import pandas as pd 


@menu
def insert_menu(save=True):
    insert={"[1] fill the list": calculate.fill,
        "[2]restore data":calculate.restore,
    }
    if save:insert["[3] save data "]= Calculate.save
    return insert
@menu
def plots():
    plots={"[1] plot the function Dx/y":Calculate.plot_Dxy,
            "[2] plot the function Dx/y":Calculate.plot_Dyx,
            "[3] plot all ":Calculate.point_plot
    }
    return plots
    
@menu
def main_menu():
    main = {"[1] insert data":insert_menu,
    "[2] regresstion function Dx/y": Calculate.regresstion_Dy_x,
    "[3] regresstion function Dy/x":  Calculate.regresstion_Dx_y,
    "[4] show results": Calculate.results,
    "[5] draw plots":plots,
    "[e] exit ":exit
    }
    return main

if input("do you want ot use dummy values (y/n) ? ")=="y" :
    matrix=[[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],[10, 20, 25, 30, 40, 45, 40, 50, 60, 55]]
    x=matrix[0]
    y=matrix[1]
else:
    n=0
    matrix=[]
    print("the matrix is empty do you want to fill or restore  ")
    insert_menu(save=False)


while(True):
    Calculate=calculate(x,y)
    append= lambda :[ list.append(matrix[i],float(input(f"enter the value you want to add to {t} : "))) for i,t in enumerate(["x","y"]) ]
    values = lambda: print(matrix)
    main_menu()
    sleep(0.2)
    print("Press esc to exit or any key to continue ...")
    key= keyboard.read_key()




