"""
Copyright (c) 2025 rice-1234
Licensed under the MIT License
"""
"""
功能实现：
duration=[1/8]*n   音符演奏时长
ineval=[1/4]*n     间隔时长
bpm=n              演奏速度

依赖：
python
musicpy
timidity
"""

from musicpy import *
from time import sleep

# 输入
a=int(input("基准： "))


so_=('G',a-1)
la_=('A',a-1)
xi_=note('B',a-1)
do=note('C',a)
re=note('D',a)
mi=note('E',a)
fa=note('F',a)
so=note('G',a)
la=note('A',a)
xi=note('B',a)
do2=note('C',a+1)
re2=note('D',a+1)
mi2=note('E',a+1)
fa2=note('F',a+1)
so2=note('G',a+1)
la2=note('A',a+1)
xi2=note('B',a+1)
do3=note('C',a+2)
re3=note('D',a+2)
mi3=note('E',a+2)
do_=note('C',a-1)
so3=note('G',a+2)
la3=note('A',a+2)
xi3=note('B',a+2)
do4=note('C',a+3)

_4=1
_2=1/2
_=1/4
b=1/8
b2=1/16
b4=1/32
b8=1/64

qzy=[la,la,so,la,la,so,                                  # 01
     la,la,so,la,do2,                                    # 02
     la,la,so,la,la,so,                                  # 03
     la,do2,re2,mi2,                                     # 04
     re2,mi2,la,so,la,so,re2,mi2,la,so,la,so,            # 05
     re2,mi2,la,so,la,so,do2,xi,do2,xi,la,so,            # 06
     re2,mi2,la,so,la,so,re2,mi2,la,so,la,so,            # 07
     re2,mi2,so2,do3,mi3,re3,xi2,la2,so2,mi2,do,         # 08
     re2,mi2,la,so,la,so,re2,mi2,la,so,la,so,            # 09
     re2,mi2,la,so,la,so,do2,xi,do2,xi,la,so,            # 10
     do2,la,do2,re2,do2,re2,mi2,re2,mi2,so2,do3,mi2,so2, # 11
     do3,xi2,la2,so2,la2,la2,do3]                        # 12

qzc=[b+b2,b2+b,b2,b+b2,b2+b,b2,
     b+b2,b2+b,b2,_,_,
     b+b2,b2+b,b2,b+b2,b2+b,b2,
     _,_,_,_,
     b,b,b2,b2,b2,b2,b,b,b2,b2,b2,b2,
     b,b,b2,b2,b2,b2,b2,b4,b4,b4,b2,b2,
     b,b,b2,b2,b2,b2,b,b,b2,b2,b2,b2,
     b,b,b,b,b2,b2,b2,b2,b,b2,b2,
     b,b,b2,b2,b2,b2,b,b,b2,b2,b2,b2,
     b,b,b2,b2,b2,b2,b2,b4,b4,b4,b2,b2,
     b,b2,b2,b,b2,b2,b,b2,b2,b2,b2,b2,b2,
     b,b,b,b,_,b,b]

qzj=[b+b2,b2+b,b2+b4,b+b2,b2+b,b2+b4,
     b+b2,b2+b,b2+b4,_,_,
     b+b2,b2+b,b2+b4,b+b2,b2+b,b2+b4,
     _,_,_,_,
     b,b,b2+b8,b2+b8,b2+b8,b2+b8,b,b,b2+b8,b2+b8,b2+b8,b2+b8,
     b,b,b2+b8,b2+b8,b2+b8,b2+b8,b2+b8,b4+b8,b4+b8,b4+b8,b2,b2+b8,
     b,b,b2+b8,b2+b8,b2+b8,b2+b8,b,b,b2+b8,b2+b8,b2+b8,b2+b8,
     b,b,b,b,b2,b2,b2,b2,b,b2,b2,
     b,b,b2+b8,b2+b8,b2+b8,b2+b8,b,b,b2+b8,b2+b8,b2+b8,b2+b8,
     b,b,b2,b2,b2,b2,b2,b4+b8,b4+b8,b4+b8,b2,b2,
     b,b2,b2,b,b2,b2,b,b2,b2,b2,b2,b2,b2,
     b,b,b,b,_,b,b]

