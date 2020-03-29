from tkinter import *
import random
import time

v = 0
v_prediction3 = random.randint(1,7)
vit = 0
vit2 = 0

def spawn():
    global collision,direction,vitesse,v,v_prediction,v_prediction2,v_prediction3,x1,y1,x2,y2,x3,y3,x4,y4,empty,scrmeter,vit,vit2
    scrmeter=0
    running = True
    score=0
    ligne0  = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne1  = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne2  = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne3  = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne4  = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne5  = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne6  = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne7  = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne8  = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne9  = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne10 = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne11 = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne12 = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne13 = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne14 = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne15 = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne16 = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne17 = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne18 = [8,0,0,0,0,0,0,0,0,0,0,9]
    ligne19 = [8,0,0,0,0,0,0,0,0,0,0,9]
    lignefin= [8,10,10,10,10,10,10,10,10,10,10,9]
    collision=[ligne0,ligne1,ligne2,ligne3,ligne4,ligne5,ligne6,ligne7,ligne8,ligne9,ligne10,ligne11,ligne12,ligne13,ligne14,ligne15,ligne16,ligne17,ligne18,ligne19,lignefin]
    empty=[0,'temp']
    update()
    
    dico={
    1:{                         # [1][2][3][4]
        0:{
            'bloc1':[ 40,-20],
            'bloc2':[ 20,  0],
            'bloc3':[  0, 20],
            'bloc4':[-20, 40]},
        1:{
            'bloc1':[ 20, 40],
            'bloc2':[  0, 20],
            'bloc3':[-20,  0],
            'bloc4':[-40,-20]},
        2:{
            'bloc1':[-40, 20],
            'bloc2':[-20,  0],
            'bloc3':[  0,-20],
            'bloc4':[ 20,-40]},
        3:{
            'bloc1':[-20,-40],
            'bloc2':[  0,-20],
            'bloc3':[ 20,  0],
            'bloc4':[ 40, 20]},   
        },
    2:{                         # [1]
        0:{                     # [2][3][4]
            'bloc1':[ 40,  0],
            'bloc2':[ 20,-20],
            'bloc3':[  0,  0],
            'bloc4':[-20, 20]},
        1:{
            'bloc1':[  0, 40],
            'bloc2':[ 20, 20],
            'bloc3':[  0,  0],
            'bloc4':[-20,-20]},
        2:{
            'bloc1':[-40,  0],
            'bloc2':[-20, 20],
            'bloc3':[  0,  0],
            'bloc4':[ 20,-20]},
        3:{
            'bloc1':[  0,-40],
            'bloc2':[-20,-20],
            'bloc3':[  0,  0],
            'bloc4':[ 20, 20]},
        },
    3:{                         #       [4]
        0:{                     # [1][2][3]
            'bloc1':[ 20,-20],
            'bloc2':[  0,  0],
            'bloc3':[-20, 20],
            'bloc4':[  0, 40]},
        1:{
            'bloc1':[ 20, 20],
            'bloc2':[  0,  0],
            'bloc3':[-20, -20],
            'bloc4':[-40,  0]},
        2:{
            'bloc1':[-20, 20],
            'bloc2':[  0,  0],
            'bloc3':[ 20,-20],
            'bloc4':[  0,-40]},
        3:{
            'bloc1':[-20,-20],
            'bloc2':[  0,  0],
            'bloc3':[ 20, 20],
            'bloc4':[ 40,  0]},  
        },
    4:{                         # [3][4]
        0:{                     # [1][2]
            'bloc1':[0, 0],
            'bloc2':[0, 0],
            'bloc3':[0, 0],
            'bloc4':[0, 0]},
        1:{
            'bloc1':[0, 0],
            'bloc2':[0, 0],
            'bloc3':[0, 0],
            'bloc4':[0, 0]},
        2:{
            'bloc1':[0, 0],
            'bloc2':[0, 0],
            'bloc3':[0, 0],
            'bloc4':[0, 0]},
        3:{
            'bloc1':[0, 0],
            'bloc2':[0, 0],
            'bloc3':[0, 0],
            'bloc4':[0, 0]},
        },
    5:{                         #    [3][4]
        0:{                     # [1][2]
            'bloc1':[0, -40],
            'bloc2':[-20, -20],
            'bloc3':[0, 0],
            'bloc4':[-20, 20]},
        1:{
            'bloc1':[40, 0],
            'bloc2':[20, -20],
            'bloc3':[0, 0],
            'bloc4':[-20, -20]},
        2:{
            'bloc1':[0, 40],
            'bloc2':[20, 20],
            'bloc3':[0, 0],
            'bloc4':[20, -20]},
        3:{
            'bloc1':[-40, 0],
            'bloc2':[-20, 20],
            'bloc3':[0, 0],
            'bloc4':[20, 20]},   
        },
    6:{                         # [1][2]
        0:{                     #    [3][4]
            'bloc1':[20, -20],
            'bloc2':[0, 0],
            'bloc3':[-20,-20],
            'bloc4':[-40, 0]},
        1:{
            'bloc1':[20, 20],
            'bloc2':[0, 0],
            'bloc3':[20, -20],
            'bloc4':[0, -40]},
        2:{
            'bloc1':[-20, 20],
            'bloc2':[0, 0],
            'bloc3':[20, 20],
            'bloc4':[40, 0]},
        3:{
            'bloc1':[-20, -20],
            'bloc2':[0, 0],
            'bloc3':[-20, 20],
            'bloc4':[0, 40]},   
        }, 
    7:{                         #    [4]
        0:{                     # [1][2][3]
            'bloc1':[20, -20],
            'bloc2':[0, 0],
            'bloc3':[-20, 20],
            'bloc4':[20, 20]},
        1:{
            'bloc1':[20, 20],
            'bloc2':[0, 0],
            'bloc3':[-20, -20],
            'bloc4':[-20, 20]},
        2:{
            'bloc1':[-20, 20],
            'bloc2':[0, 0],
            'bloc3':[20, -20],
            'bloc4':[-20, -20]},
        3:{
            'bloc1':[-20, -20],
            'bloc2':[0, 0],
            'bloc3':[20, 20],
            'bloc4':[20, -20]},   
        },
    }

    while running:
        T,vitesse,direction = 0,False,False
        
        if v == 0:
            v = random.randint(1,7)
            
        if v==1:#I bloc cyan
            grobloc,color='Ibloc','cyan'
            x1,y1,x2,y2,x3,y3,x4,y4=4,0,5,0,6,0,7,0
        if v==2:#J bloc bleu
            grobloc,color='Jbloc','blue'
            x1,y1,x2,y2,x3,y3,x4,y4=4,0,4,1,5,1,6,1
        if v==3:#L bloc orange
            grobloc,color='Lbloc','#D69003'
            x1,y1,x2,y2,x3,y3,x4,y4=4,1,5,1,6,1,6,0
        if v==4:#O bloc jaune
            grobloc,color='Obloc','#F1EF05'
            x1,y1,x2,y2,x3,y3,x4,y4=5,1,6,1,5,0,6,0
        if v==5:#S bloc vert
            grobloc,color='Sbloc','#00ff00'
            x1,y1,x2,y2,x3,y3,x4,y4=4,1,5,1,5,0,6,0
        if v==6:#Z bloc rouge
            grobloc,color='Zbloc','red'
            x1,y1,x2,y2,x3,y3,x4,y4=4,0,5,0,5,1,6,1
        if v==7:#T bloc violet
            grobloc,color='Tbloc','#d000ff'
            x1,y1,x2,y2,x3,y3,x4,y4=4,1,5,1,6,1,5,0
            
        prediction3()
        prediction2()
        prediction()
        
        collision[y1][x1],collision[y2][x2],collision[y3][x3],collision[y4][x4]='temp','temp','temp','temp'
        update()
        if (collision[y1+1][x1] not in empty) or (collision[y2+1][x2] not in empty) or (collision[y3+1][x3] not in empty) or (collision[y4+1][x4] not in empty):
            canvas.delete('all')
            canvas2.delete('all')
            running = False
            canvas.create_text(140,100,fill="white",font="Times 40 italic bold",text="Game Over!")
            canvas.create_text(140,150,fill="white",font="Times 20 italic bold",text="score : "+str(score))
            canvas.create_text(140,270,fill="white",font="Times 20 italic bold",text="Try Again?")
            canvas.create_text(140,300,fill="white",font="Times 20 italic bold",text="Press 'New Game'")
            b1 = Button(fen1, text='New Game',command=spawn)
            b1.pack(pady=25)
        while True:
            #rotation
            if direction:
                collision[y1][x1],collision[y2][x2],collision[y3][x3],collision[y4][x4]=0,0,0,0
                x1rota, y1rota = int(dico[v][T]['bloc1'][0]/20),int(dico[v][T]['bloc1'][1]/20)
                x2rota, y2rota = int(dico[v][T]['bloc2'][0]/20),int(dico[v][T]['bloc2'][1]/20)
                x3rota, y3rota = int(dico[v][T]['bloc3'][0]/20),int(dico[v][T]['bloc3'][1]/20)
                x4rota, y4rota = int(dico[v][T]['bloc4'][0]/20),int(dico[v][T]['bloc4'][1]/20)
                x1,y1,x2,y2,x3,y3,x4,y4=x1+x1rota,y1+y1rota,x2+x2rota,y2+y2rota,x3+x3rota,y3+y3rota,x4+x4rota,y4+y4rota
                #si tourner un objet le fait rentrer dans le mur on le decale pour eviter
                while 8 in [collision[y1][x1],collision[y2][x2],collision[y3][x3],collision[y4][x4]]:
                    x1,x2,x3,x4=x1+1,x2+1,x3+1,x4+1
                while 9 in [collision[y1][x1],collision[y2][x2],collision[y3][x3],collision[y4][x4]]:
                    x1,x2,x3,x4=x1-1,x2-1,x3-1,x4-1
                collision[y1][x1],collision[y2][x2],collision[y3][x3],collision[y4][x4]='temp','temp','temp','temp'
                direction,T=0,T+1
                if T==4:
                    T=0
                
            #après 30 pièces posées le jeu accélère
            if vit == 30 and vitesse!=1 and vit2!=60:
                vitesse = 2
                                
            #après 60 pièces posées le jeu accélère
            if vit2 == 60 and vitesse!=1:
                vitesse = 3
                
            #vitesse accélérée
            if vitesse == 1:
                time.sleep(0.01)
                
            #vitesse de jeu accélèrée 1
            elif vitesse == 2:
                time.sleep(0.3)
                
            #vitesse de jeu accélérée 2
            elif vitesse == 3:
                time.sleep(0.2)
                
            #sinon vitesse normale
            else:
                time.sleep(0.4)
            
            #bloc arrivé en bas: detecter si une ligne est remplie et la supprimer
            if collision[y1+1][x1] not in empty or collision[y2+1][x2] not in empty or collision[y3+1][x3] not in empty or collision[y4+1][x4] not in empty:
                collision[y1][x1],collision[y2][x2],collision[y3][x3],collision[y4][x4]=v,v,v,v
                L=19
                scrmeter = 0
                for loop in range(20):
                    if 0 not in collision[L]:
                        l=L
                        while l!=0:
                            collision[l]=collision[l-1]
                            collision[0]=[8,0,0,0,0,0,0,0,0,0,0,9]
                            l-=1
                        if scrmeter == 0:
                            score+=10               #score 1 ligne
                            print ('1 ligne : +10 points, score =', score)
                           
                        elif scrmeter == 1:
                            score+=40               #score 2 lignes
                            print ('2 lignes : +50 points, score =', score)
                        
                        elif scrmeter == 2:
                            score+=50               #score 3 lignes
                            print ('3 lignes : +100 points, score =', score)
                            
                        elif scrmeter == 3:
                            score+=900              #score 4 lignes / Tetris
                            print ('TETRIS ! +1000 points, score =', score)
                        scrmeter+=1
                        update()
                    else:
                        L-=1
                break
            collision[y1][x1],collision[y2][x2],collision[y3][x3],collision[y4][x4]=0,0,0,0
            y1,y2,y3,y4=y1+1,y2+1,y3+1,y4+1
            collision[y1][x1],collision[y2][x2],collision[y3][x3],collision[y4][x4]='temp','temp','temp','temp'
            update()

        v = v_prediction
        v_prediction = v_prediction2
        v_prediction2 = v_prediction3
        v_prediction3 = random.randint(1,7)
        
        if vit!=30:
            vit+=1
        if vit2!=60:
            vit2+=1
            print ('Tu a posé',vit2,'pièces')
            
            
