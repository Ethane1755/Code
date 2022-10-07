from vpython import *
#Web VPython 3.2

m1 = 2.0                   #球1質量
x1 = -20.0                  #球1X軸初位置
v1= 6.0                    #球1初速度
size1 = 1.0                 #球1大小

m2 = 1.0                   #球2質量
x2 = -5.0                   #球2X軸初位置
v2= 2.0                    #球2初速度
size2 = 1.0                 #球2大小

spring_k = 5.0                #彈力大小
spring_L = 5.0             #彈簧長度 

scene = canvas(width=1000, height=300, background=vec(0.6,0.8,0.8), center=vec(5,0,10),forward=vec(0,0,-1),range=10, fov=0.004)#設定畫面
ball1 = sphere(radius=size1, color = color.red, make_trail = False)  #設定球1
ball1.pos = vector(x1,0,0)             #球1位置
ball1.v = vector (v1,0,0)                        #球1的速度
v1_arrow = arrow(pos=ball1.pos,axis=ball1.v,shaftwidth=0.2*size1 ,color = color.red)

ball2 = sphere(radius=size2, color = color.blue,make_trail = False) #設定球2
ball2.pos = vector(x2,0,0)             #球2位置
ball2.v = vector (v2,0,0)                        #球2的速度
v2_arrow = arrow(pos=ball2.pos,axis=ball2.v,shaftwidth=0.2*size2 ,color = color.blue)

spring = helix(pos=ball2.pos, radius=0.5, thickness =0.1) #畫彈簧
spring.coils = 10
spring.axis = vector(-spring_L,0,0)

t = 0                                            #時間
dt = 0.001                                       #單位時間
x_t = graph(align='left',width=333,height=300,     #畫x-t圖                                  
              title='K-purple, U-green,E-black', xtitle='t', ytitle='E',
              foreground=color.black,background=color.white,
              xmax=8, xmin=0, ymax=40, ymin=0)
f1_1 = gcurve(color=color.purple)       
f1_2 = gcurve(color=color.green)
f1_3 = gcurve(color=color.black)
v_t = graph(align='left',width=333,height=300,   #畫v-t圖                                  
              title='P1-red, P2-blue, P-black', xtitle='t', ytitle='P',
              foreground=color.black,background=color.white,
              xmax=8, xmin=0, ymax=20, ymin=0)
f2_1 = gcurve(color=color.red)       
f2_2 = gcurve(color=color.blue) 
f2_3 = gcurve(color=color.black) 

while True :
    rate(1000)
    
    ball1.pos = ball1.pos
    ball2.pos = ball2.pos
    
    if mag(ball2.pos - ball1.pos) <= spring_L :
        ball1_a = -1 * spring_k * (spring_L - ( ball2.pos.x - ball1.pos.x )) / m1
        ball2_a = spring_k * (spring_L - ( ball2.pos.x - ball1.pos.x )) / m2
        spring.axis = ball1.pos-ball2.pos 
    else :                             #如果沒有，兩球的加速度均為0
        ball1_a = 0
        ball2_a = 0
        spring.axis = vector(-spring_L,0,0)

    t=t+dt
    ball1.pos = ball1.pos+ball1.v*dt  #控制球1的運動
    ball2.pos = ball2.pos+ball2.v*dt  #控制球2的運動

    v1_arrow.pos = ball1.pos #球1速度向量箭頭的起始點在球1上
    v1_arrow.axis = ball1.v  #球1速度向量箭頭的長度與方向等於球1速度

    v2_arrow.pos = ball2.pos #球2速度向量箭頭的起始點在球2上
    v2_arrow.axis = ball2.v  #球1速度向量箭頭的長度與方向等於球2速度

    spring.pos=ball2.pos  #彈簧的起始點位置在球2上
    
    K = 0.5*(m1 * (mag(ball1.v)**2))+0.5*(m2 * (mag(ball2.v)**2))
    if mag(ball2.pos - ball1.pos) >= spring_L :
        U=0
    else :                             #如果沒
        U = 0.5 * spring_k * (spring_L-(ball2.pos.x-ball1.pos.x))**2
    F = K+U

    ball1.v = ball1.v + vector(ball1_a,0,0) *dt  #加速度是向量，所以要用vector(ball1_a,0,0)
    ball2.v = ball2.v + vector(ball2_a,0,0) *dt
    f1_1.plot( pos=(t,K))
    f1_2.plot( pos=(t,U))
    f1_3.plot( pos=(t,F))
    P1 = m1*ball1.v.x
    P2 = m2*ball2.v.x
    P = P1+P2
    f2_1.plot( pos=(t,P1))
    f2_2.plot( pos=(t,P2))
    f2_3.plot( pos=(t,P))