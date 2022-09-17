from vpython import *
size = 0.1

scene = canvas(width=600, height=400, center=vector(2.5,0,0), background=vector(0,0,0))

x = arrow(pos=vector(0,0,0), axis=vector(1,0,0), shaftwidth=0.02, color=color.green)
y = arrow(pos=vector(0,0,0), axis=vector(0,1,0), shaftwidth=0.02, color=color.red)
z = arrow(pos=vector(0,0,0), axis=vector(0,0,1), shaftwidth=0.02, color=color.blue)
ball = sphere(radius=0.2, color=color.yellow, pos=vector(0,0,0), v=vector(3,0,0))

gd = graph(title = "x-t plot", width=600, height=400, xtitle="t", ytitle="x")
f1 = gcurve(color=color.blue)  
gd1 = graph(title = "v-t plot", width=600, height=400, xtitle="t", ytitle="x")
f2 = gcurve(color=color.green)
gd3 = graph(title = "a-t plot", width=600, height=400, xtitle="t", ytitle="x")
f3 = gcurve(color=color.red)

dt = 0.001
t = 0.0
v=vector(3,0,0)
a=vector(-1,-0.5,0)

while t<6:
    rate(1/dt)
    t = t+dt
    ball.pos = ball.pos + ball.v*dt
    ball.v = ball.v + a*dt
    ball.a = a
    
    T=0.4
    plot_t = t%T    
    if plot_t + dt >= T and plot_t < T:
        sphere(radius=0.2, color=color.yellow, pos=vector(ball.pos.x,ball.pos.y,0))
        arrow(pos=vector(ball.pos.x,ball.pos.y,0), axis=vector(-1,-0.5,0), shaftwidth=0.02, color=color.red)
        arrow(pos=vector(ball.pos.x,ball.pos.y,0), axis=vector(ball.v.x,ball.v.y,0), shaftwidth=0.02, color=color.green)
    f1.plot(pos=(t,ball.pos.x))    
    f2.plot(pos=(t,ball.v.x))
    f3.plot(pos=(t,ball.a.x))
    if ball.v.x > 0 and ball.v.x + ball.a.x*dt < 0:
        print('time:',t)
        print('position:',ball.pos)
        print('velocity:',ball.v)