import pgzrun
import random
import sys
import time


WIDTH=1000
HEIGHT=650
zds=5
sd=0
state=0
jfxs=''
gun=Actor('1.png')
zd=Actor('2.png')
z=Actor('3.png')
z1=Actor('5.png')
x=Actor('4.png')
def draw():
    global zds
    global jfxs
    global state
    screen.clear()
    if state == 2:
        time.sleep(6)
        sys.exit(0)
    if state==0:
        zd.draw()
        gun.draw()
        z.draw()
        x.draw()
        z1.draw()

        screen.draw.text(
                "补丁数量:" + str(zds),  # 要显示的文本
                (0, 0),  # 位置 (x, y)
                color="white",  # 文字颜色
                fontsize=30,fontname='puhuiti.ttf')
        screen.draw.text(
                 '消除bug:' + str(score),
                (0, 30),
                color="white",
                fontsize=30,fontname='puhuiti.ttf')
        screen.draw.text(
                'bug等级:' + str(sd * 10 + 1),
                (0, 60),
                color="white",
                fontsize=30,fontname='puhuiti.ttf')
    if state==1:
        screen.clear()
        #print("OK")
        sounds.over.play()
        screen.draw.text(
            "补丁数量:" + str(zds),
            (0, 0),  # 位置 (x, y)
            color="white",
            fontsize=30, fontname='puhuiti.ttf')
        screen.draw.text(
            '消除bug:' + str(score),
            (0, 30),
            color="white",
            fontsize=30, fontname='puhuiti.ttf')
        screen.draw.text(
            'bug等级:' + str(sd * 10 + 1),
            (0, 60),
            color="white",
            fontsize=30, fontname='puhuiti.ttf')
        screen.draw.text(
            '消除bug最高记录:' + jfxs,
            (0, 90),
            color="white",
            fontsize=30, fontname='puhuiti.ttf')

        screen.draw.text(
            '####################################\n'
            '#                                                                                 #\n'
            '#                                  ERROR                                   #\n'
            '#                                                                                 #\n'
            '####################################\n',
            (200, 325),
            color="white",
            fontsize=30, fontname='puhuiti.ttf')
        #print("end")
        state=2





gun.x=500
gun.y=630
x.x=45
x.y=585
zd.pos=gun.pos
score=0

music.play('bgm')
def update():
   global jfxs
   global score
   global sd
   global zds
   global state
   sd=score//10/10


   
   def yd():
      z.y=0 
      z.x=random.randint(20,980)
      z.y+=1
   def yd1():
      z1.y=0
      z1.x=random.randint(20,980)
      z1.y+=2
   gun.x+=5
   zd.angle=gun.angle
   if gun.x>1000:
       if zd.colliderect(gun):
          zd.x=0 
       gun.x=0
       
   if zd.y<0:
       zd.pos=gun.pos
   
   if not zd.colliderect(gun):
       zd.y-=10
   else:
       zd.pos=gun.pos
       if keyboard.space:
           if zds>0:
                zds-=1
                zd.y-=60
            

  
   if not z.y==0:
       z.y+=0.9+sd
   if not z1.y==0:
       z1.y+=1.4+sd
   if z.colliderect(zd):
        yd()
        zds+=1
        if random.randint(1,4)==1:
            zds+=1
        score+=1
        zd.pos=gun.pos
        sounds.bo.play()
        #print(f)
   if z1.colliderect(zd):
       yd1()

       zds+=1
       if random.randint(1,2)==1:
            zds+=1
       score+=2
       zd.pos=gun.pos
       sounds.bo.play()
   if z.colliderect(x) or z1.colliderect(x):

       open_cd = open('bugcd.txt', 'r+')
       jfxs = open_cd.read()
       # print(jfxs)
       if int(jfxs) < score:
           open_cd.close()
           open_cd = open('bugcd.txt', 'w+')
           open_cd.write(str(score))
       open_cd.close()
       open_cd = open('bugcd.txt', 'r')
       jfxs = open_cd.read()
       #print(jfxs)

       music.stop()
       open_cd.close()

       state = 1
  
pgzrun.go()    
    