zwd=[re2,mi2,la,so,la,so,re2,mi2,la,so,la,so,    #12
     re2,mi2,la,so,la,so,do2,xi,la,so,           #10
     re2,mi2,la,so,la,so,re2,mi2,la,so,la,so,
     re2,mi2,la,so,la,so,do2,xi,do2,xi,la,so,
     re2,mi2,la,so,la,so,re2,mi2,la,so,la,so,
     re2,mi2,la,so,la,so,do2,xi,la,so,
     re2,mi2,so2,la2,so2,mi2,re2,la,do2,re2,mi2,
     la,la,so,la,do,
     la,la,so,la,do2,do2,re2,
     la,la,so,la,so,mi,so,
     la,la,so,la,do2,re2,mi2,
     mi2,re2,mi2,re2,do2,la,
     la,la,la,so,so,la,do2,re2,
     la,la,so,la,so,so,mi,
     la,la,la,so,so,la,do2,re2,
     mi2,do_,re2,mi2,re2,re2,do_,
     do2,xi,la,so,
     so,la,so,mi,re,mi,
     mi,so,la,re2,xi,
     do2,xi,so,la,
     do2,xi,la,so,
     so,la,so,mi,re,mi,so,
     la,la,do_,la,do2,re2,
     xi,la,do2]

zwc=[b,b,b2,b2,b2,b2,b,b,b2,b2,b2,b2,
     b,b,b2,b2,b2,b2,b,b,b,b,
     b,b,b2,b2,b2,b2,b,b,b2,b2,b2,b2,
     b,b,b2,b2,b2,b2,b2,b4,b4,b4,b2,b2,
     b, b, b2, b2, b2, b2, b, b, b2, b2, b2, b2,
     b, b, b2, b2, b2, b2, b, b, b, b,
     b,b2,b2,b2,b2,b2,b2,b,b,b,b,
     b+b2,b2+b,b,_,0,
     _,b,b,b,b,b,b,
     _,b+b2,b2,b,b,b,b,
     _,b+b2,b2,b,b,b,b,
     _,b2,b2,b,_,_,
     b+b2,b2,b,b,b,b,b,b,
     b+b2,b2+b,b,b,b,b,b,
     b+b2,b2,b,b,b,b,b,b,
     b,0,b2,b2,b,_,0,
     _,_,_,_,
     b,b2,b2,b,b,_2,
     b,b,_,_,_,
     _,b,b,_2,
     _,_,_,_,
     b,b2,b2,b,b,_+b,b,
     b,b,b,b,_,_,
     _2+_,b,b
     ]

zwj=[b,b,b2,b2,b2,b2,b,b,b2,b2,b2,b2,               #12
     b,b,b2,b2,b2,b2,b,b,b,b,
     b,b,b2,b2,b2,b2,b,b,b2,b2,b2,b2,
     b,b,b2,b2,b2,b2,b2,b4+b8,b4+b8,b4+b8,b2,b2+b8,
     b, b, b2, b2, b2, b2, b, b, b2, b2, b2, b2+b8,
     b, b, b2, b2, b2, b2, b, b,  b, b+b4,
     b,b2,b2,b2,b2,b2,b2,b,b,b,b+b4,
     b+b2,b2+b,b,_,_,
     _,b,b,b,b,b,b+b4,
     _,b+b2,b2,b,b,b,b+b4,
     _,b+b2,b2,b,b,b,b+b4,
     _,b2+b4,b2+b4,b,_,_,
     b+b2,b2,b,b,b,b,b,b,
     b+b2,b2+b,b+b4,b,b,b,b,
     b+b2,b2,b,b,b,b,b,b,
     b,b,b2+b4,b2+b4,b,_,b+b2+b4,
     _, _, _, _,
     b,b2,b2,b,b,_+b+b2+b4,
     b,b,_,_,_,
     _,b,b,_2,
     _,_,_,_,
     b,b2,b2,b,b,_+b,b,
     b,b,0,b,_,_,
     _2+_,b,b
     ]

cf1=[re2,re2,mi2,mi2,mi2,
     so2,la2,re2,do2,mi2,la,do2,
     re2,re2,mi2,mi2,mi2,
     fa2,mi2,re2,do2,do2,la,do2,
     re2,re2,mi2,mi2,mi2,
     so2,la2,re2,do2,mi2,la,do2,
     fa2,mi2,re2,do2]