def update():
    canvas.delete('all')
    couleurinstant=0
    for y in range(21):
        for x in range(12):
            color=collision[y][x]
            if color=='temp':
                color=v
            if color==0:
                color='#2d2d2e'
            if color==1:
                color='cyan'
            if color==2:
                color='blue'
            if color==3:
                color='#D69003' #orange
            if color==4:
                color='#F1EF05' #jaune
            if color==5:
                color='#00ff00' #vert
            if color==6:
                color='red'
            if color==7:
                color='#d000ff' #violet
            if color in [8,9,10]:
                color='#111111'
            x1,y1=x*20+20,y*20+20
            x2,y2=x1+20,y1+20
            canvas.create_rectangle(x1,y1,x2,y2,outline='#2d2d2e',fill=color)
    canvas.update()



def prediction():
    canvas2.delete('all')
    if v_prediction==1: #I bloc cyan
        canvas2.create_rectangle(10,20,90,40,outline='#111111',fill='cyan')
        
    if v_prediction==2:#J bloc bleu
        canvas2.create_polygon(20,20,40,20,40,40,80,40,80,60,20,60,outline='#111111',fill='blue')
        
    if v_prediction==3:#L bloc orange
        canvas2.create_polygon(20,40,60,40,60,20,80,20,80,60,20,60,outline='#111111',fill='#d69003')
        
    if v_prediction==4:#O bloc jaune
        canvas2.create_rectangle(30,20,70,60,outline='#111111',fill='#f1ef05')
        
    if v_prediction==5:#S bloc vert
        canvas2.create_polygon(20,40,40,40,40,20,80,20,80,40,60,40,60,60,20,60,outline='#111111',fill='#00ff00')
        
    if v_prediction==6:#Z bloc rouge
        canvas2.create_polygon(20,20,60,20,60,40,80,40,80,60,40,60,40,40,20,40,outline='#111111',fill='red')
        
    if v_prediction==7:#T bloc violet
        canvas2.create_polygon(20,40,40,40,40,20,60,20,60,40,80,40,80,60,20,60,outline='#111111',fill='#d000ff')
        
    canvas2.create_line(20,40,80,40,fill='#111111')
    if v_prediction in [1,4]:
        canvas2.create_line(30,20,30,60,fill='#111111')
        canvas2.create_line(50,20,50,60,fill='#111111')
        canvas2.create_line(70,20,70,60,fill='#111111')
    if v_prediction in [2,3,5,6,7]:
        canvas2.create_line(40,20,40,60,fill='#111111')
        canvas2.create_line(60,20,60,60,fill='#111111')

