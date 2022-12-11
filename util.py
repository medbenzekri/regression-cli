from cProfile import label
import math
from matplotlib.pyplot import plot,show,legend
from numpy import array,roots
from sympy import symbols, Eq, solve 
import pickle
from simple_term_menu import TerminalMenu

class calculate:
    instance=None
    initialized=False
    def __new__(cls,x,y):
        print(calculate.instance)
        if calculate.instance==None:
            cls.instance = super(calculate, cls).__new__(cls)
        else:calculate.initialized=True
        return cls.instance

    def __init__(self,x,y):
        if calculate.initialized:return
        self.x=array(x)
        self.y=y
        self.n=len(x)
        self.x_bar=self.moyen(x)
        self.y_bar=self.moyen(y)
        self.var_x=self.variance(x,self.x_bar)
        self.var_y=self.variance(y,self.y_bar)
        self.cov_xy=self.co_variance()
        #standard diviation (ecart type)
        self.standard_diviation_x=math.sqrt(self.var_x)
        self.standard_diviation_y=math.sqrt(self.var_y)
        #cofitient of corolation
        self.r=self.cov_xy/(self.standard_diviation_x*self.standard_diviation_y)
        # values of a,b,α
        self.a=self.cov_xy/self.var_x
        self.b=self.y_bar-self.a*self.x_bar
        self.y_function=self.a*self.x+self.b
        self.alpha= self.cov_xy/self.var_y
        self.beta=self.x_bar-self.alpha*self.y_bar
        self.a_prime=1/self.alpha
        self.b_prime=-self.beta/self.alpha
        self.y_function_dxy=self.a_prime*self.x+self.b_prime
        calculate.initialized=True
    def moyen(self,t):return sum(t)/len(t)

    def variance(self,t,m): return sum([xi**2 for xi in t ])/self.n -m**2 

    def co_variance(self): return sum([xi*yi for xi,yi in zip(self.x,self.y)])/self.n -(self.x_bar*self.y_bar)

    def moyen_x(self): print(f"X̄={self.x_bar:.2f}")

    def moyen_y(self):print(f"Ȳ={self.y_bar:.2f}")

    def variance_x(self): print(f"var(x)={self.var_x:.2f}")

    def variance_y(self): print(f"var(y)={self.var_y:.2f}")

    def covxy(self):print(f"cov(x,y)={self.cov_xy:.2f}")
    def sdx(self):print(f"σ(x)={self.standard_diviation_x:.2f}")
    def sdy(self):print(f"σ(y)={self.standard_diviation_y:.2f}")
    def r_status(self):print(f"""r is {self.r:.2f} so there is {f'a strong {"positive" if self.r>0 else "negative"} corolation' if 
                                                    abs(self.r)>=.5 else 'no corolation'  }""")
    def regresstion_Dy_x(self):return print(f"Y={self.a:.2f}X{self.b:+.2f}")
    def regresstion_Dx_y(self):x=f"Y={self.a_prime:.2f}X{self.beta:+.2f}";print(x);return x
    def point_plot(self):
        plot(self.x,self.y,".")
        self.plot_Dxy(shows=False)
        self.plot_Dyx(shows=False)
        legend(loc='upper left')
        show()
    def plot_Dxy(self,shows=True):
        plot(self.x,self.y,".")
        plot(self.x,self.y_function_dxy,"-",label=self.regresstion_Dx_y)
        if shows:show()

        pass
    def plot_Dyx(self,shows=True):
        plot(self.x,self.y,".")
        plot(self.x,self.y_function,"-",label=self.regresstion_Dy_x)
        if shows:show()
        pass
    def save(self):
        with open("Data", 'wb') as file:
            pickle.dump(self,file)
            file.close()
    def load(name="Data"):
        try:
            with open(name,"rb") as file:
                x=pickle.load(file)
                file.close()
                return x
        except :
            print("No previous saves ....!")
    def restore():
        calculate.instance=calculate.load()
    
    def results(self):
        self.moyen_x()
        self.moyen_y()
        self.variance_x()
        self.variance_y()
        self.covxy()
        self.sdx()
        self.sdy()

    


    def moin_de_rec(self):
        lam,x1,x2= Symbols('λ','x1','x2')
        varx1= self.var_x
        varx2=self.var_y
        cov= self.cov_xy
        v=array([[varx1,cov],[cov,varx2]])
        a=1
        b=varx1-varx2
        c=varx1*varx2-cov**2
        lam1,lam2= roots([a,b,c])
        Max_lam=max(lam1,lam2)
        first_eq=Eq((varx1-Max_lam)*x1+cov*x2,0)
        second_eq=Eq((varx2-Max_lam)*x1+cov*x2,0)
        #u1=solve((first_eq,second_eq),(x1,x2))
        print(u1)

    def fill(): 
        n= int(input("enter the size of your matrix eg: 5 -> matrix(5x5) : "))
        listx= [float(input(f"entre the value x n°{i+1} :")) for i in range(0,n) ]
        listy= [float(input(f"entre the value de y n°{i+1} :")) for i in range(0,n) ]
        calculate.instance=calculate(x,y)



'''this is a decorator function for the menu '''
def menu(func):
    def wrapper(*args, **kwargs):
        dic=func(*args, **kwargs)
        options=dic.keys()
        functions=list(dic.values())
        menu = TerminalMenu(options)
        index= menu.show()
        functions[index]() 
    return wrapper
        


# def plot(func):
#     def wrapper():
#         plot(func())
#         plot
#         legend(loc='upper left')
#         show()
#     return wrapper


if __name__ == "__main__":
    matrix=[[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],[10, 20, 25, 30, 40, 45, 40, 50, 60, 55]]
    cal=calculate(matrix[0],matrix[0])
    cal.moin_de_rec()