cfc1=[b+b2,b+b2,b,_+b,b,
     b,b,b,b,_,b,b,
     b+b2,b+b2,b,_+b,b,
     b,b,b,b,_,b,b,
     b+b2,b+b2,b,_+b,b,
     b,b,b,b,_,b,b,
     _,_,_,_]

cfj1=[b+b2,b+b2,b,_+b,b,
     b,b,b,b,_,b,b,
     b+b2,b+b2,b,_+b,b,
     b,b,b,b,_,b,b,
     b+b2,b+b2,b,_+b,b,
     b,b,b,b,_,b,b,
     _,_,_,_]

xj11=[re2,mi2,xi,so,la,la,do2]
xjc1=[b,b,b,b,_,b,b]
xjj1=[b,b,b,b,_,b,b]

jw1=[mi2,re2,mi2,so2,la2]
jw1c=[b,b,b,b,_2]
jw1j=[b,b,b,b,_2]

jw2=[mi2,re2,mi2,so2,la2,
     la2,la2,la2,la2,la2,la2,la2,so2,mi2,do2,
     re2,re2,re2,re2,re2,re2,re2,do2,la,so,
     la,la,la,la,la,la,la,so,mi,
     re,mi,re,mi,so,la,do2,re2,re2,so2,do3,xi2,mi2,la2,
     xi2,so2,mi2,xi2,xi2,so2,mi2,xi2,so2,mi2,xi2,xi2,so2,mi2,
     do3,la2,fa2,do3,do3,la2,fa2,do3,la2,fa2,do3,do3,la2,fa2,
     do3,so2,mi2,do3,do3,so2,mi2,do3,so2,mi2,do3,do3,so2,mi2,]

jwc2=[b,b,b,b,_2,
      b,b,b,b,b,b,b2,b2,b2,b2,
      b,b,b,b,b,b,b2,b2,b2,b2,
      b,b,b,b,b,b,b2,b2,b,
      b,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b,
      b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,
      b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,
      b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,_4]

jwj2=[b,b,b,b,_2,
      b,b,b,b,b,b,b2,b2,b2,b2,
      b,b,b,b,b,b,b2,b2,b2,b2,
      b,b,b,b,b,b,b2,b2,b,
      b,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b,
      b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,
      b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,
      b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,_4]

mw=[so,la,so,mi,re,mi,
     mi,so,la,re2,xi,
     do2,xi,so,la,
     do2,xi,la,so,
     so,la,so,mi,re,mi,so,
     la,la,do_,la,do2,re2,
     xi,la,do2]

mwc=[ b,b2,b2,b,b,_2,
     b,b,_,_,_,
     _,b,b,_2,
     _,_,_,_,
     b,b2,b2,b,b,_+b,b,
     b,b,b,b,_,_,
     _2+_,b,b]

mwj=[b,b2,b2,b,b,_+b+b2+b4,
     b,b,_,_,_,
     _,b,b,_2,
     _,_,_,_,
     b,b2,b2,b,b,_+b,b,
     b,b,0,b,_,_,
     _2+_,b,b]

mw3=[re2,mi2,la,so,la,so,re2,mi2,la,so,la,so,             # 05
     re2,mi2,la,so,la,so,do2,xi,do2,xi,la,so,             # 06
     re2,mi2,la,so,la,so,re2,mi2,la,so,la,so,             # 07
     re2,mi2,so2,do3,mi3,re3,xi2,la2,so2,mi2,do,          # 08
     re2,mi2,la,so,la,so,re2,mi2,la,so,la,so,             # 09
     re2,mi2,la,so,la,so,do2,xi,do2,xi,la,so,             # 10
     do2,la,do2,re2,do2,re2,mi2,re2,mi2,so2,do3,mi2,so2,  # 11
     do3,xi2,la2,so2,la2,la2,do3,
     re3, mi3, la2,so2,la2,so2,re3, mi3, la2,so2,la2,so2, # 12
     re3,mi3,la2,so2,la2,so2,do3,xi2,la2,so2,             # 10
     re3, mi3, la2,so2,la2,so2,re3, mi3, la2,so2,la2,so2,
     re3,mi3,la2,so2,la2,so2,do3,xi2,do3,xi2,la2,so2,
     re3, mi3, la2,so2,la2,so2,re3, mi3, la2,so2,la2,so2,
     re3,mi3,la2,so2,la2,so2,do3,xi2,la2,so2,
     re3, mi3, so3, la3, so3, mi3, re3, la2, do3, re3, mi3,
     la2, la2, so2, la2, do2,
     la2, la2, so2, la2, do2]