def prediction2():
    canvas3.delete('all')
    if v_prediction2==1: #I bloc cyan
        canvas3.create_rectangle(10,20,90,40,outline='#111111',fill='cyan')
        
    if v_prediction2==2:#J bloc bleu
        canvas3.create_polygon(20,20,40,20,40,40,80,40,80,60,20,60,outline='#111111',fill='blue')
        
    if v_prediction2==3:#L bloc orange
        canvas3.create_polygon(20,40,60,40,60,20,80,20,80,60,20,60,outline='#111111',fill='#d69003')
        
    if v_prediction2==4:#O bloc jaune
        canvas3.create_rectangle(30,20,70,60,outline='#111111',fill='#f1ef05')
        
    if v_prediction2==5:#S bloc vert
        canvas3.create_polygon(20,40,40,40,40,20,80,20,80,40,60,40,60,60,20,60,outline='#111111',fill='#00ff00')
        
    if v_prediction2==6:#Z bloc rouge
        canvas3.create_polygon(20,20,60,20,60,40,80,40,80,60,40,60,40,40,20,40,outline='#111111',fill='red')
        
    if v_prediction2==7:#T bloc violet
        canvas3.create_polygon(20,40,40,40,40,20,60,20,60,40,80,40,80,60,20,60,outline='#111111',fill='#d000ff')
        
    canvas3.create_line(20,40,80,40,fill='#111111')
    if v_prediction2 in [1,4]:
        canvas3.create_line(30,20,30,60,fill='#111111')
        canvas3.create_line(50,20,50,60,fill='#111111')
        canvas3.create_line(70,20,70,60,fill='#111111')
    if v_prediction2 in [2,3,5,6,7]:
        canvas3.create_line(40,20,40,60,fill='#111111')
        canvas3.create_line(60,20,60,60,fill='#111111')
        
