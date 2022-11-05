import math
from matplotlib.pyplot import plot,show
from numpy import array
class calculate:
    def __init__(self,x,y) -> None:
        self.x=array(x)
        self.y=array(y)
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
        self.a=self.cov_xy/self.var_x
        self.b=self.y_bar-self.a*self.y_bar
        self.y_function=self.a*self.x+self.b
    def moyen(self,t):return sum(t)/len(t)
    def variance(self,t,m): return sum([xi**2 for xi in t ])/self.n -m**2 
    def co_variance(self): return sum([xi*yi for xi,yi in zip(self.x,self.y)])/self.n -(self.x_bar*self.y_bar)
    # def co_variance(self): return sum([xi*yi for xi,yi in zip(self.x,self.y)])/self.n -(self.x_bar*self.y_bar)
    def moyen_x(self): print(f"X̄={self.x_bar:.2f}")
    def moyen_y(self):print(f"Ȳ={self.y_bar:.2f}")
    def variance_x(self): print(f"var(x)={self.var_x:.2f}")
    def variance_y(self): print(f"var(y)={self.var_y:.2f}")
    def covxy(self):print(f"cov(x,y)={self.cov_xy:.2f}")
    def sdx(self):print(f"σ(x)={self.standard_diviation_x:.2f}")
    def sdy(self):print(f"σ(y)={self.standard_diviation_y:.2f}")
    def r_status(self):print(f"""r is {self.r:.2f} so there is {f'a strong {"positive"if self.r>0 else "negative"} corolation' if 
                                                    abs(self.r)>=.5 else 'no corolation'  }""")
    def regresstion_eq(self):print(f"Y={self.a:.2f}X{self.b:+.2f}")
    def point_plot(self):plot(self.x,self.y,".");plot(self.x,self.y_function,"-");show()