mw3c=[b,b,b2,b2,b2,b2,b,b,b2,b2,b2,b2,
     b,b,b2,b2,b2,b2,b2,b4,b4,b4,b2,b2,
     b,b,b2,b2,b2,b2,b,b,b2,b2,b2,b2,
     b,b,b,b,b2,b2,b2,b2,b,b2,b2,
     b,b,b2,b2,b2,b2,b,b,b2,b2,b2,b2,
     b,b,b2,b2,b2,b2,b2,b4,b4,b4,b2,b2,
     b,b2,b2,b,b2,b2,b,b2,b2,b2,b2,b2,b2,
     b,b,b,b,_,b,b,
     b, b, b2, b2, b2, b2, b, b, b2, b2, b2, b2,
     b, b, b2, b2, b2, b2, b, b, b, b,
     b, b, b2, b2, b2, b2, b, b, b2, b2, b2, b2,
     b, b, b2, b2, b2, b2, b2, b4, b4, b4, b2, b2,
     b, b, b2, b2, b2, b2, b, b, b2, b2, b2, b2,
     b, b, b2, b2, b2, b2, b, b, b, b,
     b, b2, b2, b2, b2, b2, b2, b, b, b, b,
     b + b2, b2 + b, b, _,_,
     b + b2, b2 + b, b, _4,_4]

mw3j=[b, b, b2, b2, b2, b2, b, b, b2, b2, b2, b2,
     b, b, b2, b2, b2, b2, b2, b4+b8, b4+b8, b4+b8, b2, b2,
     b, b, b2, b2, b2, b2, b, b, b2, b2, b2, b2,
     b, b, b, b, b2, b2, b2, b2, b, b2, b2,
     b, b, b2, b2, b2, b2, b, b, b2, b2, b2, b2,
     b, b, b2, b2, b2, b2, b2, b4+b8, b4+b8, b4+b8, b2, b2,
     b, b2, b2, b, b2, b2, b, b2, b2, b2, b2, b2, b2,
     b, b, b, b, _, b, b,
     b, b, b2, b2, b2, b2, b, b, b2, b2, b2, b2,  # 12
     b, b, b2, b2, b2, b2, b, b, b, b,
     b, b, b2, b2, b2, b2, b, b, b2, b2, b2, b2,
     b, b, b2, b2, b2, b2, b2, b4 + b8, b4 + b8, b4 + b8, b2, b2 + b8,
     b, b, b2, b2, b2, b2, b, b, b2, b2, b2, b2 + b8,
     b, b, b2, b2, b2, b2, b, b, b, b + b4,
     b, b2, b2, b2, b2, b2, b2, b, b, b, b + b4,
     b + b2, b2 + b, b, _, _,
     b + b2, b2 + b, b, _4, _4]

qzy2=[]
qzc2=[]
qzj2=[]
qzy2.extend(qzy)
qzc2.extend(qzc)
qzj2.extend(qzj)

for q in range(2):
     qzy2.extend(zwd)
     qzc2.extend(zwc)
     qzj2.extend(zwj)

     for  i in range(2):
          qzy2.extend(cf1)
          qzc2.extend(cfc1)
          qzj2.extend(cfj1)
          if i==1 and q==0:
               qzy2.extend(jw1)
               qzc2.extend(jw1c)
               qzj2.extend(jw1j)
               break
          qzy2.extend(xj11)
          qzc2.extend(xjc1)
          qzj2.extend(xjj1)

qzy2.extend(jw2)
qzc2.extend(jwc2)
qzj2.extend(jwj2)
qzy2.extend(mw)
qzc2.extend(mwc)
qzj2.extend(mwj)

for i in range(2):
     qzy2.extend(cf1)
     qzc2.extend(cfc1)
     qzj2.extend(cfj1)
qzy2.extend(mw3)
qzc2.extend(mw3c)
qzj2.extend(mw3j)

xj1=chord(qzy2,duration=qzc2,interval=qzj2)