def prediction3():
    global v_prediction3
    canvas4.delete('all')
    if v_prediction3==1: #I bloc cyan
        canvas4.create_rectangle(10,20,90,40,outline='#111111',fill='cyan')
        
    if v_prediction3==2:#J bloc bleu
        canvas4.create_polygon(20,20,40,20,40,40,80,40,80,60,20,60,outline='#111111',fill='blue')
        
    if v_prediction3==3:#L bloc orange
        canvas4.create_polygon(20,40,60,40,60,20,80,20,80,60,20,60,outline='#111111',fill='#d69003')
        
    if v_prediction3==4:#O bloc jaune
        canvas4.create_rectangle(30,20,70,60,outline='#111111',fill='#f1ef05')
        
    if v_prediction3==5:#S bloc vert
        canvas4.create_polygon(20,40,40,40,40,20,80,20,80,40,60,40,60,60,20,60,outline='#111111',fill='#00ff00')
        
    if v_prediction3==6:#Z bloc rouge
        canvas4.create_polygon(20,20,60,20,60,40,80,40,80,60,40,60,40,40,20,40,outline='#111111',fill='red')
        
    if v_prediction3==7:#T bloc violet
        canvas4.create_polygon(20,40,40,40,40,20,60,20,60,40,80,40,80,60,20,60,outline='#111111',fill='#d000ff')
        
    canvas4.create_line(20,40,80,40,fill='#111111')
    if v_prediction3 in [1,4]:
        canvas4.create_line(30,20,30,60,fill='#111111')
        canvas4.create_line(50,20,50,60,fill='#111111')
        canvas4.create_line(70,20,70,60,fill='#111111')
    if v_prediction3 in [2,3,5,6,7]:
        canvas4.create_line(40,20,40,60,fill='#111111')
        canvas4.create_line(60,20,60,60,fill='#111111')
        


