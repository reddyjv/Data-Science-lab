import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
y=np.sin(x)
plt.figure()
plt.plot(x,y)
plt.title("line chart")
plt.xlabel("x-axis")
plt.ylabel("Y-axis")

categories=['A','B',"c","d"]
values=[20,35,30,25]
plt.figure()
plt.bar(categories,values)
plt.title("line chart")
plt.xlabel("x-axis")
plt.ylabel("Y-axis")

x=np.random.randn(100)
y=np.random.randn(100)
colors=np.random.rand(100)
sizes=100*np.random.rand(100)
plt.figure()
plt.scatter(x,y,c=colors,s=sizes,alpha=0.5)
plt.title("line chart")
plt.xlabel("x-axis")
plt.ylabel("Y-axis")