#  pip install vpython
from vpython import *   

pop=vector(0,0,0)

rin = ring(pos=pop,color=color.red,make_trail=True,thickness=0.5,retain=100)

t=0
dt=0.01

while(t<=1000):
    
    rate(100)
    
    rin.pos.x = 1/sin(t)
    
    t =t + dt
    
print("End of program")