def left(event):
    global collision,direction,vitesse,v,x1,y1,x2,y2,x3,y3,x4,y4,empty
    if collision[y1][x1-1] in empty and collision[y2][x2-1] in empty and collision[y3][x3-1] in empty and collision[y4][x4-1] in empty:
        collision[y1][x1],collision[y2][x2],collision[y3][x3],collision[y4][x4]=0,0,0,0
        x1,x2,x3,x4=x1-1,x2-1,x3-1,x4-1
        collision[y1][x1],collision[y2][x2],collision[y3][x3],collision[y4][x4]='temp','temp','temp','temp'
    update()
    
def right(event):
    global collision,direction,vitesse,v,x1,y1,x2,y2,x3,y3,x4,y4,empty
    if collision[y1][x1+1] in empty and collision[y2][x2+1] in empty and collision[y3][x3+1] in empty and collision[y4][x4+1] in empty:
        collision[y1][x1],collision[y2][x2],collision[y3][x3],collision[y4][x4]=0,0,0,0
        x1,x2,x3,x4=x1+1,x2+1,x3+1,x4+1
        collision[y1][x1],collision[y2][x2],collision[y3][x3],collision[y4][x4]='temp','temp','temp','temp'
    update()
    
def down(event):
    global vitesse
    vitesse = 1
def turnr(event):
    global direction
    direction = True
def quit(event):
    fen1.destroy()
 
 
fen1 = Tk()
fen1.config(bg='#111111')
fen1.title('Tetris')
canvas = Canvas(fen1,height=460,width=280,bg='#111111')
canvas2 = Canvas(fen1,height=80,width=100,bg='#111111')
canvas.pack(side=LEFT)
canvas2.pack()
canvas3 = Canvas(fen1,height=80,width=100,bg='#111111')
canvas.pack(side=LEFT)
canvas3.pack()
canvas4 = Canvas(fen1,height=80,width=100,bg='#111111')
canvas.pack(side=LEFT)
canvas4.pack()
b1 = Button(fen1, text='Start',command=spawn)
b1.pack(pady=50)
canvas.create_text(140,100,fill="white",font="Arial 60 bold",text="Tetris")
canvas.create_text(250,80,fill="white",font="Arial 20 bold",text="®")
canvas.create_text(150,220,fill="white",font="Times 15 italic bold",text="insert 25¢")
canvas.create_text(150,235,fill="white",font="Times 15 italic bold",text="push start")
canvas.create_text(140,450,fill="white",font="Arial 10 bold",text="©     1989     Nintendo")


fen1.bind('<d>', right)
fen1.bind('<q>', left)
fen1.bind('<z>', turnr)
fen1.bind('<s>', down)
fen1.mainloop()