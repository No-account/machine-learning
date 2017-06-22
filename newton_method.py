#牛顿法解方程f（x）=0，求x

#计算出f（x）与0的差值
def dx(f,x):
    return abs(0-f(x))

#牛顿法
def newton_method(f,df,x0,e):
    delta=dx(f,x0)
    while(delta>e):
        x0=x0-f(x0)/df(x0)
        #每次迭代要重新计算delta
        delta=dx(f,x0)
    print(x0,f(x0))

#计算出f（x）
def f(x):
    return 6*x**5-5*x**4-4*x**3+3*x**2

#f（x）的倒数
def df(x):
    return 30*x**4-20*x**3-12*x**2+6*x

#要指定几个起始点
x0s = [0.1, .5, 1.2]
for x0 in x0s:
    newton_method(f, df, x0, 1e-5)
