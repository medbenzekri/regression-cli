from cProfile import label
import math
from matplotlib.pyplot import plot,show,legend
from numpy import array
import pickle
class calculate:
    instance=None
    def __init__(self,x,y):
        if calculate.instance: return calculate.instance
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
    def r_status(self):print(f"""r is {self.r:.2f} so there is {f'a strong {"positive"if self.r>0 else "negative"} corolation' if 
                                                    abs(self.r)>=.5 else 'no corolation'  }""")
    def regresstion_Dy_x(self):return print(f"Y={self.a:.2f}X{self.b:+.2f}")
    def regresstion_Dx_y(self):x=f"Y={self.a_prime:.2f}X{self.beta:+.2f}";print(x);return x
    def point_plot(self):
        plot(self.x,self.y,".")
        plot(self.x,self.y_function,"-",label=self.regresstion_Dy_x)
        plot(self.x,self.y_function_dxy,"-",label=self.regresstion_Dx_y)
        legend(loc='upper left')
        show()
    def plot_Dxy(self):
        
    def plot_Dyx(self):    
    def save(self):
        with open("Data", 'wb') as file
            pickle.dump(self,file)
            file.close()
    def load(name="Data"):
        try:
        with open(name,"rb") as file
            return pickle.load(file)
        except:
            print("No previous saves ....!")
    def restore():
        calculate.instance=load()
    