play(xj1,bpm=154)

print('原曲:千本桜(千本樱)')
sleep(1)
print('by 一米一饭一\n')
sleep(29.1)
print('大胆不敌 にハイカラ革命')
print('英勇无畏 维新革命\n')
sleep(3.4)
print('磊々落々 反戦国家')
print('光明磊落 反战国家\n')
sleep(3.5)
print('日の丸印の二輪車転がし')
print('乘着有日之丸印记的二轮车\n')
sleep(3.5)
print('悪霊退散 ICBM')
print('恶灵退散 ICBM\n')
sleep(3.2)
print('環状線を走り抜けて')
print('疾行穿过环状线\n')
sleep(3.2)
print('東奔西走 なんのその')
print('东奔西走 在所不辞\n')
sleep(3.2)
print('少年少女 戦国无双')
print('少年少女 战国无双\n')
sleep(3.2)
print('浮世の随に')
print('尘世若梦 唯有随之沉浮\n')
sleep(2.8)
def gc():
     print('千本桜夜ニ纷レ')
     print('千本樱夜中飞散\n')
     sleep(2.8)
     print('君ノ声モ届カナイヨ')
     print('你的声音 亦无法传达\n')
     sleep(2.8)
     print('此処は宴钢の槛')
     print('铁牢之中 宴请众人\n')
     sleep(2.8)
     print('その断头台で见下して')
     print('断头台上俯视众生\n')
     sleep(3.5)
     print('三千世界　常世之闇')
     print('大千世界 桃园之暗\n')
     sleep(3)
     print('叹ク呗モ闻コエナイヨ')
     print('悲叹之曲 亦不可听闻\n')
     sleep(3.2)
gc()
print('青蓝の空　遥か彼方')
print('那青蓝苍穹的遥远彼方\n')
sleep(3.2)
print('その光线铳で打ち抜いて')
print('那就以光线击穿吧\n')
sleep(14.8)
print('百戦錬磨 の見た目は将校')
print('百战磨练 似是将校之人\n')
sleep(3.4)
print('いったりきたりの花魁道中')
print('人来人往的花魁道中\n')
sleep(3.5)
print('アイツもコイツも皆で集まれ')
print('无论是谁全都集结起来\n')
sleep(3.5)
print('聖者の行进')
print('圣者行进\n')
sleep(1)
print('わんっ　つー　さん　しっ')
print('一二三四\n')
sleep(2.2)
print('禅定門を潜り抜けて')
print('从佛门之地穿过\n')
sleep(3.2)
print('安楽浄土厄払い')
print('安乐净土 消灾除厄\n')
sleep(3.2)
print('きっと終幕は大団円')
print('终焉之幕定是大团圆\n')
sleep(3.2)
print('拍手の合間に')
print('在一片掌声之中\n')
sleep(2.8)
gc()
print('希望の丘 遥か彼方')
print('朝着希望之丘遥远彼方\n')
sleep(3.2)
print('その閃光弾を打ち上げろ')
print('就将那闪光弹射入天吧\n')
sleep(15)
print('環状線を走り抜けて')
print('疾行穿过环状线\n')
sleep(3.2)
print('東奔西走 なんのその')
print('东奔西走 在所不辞\n')
sleep(3.2)
print('少年少女 戦国无双')
print('少年少女 战国无双\n')
sleep(3.2)
print('浮世の随に')
print('尘世若梦 唯有随之沉浮\n')
sleep(2.8)
print('千本桜夜ニ纷レ')
print('千本樱夜中飞散\n')
sleep(2.8)
print('君ノ声モ届カナイヨ')
print('你的声音 亦无法传达\n')
sleep(2.8)
print('此処は宴钢の槛')
print('铁牢之中 宴请众人\n')
sleep(2.8)
print('その断頭台を飛び降りて')
print('自那断头台上跳下\n')
sleep(2.8)
print('千本桜夜ニ纷レ')
print('千本樱夜中飞散\n')
sleep(2.8)
print('君が歌い僕は踊る')
print('你放声歌唱 我翩翩起舞\n')
sleep(2.8)
print('此処は宴钢の槛')
print('铁牢之中 宴请众人\n')
sleep(2.8)
print('さあ光線銃を撃ちまくれ')
print('扣下光线枪的扳机吧')
sleep(20)
