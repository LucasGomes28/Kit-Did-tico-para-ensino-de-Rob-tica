from tkinter import*
import math
import serial
from threading import Thread
import time


x=254.2
y=0
z=123
j1=0
j2=86.74
j3=-91.32
j1_ant=0
j2_ant=86.74
j3_ant=-91.32
veloXYZ=0
veloJoints=0
auto_modo = 0
Lim_Garra_aberta = 100
Lim_Garra_fechada = 0

xmenos_click=xmais_click=ymenos_click=ymais_click=zmenos_click=zmais_click=False
j1menos_click=j1mais_click=j2menos_click=j2mais_click=j3menos_click=j3mais_click=False

l1 = 135
l2 = 147
l3 = 100

x_rec=[None]*30
y_rec=[None]*30
z_rec=[None]*30
j1_rec=[None]*30
j2_rec=[None]*30
j3_rec=[None]*30

Saida = ["0","0","0"]
Entrada = ["0","0","0"]
Leitura_Entradas = "0"
criar_prog = 0

def conectar():
    import tkinter
    from tkinter import ttk
     
    def conect():
        global comunicacao
        comunicacao = serial.Serial(comboBox_porta_COM.get(), comboBox_selecao_baudrate.get())
        bt_Conect.configure(text="CONECTADO",background="#028A0F", foreground="white", font=('Calibri', 11, 'bold'))

        janela_conectar.destroy()
    
    def cancelar():
        janela_conectar.destroy()
        
    janela_conectar = tkinter.Tk()
    janela_conectar.title("Conectar")
    janela_conectar.geometry("270x170+200+200")
    
    text=Label(janela_conectar,text="Configuração da Porta Serial:",foreground="#000000")
    text.place(x=45,y=13,width=170,height=15)
    
    text_porta=Label(janela_conectar,text="Porta: ",foreground="#000000")
    text_porta.place(x=60,y=43,width=50,height=15)
    
    text_baud=Label(janela_conectar,text="Baudrate: ",foreground="#000000")
    text_baud.place(x=60,y=78,width=50,height=15)
    
    bt_conect=Button(janela_conectar,text="OK",background="#FFE4B5", command=conect)
    bt_conect.place(x=65,y=120,width=60,height=30)
    
    bt_cancelar=Button(janela_conectar,text="Cancelar",background="#FFE4B5", command=cancelar)
    bt_cancelar.place(x=140,y=120,width=60,height=30)
    
    COM_list=["COM1","COM2","COM3","COM4","COM5","COM6","COM7","COM8","COM9","COM10"]
    comboBox_porta_COM = ttk.Combobox(janela_conectar,values=COM_list, width=8)
    comboBox_porta_COM.place(x=115, y=41)
    comboBox_porta_COM.current(4)
    baud_list=[9600,19200,38400,57600,115200]
    comboBox_selecao_baudrate = ttk.Combobox(janela_conectar,values=baud_list, width=8)
    comboBox_selecao_baudrate.place(x=115, y=75)
    comboBox_selecao_baudrate.current(4)
    valor_modo.set(2)
    
def desconectar():
    comunicacao.close()
    bt_Conect.configure(text="Conectar",background="#98FB98", foreground="black", font=('Calibri', 10))
    
def xmenos_pressed(event):
    global xmenos_click
    xmenos_click=True
                             
def xmenos_released(event):
    global xmenos_click
    xmenos_click=False

def xmais_pressed(event):
    global xmais_click
    xmais_click=True
                             
def xmais_released(event):
    global xmais_click
    xmais_click=False

def ymenos_pressed(event):
    global ymenos_click
    ymenos_click=True
                             
def ymenos_released(event):
    global ymenos_click
    ymenos_click=False
    
def ymais_pressed(event):
    global ymais_click
    ymais_click=True
                             
def ymais_released(event):
    global ymais_click
    ymais_click=False

def zmenos_pressed(event):
    global zmenos_click
    zmenos_click=True
                             
def zmenos_released(event):
    global zmenos_click
    zmenos_click=False
    
def zmais_pressed(event):
    global zmais_click
    zmais_click=True
                             
def zmais_released(event):
    global zmais_click
    zmais_click=False
        
def j1menos_pressed(event):
    global j1menos_click
    j1menos_click=True
                             
def j1menos_released(event):
    global j1menos_click
    j1menos_click=False
    
def j1mais_pressed(event):
    global j1mais_click
    j1mais_click=True
                             
def j1mais_released(event):
    global j1mais_click
    j1mais_click=False

def j2menos_pressed(event):
    global j2menos_click
    j2menos_click=True
                             
def j2menos_released(event):
    global j2menos_click
    j2menos_click=False
    
def j2mais_pressed(event):
    global j2mais_click
    j2mais_click=True
                             
def j2mais_released(event):
    global j2mais_click
    j2mais_click=False
    
def j3menos_pressed(event):
    global j3menos_click
    j3menos_click=True
                             
def j3menos_released(event):
    global j3menos_click
    j3menos_click=False
    
def j3mais_pressed(event):
    global j3mais_click
    j3mais_click=True
                             
def j3mais_released(event):
    global j3mais_click
    j3mais_click=False

def calculo():
    global x
    global y
    global z
    global j1
    global j2
    global j3
    global xmenos_click
    global xmais_click
    global ymenos_click
    global ymais_click
    global zmenos_click
    global zmais_click
    global j1menos_click
    global j1mais_click
    global j2menos_click
    global j2mais_click
    global j3menos_click
    global j3mais_click
    global comunicacao
    global var_j1
    global var_j2
    global var_j3
    global j1i
    global j2i
    global j3i
    global var_x
    global var_y
    global var_z
    global xi
    global yi
    global zi
    global xint
    global yint
    global zint
    global xf
    global yf
    global zf
    global Num_pontos
    global Leitura_Entradas
    global auto_modo
    #auto_modo = 0 --> desligado
    #auto_modo = 1 --> mover joints
    #auto_modo = 2 --> mover linear
    #auto_modo = 3 --> mover circular
    #auto_modo = 4 --> rodar programa
    
    while True:
        if auto_modo == 0:
            if xmenos_click:
                ValorVelocidadeXYZ()
                x=x-(veloXYZ/20)
                xprint=round(x,2)
                lbX.config(text=xprint)
                cinematica()
                
            if xmais_click:
                ValorVelocidadeXYZ()
                x=x+(veloXYZ/20)
                xprint=round(x,2)
                lbX.config(text=xprint)
                cinematica()
                
            if ymenos_click:
                ValorVelocidadeXYZ()
                y=y-(veloXYZ/20)
                yprint=round(y,2)
                lbY.config(text=yprint)
                cinematica()
                
            if ymais_click:
                ValorVelocidadeXYZ()
                y=y+(veloXYZ/20)
                yprint=round(y,2)
                lbY.config(text=yprint)
                cinematica()
                
            if zmenos_click:
                ValorVelocidadeXYZ()
                z=z-(veloXYZ/20)
                zprint=round(z,2)
                lbZ.config(text=zprint)
                cinematica()
                
            if zmais_click:
                ValorVelocidadeXYZ()
                z=z+(veloXYZ/20)
                zprint=round(z,2)
                lbZ.config(text=zprint)
                cinematica()
                
            if j1menos_click:
                ValorVelocidadeJoints()
                j1=j1-(veloJoints/50)
                j1print=round(j1,2)
                lbJ1.config(text=j1print)
                cinematica()            
                
            if j1mais_click:
                ValorVelocidadeJoints()
                j1=j1+(veloJoints/50)
                j1print=round(j1,2)
                lbJ1.config(text=j1print)
                cinematica()
                
            if j2menos_click:
                ValorVelocidadeJoints()
                j2=j2-(veloJoints/50)
                j2print=round(j2,2)
                lbJ2.config(text=j2print)
                cinematica()
                
            if j2mais_click:
                ValorVelocidadeJoints()
                j2=j2+(veloJoints/50)
                j2print=round(j2,2)
                lbJ2.config(text=j2print)
                cinematica()
                
            if j3menos_click:
                ValorVelocidadeJoints()
                j3=j3-(veloJoints/50)
                j3print=round(j3,2)
                lbJ3.config(text=j3print)
                cinematica()
               
            if j3mais_click:
                ValorVelocidadeJoints()
                j3=j3+(veloJoints/50)
                j3print=round(j3,2)
                lbJ3.config(text=j3print)
                cinematica()
            
        if auto_modo == 1:
            # Gerando a trajetória
            g = 0
            while g < (Num_pontos+1):
                j1 = j1i + (var_j1 * g)
                j2 = j2i + (var_j2 * g)
                j3 = j3i + (var_j3 * g)
                j1print=round(j1,2)
                j2print=round(j2,2)
                j3print=round(j3,2)
                lbJ1.config(text=j1print)
                lbJ2.config(text=j2print)
                lbJ3.config(text=j3print)
                cinematica()
                g += 1
            auto_modo = 0
        
        if auto_modo == 2:
            # Gerando a trajetória
            j = 0
            while j < (Num_pontos+1):
                x = xi + (var_x * j)
                y = yi + (var_y * j)
                z = zi + (var_z * j)
                xprint=round(x,2)
                yprint=round(y,2)
                zprint=round(z,2)
                lbX.config(text=xprint)
                lbY.config(text=yprint)
                lbZ.config(text=zprint)
                cinematica()
                j += 1
            auto_modo = 0
            
        if auto_modo == 3:
            # Gerando a trajetória
            u = 0
            k = 0
            while k < (Num_pontos+1):
                u = k/Num_pontos
                x = round((math.pow((1-u),2)*xi+(1-u)*(2*u)*xint+math.pow(u,2)*xf),2)
                y = round((math.pow((1-u),2)*yi+(1-u)*(2*u)*yint+math.pow(u,2)*yf),2)
                z = round((math.pow((1-u),2)*zi+(1-u)*(2*u)*zint+math.pow(u,2)*zf),2)
                xprint=round(x,2)
                yprint=round(y,2)
                zprint=round(z,2)
                lbX.config(text=xprint)
                lbY.config(text=yprint)
                lbZ.config(text=zprint)
                cinematica()
                k += 1
            auto_modo = 0
        
        if auto_modo == 4:
            prog_finalizado = 0
            Modo_Programacao = 0
            #Modo_Programacao = 1 --> Modo Multiplic
            #Modo_Programacao = 2 --> Programação ACL
            #Modo_Programacao = 3 --> G code
            
            with open(nomeProg + '.txt','r') as arquivo:
                while (prog_finalizado == 0):
                    codigo=arquivo.readline()
                    print(codigo)
                    if codigo == 'Multiplic Mode\n':
                        Modo_Programacao = 1
                    if codigo[0:7] == 'Program':
                        Modo_Programacao = 2
                    if codigo[0:6] == 'G code':
                        Modo_Programacao = 3
                        
                    if Modo_Programacao == 1:
                        if codigo[0:7] == 'wait in':
                            entrada = codigo[8]
                            estado = codigo[13]
                            
                            for s in range(0,100):
                                comunicacao.write(codigo_anterior.encode())
                                leitura_serial = comunicacao.readline()
                            
                            Entrada[0] = str(leitura_serial[0] - 48)
                            Entrada[1] = str(leitura_serial[1] - 48)
                            Entrada[2] = str(leitura_serial[2] - 48)

                            if estado == "1":
                                while Entrada[int(entrada)-1] != "1":
                                    comunicacao.write(codigo_anterior.encode())
                                    leitura_serial = comunicacao.readline()
                                    Entrada[int(entrada)-1] = str(leitura_serial[int(entrada)-1] - 48)
                                
                            if estado == "0":
                                while Entrada[int(entrada)-1] != "0":
                                    comunicacao.write(codigo_anterior.encode())
                                    leitura_serial = comunicacao.readline()
                                    Entrada[int(entrada)-1] = str(leitura_serial[int(entrada)-1] - 48)
                           
                        else:
                            comunicacao.write(codigo.encode())
                        
                    if Modo_Programacao == 2:
                        if codigo == 'open\n':
                            posicaoGarra.set(Lim_Garra_aberta)

                        if codigo == 'close\n':
                            posicaoGarra.set(Lim_Garra_fechada)
                        
                        if codigo[0:5] == 'delay':
                            #Obtendo o tempo desejado removendo caracteres indesejados
                            tempo = codigo
                            disallowed_characters = "delay \n"
                            for character in disallowed_characters:
                                tempo = tempo.replace(character, "")
                            
                            tempo = int(tempo)/100
                            time.sleep(tempo)
                        
                        if codigo[0:6] == 'speed ':
                            #Obtendo o tempo desejado removendo caracteres indesejados
                            velocidade = codigo
                            disallowed_characters = "speed \n"
                            for character in disallowed_characters:
                                velocidade = velocidade.replace(character, "")
                            
                            velocidade = int(velocidade)/10
                            velocidadeJoints.set(velocidade)
                            
                        if codigo[0:6] == 'speedl':
                            #Obtendo o tempo desejado removendo caracteres indesejados
                            velocidade = codigo
                            disallowed_characters = "speedl \n"
                            for character in disallowed_characters:
                                velocidade = velocidade.replace(character, "")
                            
                            velocidade = int(velocidade)/10
                            velocidadeXYZ.set(velocidade)
                        
                        if codigo[0:7] == 'set out':
                            saida = codigo[8]
                            estado = codigo[13]
                            
                            Saida[int(saida)-1] = int(estado)
                            cinematica()
                            
                        if codigo[0:7] == 'wait in':
                            entrada = codigo[8]
                            estado = codigo[13]
                            
                            Leitura_Entradas = "1"            
                            cinematica()
                            leitura_serial = comunicacao.readline()
                            Entrada[0] = str(leitura_serial[0] - 48)
                            Entrada[1] = str(leitura_serial[1] - 48)
                            Entrada[2] = str(leitura_serial[2] - 48)

                            if estado == "1":
                                while Entrada[int(entrada)-1] != "1":
                                    cinematica()
                                    leitura_serial = comunicacao.readline()
                                    Entrada[int(entrada)-1] = str(leitura_serial[int(entrada)-1] - 48)
                                
                            if estado == "0":
                                while Entrada[int(entrada)-1] != "0":
                                    cinematica()
                                    leitura_serial = comunicacao.readline()
                                    Entrada[int(entrada)-1] = str(leitura_serial[int(entrada)-1] - 48)
                            Leitura_Entradas = "0" 
                        
                        if codigo[0:5] == 'movel':
                            #Obtendo a posição desejada removendo caracteres indesejados
                            posicao = codigo
                            disallowed_characters = "movel pos[]\n"
                            for character in disallowed_characters:
                                posicao = posicao.replace(character, "")
                            
                            posicao = int(posicao)
                            incremento = velocidadeXYZ.get()/20
        
                            # Posição inicial
                            xi = x
                            yi = y
                            zi = z

                            # Posição final
                            xf = x_rec[posicao]
                            yf = y_rec[posicao]
                            zf = z_rec[posicao]


                            # Encontrando a distância entre os dois pontos
                            dist = math.sqrt(math.pow(xf-xi,2)+math.pow(yf-yi,2)+math.pow(zf-zi,2))

                            # Encontrando o número de pontos a serem gerados
                            Num_pontos = dist/incremento
                            Num_pontos = round(Num_pontos,0)
                            Num_pontos = int(Num_pontos)

                            # Encontrando a variação para cada eixo (x, y e z)
                            var_x = (xf-xi)/Num_pontos
                            var_y = (yf-yi)/Num_pontos
                            var_z = (zf-zi)/Num_pontos
                            
                            # Gerando a trajetória
                            j = 0
                            auto_modo = 2
                            while j < (Num_pontos+1):
                                x = xi + (var_x * j)
                                y = yi + (var_y * j)
                                z = zi + (var_z * j)
                                xprint=round(x,2)
                                yprint=round(y,2)
                                zprint=round(z,2)
                                lbX.config(text=xprint)
                                lbY.config(text=yprint)
                                lbZ.config(text=zprint)
                                cinematica()
                                j += 1
                            auto_modo = 4

                        if codigo[0:5] == 'move ':
                            #Obtendo a posição desejada removendo caracteres indesejados
                            posicao = codigo
                            disallowed_characters = "move pos[]\n"
                            for character in disallowed_characters:
                                posicao = posicao.replace(character, "")
                            
                            posicao = int(posicao)
                            incremento = velocidadeJoints.get()/50
        
                            # Posição inicial
                            j1i = j1
                            j2i = j2
                            j3i = j3

                            # Posição final
                            j1f = j1_rec[posicao]
                            j2f = j2_rec[posicao]
                            j3f = j3_rec[posicao]


                           # Encontrando o número de pontos a serem gerados

                            angulo = max(abs(j1f-j1i),abs(j2f-j2i),abs(j3f-j3i))
                            Num_pontos = angulo/incremento
                            Num_pontos = round(Num_pontos,0)
                            Num_pontos = int(Num_pontos)

                            # Encontrando a variação para cada junta (j1, j2 e j3)

                            var_j1 = (j1f-j1i)/Num_pontos
                            var_j2 = (j2f-j2i)/Num_pontos
                            var_j3 = (j3f-j3i)/Num_pontos

                            # Gerando a trajetória
                            auto_modo = 1
                            g = 0
                            while g < (Num_pontos+1):
                                j1 = j1i + (var_j1 * g)
                                j2 = j2i + (var_j2 * g)
                                j3 = j3i + (var_j3 * g)
                                j1print=round(j1,2)
                                j2print=round(j2,2)
                                j3print=round(j3,2)
                                lbJ1.config(text=j1print)
                                lbJ2.config(text=j2print)
                                lbJ3.config(text=j3print)
                                cinematica()
                                g += 1
                            auto_modo = 4
                            
                        if codigo[0:5] == 'movec':
                            #Obtendo a posição desejada removendo caracteres indesejados
                            posicao_final = codigo[5:13]
                            posicao_int = codigo[13:len(codigo)]
                            disallowed_characters = "movec pos[]\n"
                            for character in disallowed_characters:
                                posicao_final = posicao_final.replace(character, "")
                                posicao_int = posicao_int.replace(character, "")
                            
                            posicao_final = int(posicao_final)
                            posicao_int = int(posicao_int)
                            incremento = velocidadeXYZ.get()/20
        
                            # Posição inicial
                            xi = x
                            yi = y
                            zi = z
                            
                            # Posição intermediária
                            xint = x_rec[posicao_int]
                            yint = y_rec[posicao_int]
                            zint = z_rec[posicao_int]
                            yint = yint*2

                            # Posição final
                            xf = x_rec[posicao_final]
                            yf = y_rec[posicao_final]
                            zf = z_rec[posicao_final]


                           # Encontrando a distância entre os pontos
                            dist = (math.sqrt(math.pow(xf-xint,2)+math.pow(yf-yint,2)+math.pow(zf-zint,2)))+(math.sqrt(math.pow(xint-xi,2)+math.pow(yint-yi,2)+math.pow(zint-zi,2)))

                            # Encontrando o número de pontos a serem gerados
                            Num_pontos = dist/incremento
                            Num_pontos = round(Num_pontos,0)
                            Num_pontos = int(Num_pontos)

                            
                            # Gerando a trajetória
                            u = 0
                            k = 0
                            auto_modo = 3
                            while k < (Num_pontos+1):
                                u = k/Num_pontos
                                x = round((math.pow((1-u),2)*xi+(1-u)*(2*u)*xint+math.pow(u,2)*xf),2)
                                y = round((math.pow((1-u),2)*yi+(1-u)*(2*u)*yint+math.pow(u,2)*yf),2)
                                z = round((math.pow((1-u),2)*zi+(1-u)*(2*u)*zint+math.pow(u,2)*zf),2)
                                xprint=round(x,2)
                                yprint=round(y,2)
                                zprint=round(z,2)
                                lbX.config(text=xprint)
                                lbY.config(text=yprint)
                                lbZ.config(text=zprint)
                                cinematica()
                                k += 1
                            auto_modo = 4
                        
                    if codigo == 'end':
                        prog_finalizado = 1
                        
                    codigo_anterior = codigo
            auto_modo = 0
            
def Garra(self):
    if valor_modo.get() == 1 or valor_modo.get() == 2:
        cinematica()
        
def Abrir_Garra():
    global Lim_Garra_aberta
    posicaoGarra.set(Lim_Garra_aberta)

def Fechar_Garra():
    global Lim_Garra_fechada
    posicaoGarra.set(Lim_Garra_fechada)
    
def Limites_Garra():
    import tkinter
    from tkinter import ttk
      
    def confirma():
        global Lim_Garra_aberta
        global Lim_Garra_fechada
        
        Lim_Garra_aberta = int(Limite_maximo.get("1.0","end-1c"))
        Lim_Garra_fechada = int(Limite_minimo.get("1.0","end-1c"))
        
        if Lim_Garra_aberta > 100:
            Lim_Garra_aberta = 100
        if Lim_Garra_fechada < 0:
            Lim_Garra_fechada = 0
            
        posicaoGarra.configure(from_=Lim_Garra_fechada,to=Lim_Garra_aberta)

        janela_limites_garra.destroy()
    
    def cancelar():
        janela_limites_garra.destroy()
        
    janela_limites_garra = tkinter.Tk()
    janela_limites_garra.title("Ajustar Limites")
    janela_limites_garra.geometry("270x170+200+200")
    
    text=Label(janela_limites_garra,text="Informe os valores para os limites da Garra:",foreground="#000000")
    text.place(x=0,y=13,width=270,height=15)
    
    text_max=Label(janela_limites_garra,text="Máximo: ",foreground="#000000")
    text_max.place(x=80,y=48,width=50,height=15)
    
    text_min=Label(janela_limites_garra,text="Mínimo: ",foreground="#000000")
    text_min.place(x=80,y=83,width=50,height=15)
    
    bt_confirma=Button(janela_limites_garra,text="OK",background="#FFE4B5", command=confirma)
    bt_confirma.place(x=65,y=120,width=60,height=30)
    
    bt_cancelar=Button(janela_limites_garra,text="Cancelar",background="#FFE4B5", command=cancelar)
    bt_cancelar.place(x=140,y=120,width=60,height=30)
    
    Limite_maximo=Text(janela_limites_garra,width=7,height=1)
    Limite_maximo.insert("1.0","100")
    Limite_maximo.place(x=135,y=45)
    
    Limite_minimo=Text(janela_limites_garra,width=7,height=1)
    Limite_minimo.insert("1.0","0")
    Limite_minimo.place(x=135,y=80)

def ValorVelocidadeXYZ():
    global veloXYZ
    global valor_modo
    if valor_modo.get() == 1:
        veloXYZ=velocidadeXYZ.get()
    elif valor_modo.get() == 2:
        veloXYZ=0
    else:
        veloXYZ=0
               
    
def ValorVelocidadeJoints():
    global veloJoints
    global valor_modo
    if valor_modo.get() == 2:
        veloJoints=velocidadeJoints.get()
    elif valor_modo.get() == 1:
        veloJoints=0
    else:
        veloJoints=0
        
def Salvar_Programa():
    import tkinter
    from tkinter import ttk
    
    janela_salvar_prog = tkinter.Tk()
    janela_salvar_prog.title("Salvar Programa")
    janela_salvar_prog.geometry("390x170+200+200")
    
    def salvarprog():
        global x_rec
        global y_rec
        global z_rec
        global j1_rec
        global j2_rec
        global j3_rec
        
        nome=str(NomeProg.get("1.0","end-1c"))
       
        x_txt=str(x_rec)
        y_txt=str(y_rec)
        z_txt=str(z_rec)
        j1_txt=str(j1_rec)
        j2_txt=str(j2_rec)
        j3_txt=str(j3_rec)
        
        with open(nome + '.txt','w') as arquivo:
            arquivo.write(x_txt + '\n')
            arquivo.write(y_txt + '\n')
            arquivo.write(z_txt + '\n')
            arquivo.write(j1_txt + '\n')
            arquivo.write(j2_txt + '\n')
            arquivo.write(j3_txt + '\n')
        
        janela_salvar_prog.destroy()
                
    def cancelarprog():
        janela_salvar_prog.destroy()
    
    text_salvar_prog=Label(janela_salvar_prog,text="Nome do programa: ",foreground="#000000")
    text_salvar_prog.place(x=1,y=30,width=170,height=15)
    
    NomeProg=Text(janela_salvar_prog,width=40,height=1)
    NomeProg.place(x=30,y=55)
    
    bt_salvarprog=Button(janela_salvar_prog,text="Salvar",background="#FFE4B5", command=salvarprog)
    bt_salvarprog.place(x=115,y=110,width=60,height=30)
    
    bt_cancelarprog=Button(janela_salvar_prog,text="Cancelar",background="#FFE4B5", command=cancelarprog)
    bt_cancelarprog.place(x=200,y=110,width=60,height=30)
    
def Abrir_Programa():
    import tkinter
    from tkinter import ttk    
    janela_abrir_prog = tkinter.Tk()
    janela_abrir_prog.title("Abrir Programa")
    janela_abrir_prog.geometry("390x170+200+200")
    
    def abrirprog():
        global x_rec
        global y_rec
        global z_rec
        global j1_rec
        global j2_rec
        global j3_rec
        
        nome=str(NomeProg.get("1.0","end-1c"))
        
        with open(nome + '.txt','r') as arquivo:  
            x_txt=arquivo.readline()
            y_txt=arquivo.readline()
            z_txt=arquivo.readline()
            j1_txt=arquivo.readline()
            j2_txt=arquivo.readline()
            j3_txt=arquivo.readline()
        
        #Removendo Caracteres Indesejados
        disallowed_characters = "[ ]\n"
        for character in disallowed_characters:
            x_txt = x_txt.replace(character, "")
            y_txt = y_txt.replace(character, "")
            z_txt = z_txt.replace(character, "")
            j1_txt = j1_txt.replace(character, "")
            j2_txt = j2_txt.replace(character, "")
            j3_txt = j3_txt.replace(character, "")

        #Separando as posições no vetor de posições    
        x_rec=x_txt.split(',')             
        y_rec=y_txt.split(',') 
        z_rec=z_txt.split(',') 
        j1_rec=j1_txt.split(',') 
        j2_rec=j2_txt.split(',') 
        j3_rec=j3_txt.split(',') 
        
        #Convertendo strings para float
        for g in range(0,30):
            if x_rec[g] == 'None':
                x_rec[g] = None
            else:
                x_rec[g] = float(x_rec[g])
                
            if y_rec[g] == 'None':
                y_rec[g] = None
            else:
                y_rec[g] = float(y_rec[g])
            
            if z_rec[g] == 'None':
                z_rec[g] = None
            else:
                z_rec[g] = float(z_rec[g])
                
            if j1_rec[g] == 'None':
                j1_rec[g] = None
            else:
                j1_rec[g] = float(j1_rec[g])
            
            if j2_rec[g] == 'None':
                j2_rec[g] = None
            else:
                j2_rec[g] = float(j2_rec[g])
            
            if j3_rec[g] == 'None':
                j3_rec[g] = None
            else:
                j3_rec[g] = float(j3_rec[g])
                
        print(x_rec)
        print(y_rec)
        print(z_rec)
        print(j1_rec)
        print(j2_rec)
        print(j3_rec)
        
        janela_abrir_prog.destroy()
                
    def cancelarabrir():
        janela_abrir_prog.destroy()
     
    text_abrir_prog=Label(janela_abrir_prog,text="Nome do programa: ",foreground="#000000")
    text_abrir_prog.place(x=1,y=30,width=170,height=15)
    
    NomeProg=Text(janela_abrir_prog,width=40,height=1)
    NomeProg.place(x=30,y=55)
    
    bt_abrirprog=Button(janela_abrir_prog,text="Abrir",background="#FFE4B5", command=abrirprog)
    bt_abrirprog.place(x=115,y=110,width=60,height=30)
    
    bt_cancelarabrir=Button(janela_abrir_prog,text="Cancelar",background="#FFE4B5", command=cancelarabrir)
    bt_cancelarabrir.place(x=200,y=110,width=60,height=30)

def Criar_Programa():
    import tkinter
    from tkinter import ttk
    global nomeProg
    global criar_prog
    
    if criar_prog == 1:
        criar_prog = 0
        with open(nomeProg + '.txt','a') as arquivo:
            arquivo.write('end')
        bt_Criar_Prog.configure(text="Criar Programa",background="#DCDCDC", foreground="black", font=('Calibri', 10))
    else:
        janela_salvar_prog = tkinter.Tk()
        janela_salvar_prog.title("Criar Programa")
        janela_salvar_prog.geometry("390x170+200+200")
        
        def salvarprog():
            global nomeProg
            global criar_prog
            
            criar_prog = 1
            nomeProg=str(NomeProg.get("1.0","end-1c"))
            with open(nomeProg + '.txt','a') as arquivo:
                    arquivo.write('Multiplic Mode\n')
            bt_Criar_Prog.configure(text="Finalizar",background="red", foreground="white", font=('Calibri', 11, 'bold'))
            janela_salvar_prog.destroy()
                    
        def cancelarprog():
            janela_salvar_prog.destroy()
        
        text_salvar_prog=Label(janela_salvar_prog,text="Nome do programa: ",foreground="#000000")
        text_salvar_prog.place(x=1,y=30,width=170,height=15)
        
        NomeProg=Text(janela_salvar_prog,width=40,height=1)
        NomeProg.place(x=30,y=55)
        
        bt_salvarprog=Button(janela_salvar_prog,text="Salvar",background="#FFE4B5", command=salvarprog)
        bt_salvarprog.place(x=115,y=110,width=60,height=30)
        
        bt_cancelarprog=Button(janela_salvar_prog,text="Cancelar",background="#FFE4B5", command=cancelarprog)
        bt_cancelarprog.place(x=200,y=110,width=60,height=30)


def Executar_Programa():
    import tkinter
    from tkinter import ttk    
    janela_executar_prog = tkinter.Tk()
    janela_executar_prog.title("Executar Programa")
    janela_executar_prog.geometry("390x170+200+200")
    
    def abrirprog():
        global auto_modo
        global nomeProg
        
        nomeProg=str(NomeProg.get("1.0","end-1c"))
        auto_modo = 4 
        janela_executar_prog.destroy()
                
    def cancelarabrir():
        janela_executar_prog.destroy()
     
    text_abrir_prog=Label(janela_executar_prog,text="Nome do programa: ",foreground="#000000")
    text_abrir_prog.place(x=1,y=30,width=170,height=15)
    
    NomeProg=Text(janela_executar_prog,width=40,height=1)
    NomeProg.place(x=30,y=55)
    
    bt_abrirprog=Button(janela_executar_prog,text="Abrir",background="#FFE4B5", command=abrirprog)
    bt_abrirprog.place(x=115,y=110,width=60,height=30)
    
    bt_cancelarabrir=Button(janela_executar_prog,text="Cancelar",background="#FFE4B5", command=cancelarabrir)
    bt_cancelarabrir.place(x=200,y=110,width=60,height=30)
    
def Setar_Saida():
    import tkinter
    from tkinter import ttk
    
    
    def Atualizar_Saidas():
        global Saida
        if comboBox_selecao_pos1.get() == "On":
            Saida[0] = 1
        elif comboBox_selecao_pos1.get() == "Off":
            Saida[0] = 0
        
        if comboBox_selecao_pos2.get() == "On":
            Saida[1] = 1
        elif comboBox_selecao_pos2.get() == "Off":
            Saida[1] = 0

        if comboBox_selecao_pos3.get() == "On":
            Saida[2] = 1
        elif comboBox_selecao_pos3.get() == "Off":
            Saida[2] = 0
               
        cinematica()
        
        janela_Setar_Saidas.destroy()
    
    def cancelar():
        janela_Setar_Saidas.destroy()
        
    janela_Setar_Saidas = tkinter.Tk()
    janela_Setar_Saidas.title("Definir Saídas")
    #Dimensões da janela
    #LxA+E+T
    #Largura x Altura + Distância à esquerda + Distância do topo
    janela_Setar_Saidas.geometry("270x170+200+200")
    
    text_salvar_pos=Label(janela_Setar_Saidas,text="Ligar/Desligar Saídas:",foreground="#000000")
    text_salvar_pos.place(x=0,y=8,width=170,height=15)
    
    text_num_pos1=Label(janela_Setar_Saidas,text="Saída 1: ",foreground="#000000")
    text_num_pos1.place(x=85,y=37,width=50,height=15)

    text_num_pos2=Label(janela_Setar_Saidas,text="Saída 2: ",foreground="#000000")
    text_num_pos2.place(x=85,y=62,width=50,height=15)

    text_num_pos3=Label(janela_Setar_Saidas,text="Saída 3: ",foreground="#000000")
    text_num_pos3.place(x=85,y=87,width=50,height=15)
    
    bt_salvar=Button(janela_Setar_Saidas,text="OK",background="#FFE4B5", command=Atualizar_Saidas)
    bt_salvar.place(x=65,y=120,width=60,height=30)
    
    bt_cancelar=Button(janela_Setar_Saidas,text="Cancelar",background="#FFE4B5", command=cancelar)
    bt_cancelar.place(x=140,y=120,width=60,height=30)
    
    pos_list=["Off","On"]
    comboBox_selecao_pos1 = ttk.Combobox(janela_Setar_Saidas,values=pos_list)
    comboBox_selecao_pos1.place(x=140, y=35, width=50)
    comboBox_selecao_pos1.current(0)
    
    comboBox_selecao_pos2 = ttk.Combobox(janela_Setar_Saidas,values=pos_list)
    comboBox_selecao_pos2.place(x=140, y=60, width=50)
    comboBox_selecao_pos2.current(0)
    
    comboBox_selecao_pos3 = ttk.Combobox(janela_Setar_Saidas,values=pos_list)
    comboBox_selecao_pos3.place(x=140, y=85, width=50)
    comboBox_selecao_pos3.current(0)
    
    janela_Setar_Saidas.mainloop()

def Aguardar_Entrada():
    import tkinter
    from tkinter import ttk
    
    
    def Atualizar_Entradas():
        global Leitura_Entradas
        global criar_prog
        global nomeProg
        
        Leitura_Entradas = "1"            
        cinematica()
        leitura_serial = comunicacao.readline()
        Entrada[0] = str(leitura_serial[0] - 48)
        Entrada[1] = str(leitura_serial[1] - 48)
        Entrada[2] = str(leitura_serial[2] - 48)

        if comboBox_selecao_pos.get() == "On":
            while Entrada[int(comboBox_selecao_entrada.get())-1] != "1":
                Leitura_Entradas = "1"            
                cinematica()
                leitura_serial = comunicacao.readline()
                Entrada[int(comboBox_selecao_entrada.get())-1] = str(leitura_serial[int(comboBox_selecao_entrada.get())-1] - 48)
            if criar_prog == 1:
                with open(nomeProg + '.txt','a') as arquivo:
                    arquivo.write('wait in['+str(comboBox_selecao_entrada.get())+'] = 1\n')
        if comboBox_selecao_pos.get() == "Off":
            while Entrada[int(comboBox_selecao_entrada.get())-1] != "0":
                Leitura_Entradas = "1"            
                cinematica()
                leitura_serial = comunicacao.readline()
                Entrada[int(comboBox_selecao_entrada.get())-1] = str(leitura_serial[int(comboBox_selecao_entrada.get())-1] - 48)
            if criar_prog == 1:
                with open(nomeProg + '.txt','a') as arquivo:
                    arquivo.write('wait in['+str(comboBox_selecao_entrada.get())+'] = 0\n')
            
        Leitura_Entradas = "0"   
        
        janela_Aguardar_Entrada.destroy()
    
    def cancelar():
        janela_Aguardar_Entrada.destroy()
        
    janela_Aguardar_Entrada = tkinter.Tk()
    janela_Aguardar_Entrada.title("Aguardar Entrada")
    #Dimensões da janela
    #LxA+E+T
    #Largura x Altura + Distância à esquerda + Distância do topo
    janela_Aguardar_Entrada.geometry("270x170+200+200")
    
    text_salvar_pos=Label(janela_Aguardar_Entrada,text="Aguardar Entrada",foreground="#000000")
    text_salvar_pos.place(x=0,y=52,width=170,height=15)
    
    text_num_pos1=Label(janela_Aguardar_Entrada,text=" = ",foreground="#000000")
    text_num_pos1.place(x=163,y=52,width=50,height=15)

    
    bt_salvar=Button(janela_Aguardar_Entrada,text="OK",background="#FFE4B5", command=Atualizar_Entradas)
    bt_salvar.place(x=65,y=120,width=60,height=30)
    
    bt_cancelar=Button(janela_Aguardar_Entrada,text="Cancelar",background="#FFE4B5", command=cancelar)
    bt_cancelar.place(x=140,y=120,width=60,height=30)
    
    pos_list=[1,2,3]
    pos_list2=["On","Off"]
    comboBox_selecao_entrada = ttk.Combobox(janela_Aguardar_Entrada,values=pos_list)
    comboBox_selecao_entrada.place(x=140, y=50, width=35)
    comboBox_selecao_entrada.current(0)
    
    comboBox_selecao_pos = ttk.Combobox(janela_Aguardar_Entrada,values=pos_list2)
    comboBox_selecao_pos.place(x=200, y=50, width=40)
    comboBox_selecao_pos.current(0)
    
    janela_Aguardar_Entrada.mainloop()
    
def Gravar():
    import tkinter
    from tkinter import ttk
    
    def callbackFunc(event):
        global pos_selecionada
        pos_selecionada = comboBox_selecao_pos.get()
     
    def Gravar():
        global x
        global y
        global z
        global j1
        global j2
        global j3
        global x_rec
        global y_rec
        global z_rec
        global j1_rec
        global j2_rec
        global j3_rec
        posicao=int(float(comboBox_selecao_pos.get()))
               
        x_rec[posicao]=round(x,2)
        y_rec[posicao]=round(y,2)
        z_rec[posicao]=round(z,2)
        j1_rec[posicao]=round(j1,2)
        j2_rec[posicao]=round(j2,2)
        j3_rec[posicao]=round(j3,2)
        
        print(x_rec)
        print(y_rec)
        print(z_rec)
        print(j1_rec)
        print(j2_rec)
        print(j3_rec)
        
        janela_salvar_pos.destroy()
    
    def cancelar():
        janela_salvar_pos.destroy()
        
    janela_salvar_pos = tkinter.Tk()
    janela_salvar_pos.title("Salvar Posição")
    #Dimensões da janela
    #LxA+E+T
    #Largura x Altura + Distância à esquerda + Distância do topo
    janela_salvar_pos.geometry("270x170+200+200")
    
    text_salvar_pos=Label(janela_salvar_pos,text="Deseja salvar em qual posição?",foreground="#000000")
    text_salvar_pos.place(x=45,y=20,width=170,height=15)
    
    text_num_pos=Label(janela_salvar_pos,text="Posição: ",foreground="#000000")
    text_num_pos.place(x=45,y=70,width=50,height=15)
    
    bt_salvar=Button(janela_salvar_pos,text="Salvar",background="#FFE4B5", command=Gravar)
    bt_salvar.place(x=65,y=120,width=60,height=30)
    
    bt_cancelar=Button(janela_salvar_pos,text="Cancelar",background="#FFE4B5", command=cancelar)
    bt_cancelar.place(x=140,y=120,width=60,height=30)
    
    pos_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    comboBox_selecao_pos = ttk.Combobox(janela_salvar_pos,values=pos_list)
    comboBox_selecao_pos.grid(column=0, row=1,)
    comboBox_selecao_pos.pack(padx=100, pady=67)
    comboBox_selecao_pos.current(0)
    comboBox_selecao_pos.bind("<<ComboboxSelected>>", callbackFunc)
    
    janela_salvar_pos.mainloop()        

def Mover_Linear():     
    import tkinter
    from tkinter import ttk
    
    def callbackFunc(event):
        global pos_selecionada
        pos_selecionada = comboBox_selecao_pos.get()
     
    def Mover():
        global x
        global y
        global z
        global x_rec
        global y_rec
        global z_rec
        global var_x
        global var_y
        global var_z
        global xi
        global yi
        global zi
        global Num_pontos
        global auto_modo
        #auto_modo = 0 --> desligado
        #auto_modo = 1 --> mover joints
        #auto_modo = 2 --> mover linear
        #auto_modo = 3 --> mover circular
        
        posicao=int(float(comboBox_selecao_pos.get()))
        incremento = velocidadeXYZ.get()/20
        
        # Posição inicial
        xi = x
        yi = y
        zi = z

        # Posição final
        xf = x_rec[posicao]
        yf = y_rec[posicao]
        zf = z_rec[posicao]


        # Encontrando a distância entre os dois pontos
        dist = math.sqrt(math.pow(xf-xi,2)+math.pow(yf-yi,2)+math.pow(zf-zi,2))

        # Encontrando o número de pontos a serem gerados
        Num_pontos = dist/incremento
        Num_pontos = round(Num_pontos,0)
        Num_pontos = int(Num_pontos)

        # Encontrando a variação para cada eixo (x, y e z)
        var_x = (xf-xi)/Num_pontos
        var_y = (yf-yi)/Num_pontos
        var_z = (zf-zi)/Num_pontos
      
        auto_modo = 2
            
        janela_mover_pos.destroy()
    
    def cancelar():
        janela_mover_pos.destroy()
        
    janela_mover_pos = tkinter.Tk()
    janela_mover_pos.title("Mover Linear")
    #Dimensões da janela
    #LxA+E+T
    #Largura x Altura + Distância à esquerda + Distância do topo
    janela_mover_pos.geometry("270x170+200+200")
    
    text_mover_pos=Label(janela_mover_pos,text="Deseja mover para qual posição?",foreground="#000000")
    text_mover_pos.place(x=45,y=20,width=170,height=15)
    
    text_num_pos=Label(janela_mover_pos,text="Posição: ",foreground="#000000")
    text_num_pos.place(x=45,y=70,width=50,height=15)
    
    bt_mover=Button(janela_mover_pos,text="Mover",background="#FFE4B5", command=Mover)
    bt_mover.place(x=65,y=120,width=60,height=30)
    
    bt_cancelar=Button(janela_mover_pos,text="Cancelar",background="#FFE4B5", command=cancelar)
    bt_cancelar.place(x=140,y=120,width=60,height=30)
    
    pos_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    comboBox_selecao_pos = ttk.Combobox(janela_mover_pos,values=pos_list)
    comboBox_selecao_pos.grid(column=0, row=1,)
    comboBox_selecao_pos.pack(padx=100, pady=67)
    comboBox_selecao_pos.current(0)
    comboBox_selecao_pos.bind("<<ComboboxSelected>>", callbackFunc)
    
    janela_mover_pos.mainloop()

def Mover_Joints():     
    import tkinter
    from tkinter import ttk
    
    def callbackFunc(event):
        global pos_selecionada
        pos_selecionada = comboBox_selecao_pos.get()
     
    def Mover():
        global j1
        global j2
        global j3
        global j1_rec
        global j2_rec
        global j3_rec
        global Num_pontos
        global var_j1
        global var_j2
        global var_j3
        global j1i
        global j2i
        global j3i
        global auto_modo
        #auto_modo = 0 --> desligado
        #auto_modo = 1 --> mover joints
        #auto_modo = 2 --> mover linear
        #auto_modo = 3 --> mover circular
        
        posicao=int(float(comboBox_selecao_pos.get()))    
        incremento = velocidadeJoints.get()/50
        
        # Posição inicial
        j1i = j1
        j2i = j2
        j3i = j3

        # Posição final
        j1f = j1_rec[posicao]
        j2f = j2_rec[posicao]
        j3f = j3_rec[posicao]


       # Encontrando o número de pontos a serem gerados

        angulo = max(abs(j1f-j1i),abs(j2f-j2i),abs(j3f-j3i))
        Num_pontos = angulo/incremento
        Num_pontos = round(Num_pontos,0)
        Num_pontos = int(Num_pontos)

        # Encontrando a variação para cada junta (j1, j2 e j3)

        var_j1 = (j1f-j1i)/Num_pontos
        var_j2 = (j2f-j2i)/Num_pontos
        var_j3 = (j3f-j3i)/Num_pontos

        auto_modo = 1
            
        janela_mover_pos.destroy()
    
    def cancelar():
        janela_mover_pos.destroy()
        
    janela_mover_pos = tkinter.Tk()
    janela_mover_pos.title("Mover Joints")
    #Dimensões da janela
    #LxA+E+T
    #Largura x Altura + Distância à esquerda + Distância do topo
    janela_mover_pos.geometry("270x170+200+200")
    
    text_mover_pos=Label(janela_mover_pos,text="Deseja mover para qual posição?",foreground="#000000")
    text_mover_pos.place(x=45,y=20,width=170,height=15)
    
    text_num_pos=Label(janela_mover_pos,text="Posição: ",foreground="#000000")
    text_num_pos.place(x=45,y=70,width=50,height=15)
    
    bt_mover=Button(janela_mover_pos,text="Mover",background="#FFE4B5", command=Mover)
    bt_mover.place(x=65,y=120,width=60,height=30)
    
    bt_cancelar=Button(janela_mover_pos,text="Cancelar",background="#FFE4B5", command=cancelar)
    bt_cancelar.place(x=140,y=120,width=60,height=30)
    
    pos_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    comboBox_selecao_pos = ttk.Combobox(janela_mover_pos,values=pos_list)
    comboBox_selecao_pos.grid(column=0, row=1,)
    comboBox_selecao_pos.pack(padx=100, pady=67)
    comboBox_selecao_pos.current(0)
    comboBox_selecao_pos.bind("<<ComboboxSelected>>", callbackFunc)
    
    janela_mover_pos.mainloop()
    
def Mover_Circular():     
    import tkinter
    from tkinter import ttk
    
    def callbackFunc(event):
        global pos_selecionada
        pos_selecionada = comboBox_selecao_pos.get()
        
    def callbackFunc2(event):
        global pos_selecionada_int
        pos_selecionada_int = comboBox_selecao_pos_int.get()
     
    def Mover():
        global x
        global y
        global z
        global x_rec
        global y_rec
        global z_rec
        global xi
        global yi
        global zi
        global xint
        global yint
        global zint
        global xf
        global yf
        global zf
        global Num_pontos
        global auto_modo
        #auto_modo = 0 --> desligado
        #auto_modo = 1 --> mover joints
        #auto_modo = 2 --> mover linear
        #auto_modo = 3 --> mover circular
        
        posicao=int(float(comboBox_selecao_pos.get()))#posição final
        posicao_int=int(float(comboBox_selecao_pos_int.get()))#posição intermediária
        incremento = velocidadeXYZ.get()/20
        
        # Posição inicial
        xi = x
        yi = y
        zi = z
        
        # Posição intermediária
        xint = x_rec[posicao_int]
        yint = y_rec[posicao_int]
        zint = z_rec[posicao_int]
        yint = yint*2

        # Posição final
        xf = x_rec[posicao]
        yf = y_rec[posicao]
        zf = z_rec[posicao]


       # Encontrando a distância entre os pontos
        dist = (math.sqrt(math.pow(xf-xint,2)+math.pow(yf-yint,2)+math.pow(zf-zint,2)))+(math.sqrt(math.pow(xint-xi,2)+math.pow(yint-yi,2)+math.pow(zint-zi,2)))

        # Encontrando o número de pontos a serem gerados
        Num_pontos = dist/incremento
        Num_pontos = round(Num_pontos,0)
        Num_pontos = int(Num_pontos)

        auto_modo = 3
            
        janela_mover_pos.destroy()
    
    def cancelar():
        janela_mover_pos.destroy()
        
    janela_mover_pos = tkinter.Tk()
    janela_mover_pos.title("Mover Circular")
    #Dimensões da janela
    #LxA+E+T
    #Largura x Altura + Distância à esquerda + Distância do topo
    janela_mover_pos.geometry("270x170+200+200")
    
    text_mover_pos=Label(janela_mover_pos,text="Deseja mover para qual posição?",foreground="#000000")
    text_mover_pos.place(x=45,y=10,width=170,height=15)
    
    text_num_pos=Label(janela_mover_pos,text="Posição: ",foreground="#000000")
    text_num_pos.place(x=60,y=35,width=50,height=15)
    
    text_mover_pos_int=Label(janela_mover_pos,text="Informe a posição intermediária:",foreground="#000000")
    text_mover_pos_int.place(x=45,y=65,width=170,height=15)
    
    text_num_pos_int=Label(janela_mover_pos,text="Posição: ",foreground="#000000")
    text_num_pos_int.place(x=60,y=90,width=50,height=15)
    
    bt_mover=Button(janela_mover_pos,text="Mover",background="#FFE4B5", command=Mover)
    bt_mover.place(x=65,y=120,width=60,height=30)
    
    bt_cancelar=Button(janela_mover_pos,text="Cancelar",background="#FFE4B5", command=cancelar)
    bt_cancelar.place(x=140,y=120,width=60,height=30)
    
    pos_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    comboBox_selecao_pos = ttk.Combobox(janela_mover_pos,values=pos_list, width=8)
    comboBox_selecao_pos.place(x=115, y=32)
    comboBox_selecao_pos.current(0)
    comboBox_selecao_pos.bind("<<ComboboxSelected>>", callbackFunc)
    comboBox_selecao_pos_int = ttk.Combobox(janela_mover_pos,values=pos_list, width=8)
    comboBox_selecao_pos_int.place(x=115, y=87)
    comboBox_selecao_pos_int.current(0)
    comboBox_selecao_pos_int.bind("<<ComboboxSelected>>", callbackFunc2)
    
    janela_mover_pos.mainloop()
    
def cinematica():
    global valor_modo
    global auto_modo
    global x
    global y
    global z
    global l1
    global l2
    global l3
    global j1
    global j2
    global j3
    global j1_ant
    global j2_ant
    global j3_ant
    global Saida
    global Leitura_Entradas
    global criar_prog
    global nomeProg
    
    if ((valor_modo.get() == 1) and (auto_modo == 0)) or (auto_modo == 2) or (auto_modo == 3):
        #print("SELECIONADO MODO XYZ")
        
        #Encontrando Teta0
        absx = abs(x)
        if (x==0)and(y>0):
            Teta0 = 90
        elif (x==0)and(y<0):
            Teta0 = -90
        elif (x<0):
            tanTeta0 = (y/absx)
            Teta0 = 180-math.degrees(math.atan(tanTeta0))
        else:
            tanTeta0 = (y/absx)
            Teta0 = math.degrees(math.atan(tanTeta0))
         
        absTeta0 = abs(Teta0)
        
        #Ajuste do braço l3
        x2 = x-((math.cos(math.radians(Teta0)))*l3) #x2 = x com a translação do braço l3
        y2 = y-((math.sin(math.radians(Teta0)))*l3) #y2 = y com a translação do braço l3
      
        #Encontrando Teta2
        #Teta2_1 --> cotovelo abaixo
        #Teta2_2 --> cotovelo acima
        cosTeta2 = -(1/2)*((-math.pow(x2,2)-math.pow(y2,2)-math.pow(z,2)+math.pow(l2,2)+math.pow(l1,2))/(l2*l1))
        senTeta2_1 = math.sqrt(1-math.pow(cosTeta2,2))
        senTeta2_2 = -math.sqrt(1-math.pow(cosTeta2,2))
        Teta2_1 = math.degrees(math.acos(cosTeta2))
        Teta2_2 = -math.degrees(math.acos(cosTeta2))

        #Encontrando Teta1
        #Teta1_1 --> cotovelo abaixo
        #Teta1_2 --> cotovelo acima
        senTeta1_1 = (z*cosTeta2*l2+l1*z-math.sqrt(math.pow(z,2)*math.pow(cosTeta2,2)*math.pow(l2,2)+2*math.pow(l2,3)*cosTeta2*l1*math.pow(senTeta2_1,2)+math.pow(l1,2)*math.pow(l2,2)*math.pow(senTeta2_1,2)+math.pow(l2,4)*math.pow(senTeta2_1,2)-math.pow(l2,2)*math.pow(z,2)))/(2*l2*cosTeta2*l1+math.pow(l1,2)+math.pow(l2,2))
        senTeta1_2 = (z*cosTeta2*l2+l1*z+math.sqrt(math.pow(z,2)*math.pow(cosTeta2,2)*math.pow(l2,2)+2*math.pow(l2,3)*cosTeta2*l1*math.pow(senTeta2_1,2)+math.pow(l1,2)*math.pow(l2,2)*math.pow(senTeta2_1,2)+math.pow(l2,4)*math.pow(senTeta2_1,2)-math.pow(l2,2)*math.pow(z,2)))/(2*l2*cosTeta2*l1+math.pow(l1,2)+math.pow(l2,2))
        Teta1_1 = math.degrees(math.asin(senTeta1_1))
        Teta1_2 = math.degrees(math.asin(senTeta1_2))
         

        if (math.sqrt(math.pow(x2,2)+math.pow(y2,2)+math.pow((z-l1),2))<l2):
            Teta1_2 = 180-math.degrees(math.asin(senTeta1_2))
            

        j1=Teta0
        if (abs(Teta1_2-j2) <= abs(Teta1_1-j2)):
            j2=Teta1_2
            j3=Teta2_2
            
        else:
            j2=Teta1_1
            j3=Teta2_1            
                
        j1print=round(j1,2)
        j2print=round(j2,2)
        j3print=round(j3,2)
        
        lbJ1.config(text=j1print)
        lbJ2.config(text=j2print)
        lbJ3.config(text=j3print)        
        
             
    elif ((valor_modo.get() == 2) and (auto_modo == 0)) or (auto_modo == 1):
        #print("SELECIONADO MODO JOINTS")
        
        Teta0=j1
        Teta1=j2
        Teta2=j3
        
        #Encontrando X
        x2 = (math.cos(math.radians(Teta0))*math.cos(math.radians(Teta1))*math.cos(math.radians(Teta2))-math.cos(math.radians(Teta0))*math.sin(math.radians(Teta1))*math.sin(math.radians(Teta2)))*l2+math.cos(math.radians(Teta0))*math.cos(math.radians(Teta1))*l1
        x = x2+((math.cos(math.radians(Teta0)))*l3)# x = x2 com a translação do braço l3

        #Encontrando Y
        y2 = (math.sin(math.radians(Teta0))*math.cos(math.radians(Teta1))*math.cos(math.radians(Teta2))-math.sin(math.radians(Teta0))*math.sin(math.radians(Teta1))*math.sin(math.radians(Teta2)))*l2+math.sin(math.radians(Teta0))*math.cos(math.radians(Teta1))*l1
        y = y2+((math.sin(math.radians(Teta0)))*l3)# y = y2 com a translação do braço l3
        
        #Encontrando Z
        z = (math.sin(math.radians(Teta1))*math.cos(math.radians(Teta2))+math.cos(math.radians(Teta1))*math.sin(math.radians(Teta2)))*l2+math.sin(math.radians(Teta1))*l1
            
        xprint=round(x,2)
        yprint=round(y,2)
        zprint=round(z,2)
        
        lbX.config(text=xprint)
        lbY.config(text=yprint)
        lbZ.config(text=zprint)
                 

    elif auto_modo == 0:
        print("SELECIONE UM MODO DE CONTROLE")
       
    #Correção da folga da base
    if((j1-j1_ant)<0):
        correcao_j1 = 0.5
    else:
        correcao_j1 = 0
    
    #Correção da folga do braço L1
    if((j2-j2_ant)>0):
        correcao_j2 = -3
    else:
        correcao_j2 = 0
    
    #Correção da folga do braço L2
    if((j3-j3_ant)<0):
        correcao_j3 = -3
    else:
        correcao_j3 = 0
        
    #Cálculo do ângulo do motor da Base
    M1 = (j1-(-28))*(166-0)/(68-(-28))+0+correcao_j1
    if M1 > 179: M1 = 179 #Limite máximo de eixo
    if M1 < 0: M1 = 0 #Limite mínimo de eixo
    M1 = (M1-0)*(2500-500)/(179-0)+500 #Conversão para Microsegundos
    
    #Cálculo do ângulo do motor do braço L1
    M2 = (j2-41)*(92.5-130)/(90-41)+130+correcao_j2
    if M2 > 141: M2 = 141 #Limite máximo de eixo
    if M2 < 57: M2 = 57 #Limite mínimo de eixo
    M2 = (M2-0)*(2500-500)/(179-0)+500 #Conversão para Microsegundos

    #Cálculo do ângulo do motor do braço L2
    M3 = (j3+j2)+81.73+correcao_j3
    if M3 > 110: M3 = 110 #Limite máximo de eixo
    if M3 < 20: M3 = 20 #Limite mínimo de eixo
    M3 = (M3-0)*(2500-500)/(179-0)+500 #Conversão para Microsegundos
    
    #Cálculo do ângulo do motor da Garra
    Garra = posicaoGarra.get()
    Garra = (Garra-0)*(150-57)/(100-0)+57
    Garra = (Garra-0)*(2500-500)/(179-0)+500 #Conversão para Microsegundos
    

    #Código a ser enviado para o robô
    codigo = "<{0}{1}{2}{3}{4}{5}{6}{7}>\n"
    codigo = (codigo.format(str("{:.0f}".format(M1)).zfill(4),str("{:.0f}".format(M2)).zfill(4),str("{:.0f}".format(M3)).zfill(4),str("{:.0f}".format(Garra)).zfill(4),str(Saida[0]),str(Saida[1]),str(Saida[2]),str(Leitura_Entradas)))
    codigo = str(codigo)
    lbComSerial.config(text=codigo[0:22])
    #print(codigo)
    comunicacao.write(codigo.encode())
    if criar_prog == 1:
        with open(nomeProg + '.txt','a') as arquivo:
            arquivo.write(codigo)

    #Armazenamento dos Ângulos para cálculos posteriores
    j1_ant = j1
    j2_ant = j2
    j3_ant = j3
    #time.sleep(0.07) 

app=Tk()
app.title("Controle do Robô")
app.geometry("800x500")
app.configure(background="#808080")

valor_modo=IntVar()

btradio_XYZ=Radiobutton(app,text="XYZ   ",variable=valor_modo,value=1)
btradio_XYZ.place(x=690,y=40)

btradio_Joints=Radiobutton(app,text="Joints",variable=valor_modo,value=2)
btradio_Joints.place(x=690,y=75)

XYZ=Label(app,background="#DCDCDC")
XYZ.place(x=20,y=150,width=300,height=330)

textXYZ=Label(app,text="XYZ",background="#DCDCDC",foreground="#000000")
textXYZ.place(x=30,y=160,width=30,height=15)

Joints=Label(app,background="#DCDCDC")
Joints.place(x=340,y=150,width=300,height=330)

textJoints=Label(app,text="Joints",background="#DCDCDC",foreground="#000000")
textJoints.place(x=350,y=160,width=30,height=15)

bt_Conect=Button(app,text="Conectar",background="#98FB98",command=conectar)
bt_Conect.place(x=10,y=20,width=150,height=40)
bt_Disconect=Button(app,text="Desconectar",background="#F0E68C",command=desconectar)
bt_Disconect.place(x=170,y=20,width=150,height=40)

bt_xmenos=Button(app,text="X-",background="#FFE4B5")
bt_xmenos.place(x=70,y=200,width=40,height=40)
bt_xmais=Button(app,text="X+",background="#FFE4B5")
bt_xmais.place(x=120,y=200,width=40,height=40)
bt_ymenos=Button(app,text="Y-",background="#FFE4B5")
bt_ymenos.place(x=70,y=250,width=40,height=40)
bt_ymais=Button(app,text="Y+",background="#FFE4B5")
bt_ymais.place(x=120,y=250,width=40,height=40)
bt_zmenos=Button(app,text="Z-",background="#FFE4B5")
bt_zmenos.place(x=70,y=300,width=40,height=40)
bt_zmais=Button(app,text="Z+",background="#FFE4B5")
bt_zmais.place(x=120,y=300,width=40,height=40)

bt_j1menos=Button(app,text="J1-",background="#FFE4B5")
bt_j1menos.place(x=390,y=200,width=40,height=40)
bt_j1mais=Button(app,text="J1+",background="#FFE4B5")
bt_j1mais.place(x=440,y=200,width=40,height=40)
bt_j2menos=Button(app,text="J2-",background="#FFE4B5")
bt_j2menos.place(x=390,y=250,width=40,height=40)
bt_j2mais=Button(app,text="J2+",background="#FFE4B5")
bt_j2mais.place(x=440,y=250,width=40,height=40)
bt_j3menos=Button(app,text="J3-",background="#FFE4B5")
bt_j3menos.place(x=390,y=300,width=40,height=40)
bt_j3mais=Button(app,text="J3+",background="#FFE4B5")
bt_j3mais.place(x=440,y=300,width=40,height=40)

textVeloXYZ=Label(app,text="Velocidade",background="#DCDCDC",foreground="#000000")
textVeloXYZ.place(x=30,y=380,width=65,height=15)

textVeloJoints=Label(app,text="Velocidade",background="#DCDCDC",foreground="#000000")
textVeloJoints.place(x=350,y=380,width=65,height=15)

velocidadeXYZ=Scale(app,from_=0,to=10,orient=HORIZONTAL,background="#ADD8E6")
velocidadeXYZ.place(x=115,y=410)
velocidadeXYZ.set(5)

velocidadeJoints=Scale(app,from_=0,to=10,orient=HORIZONTAL,background="#ADD8E6")
velocidadeJoints.place(x=435,y=410)
velocidadeJoints.set(5)

garra=Label(app,background="#DCDCDC")
garra.place(x=340,y=20,width=300,height=100)

textGarra=Label(app,text="Garra",background="#DCDCDC",foreground="#000000")
textGarra.place(x=350,y=30,width=30,height=15)

posicaoGarra=Scale(app,from_=0,to=100,orient=HORIZONTAL,background="#ADD8E6", command=Garra)
posicaoGarra.place(x=435,y=60)
posicaoGarra.set(50)

textFechada=Label(app,text="Fechada",background="#DCDCDC",foreground="#000000")
textFechada.place(x=380,y=80,width=50,height=15)

textAberta=Label(app,text="Aberta",background="#DCDCDC",foreground="#000000")
textAberta.place(x=545,y=80,width=40,height=15)

bt_Abrir_Garra=Button(app,text="Abrir",background="#98FB98",command=Abrir_Garra)
bt_Abrir_Garra.place(x=490,y=30,width=50,height=25)

bt_Fechar_Garra=Button(app,text="Fechar",background="#F0E68C",command=Fechar_Garra)
bt_Fechar_Garra.place(x=435,y=30,width=50,height=25)

bt_Limites_Garra=Button(app,text="Ajustar\nLimites",background="#DCDCDC",command=Limites_Garra)
bt_Limites_Garra.place(x=565,y=30,width=50,height=35)

textX=Label(app,text="X :",background="#DCDCDC",foreground="#000000")
textX.place(x=190,y=225,width=30,height=25)

lbX=Label(app,text=x,background="#FFFFFF")
lbX.place(x=220,y=225,width=70,height=25)

textY=Label(app,text="Y :",background="#DCDCDC",foreground="#000000")
textY.place(x=190,y=255,width=30,height=25)

lbY=Label(app,text=y,background="#FFFFFF")
lbY.place(x=220,y=255,width=70,height=25)

textZ=Label(app,text="Z :",background="#DCDCDC",foreground="#000000")
textZ.place(x=190,y=285,width=30,height=25)

lbZ=Label(app,text=z,background="#FFFFFF")
lbZ.place(x=220,y=285,width=70,height=25)

textJ1=Label(app,text="J1 :",background="#DCDCDC",foreground="#000000")
textJ1.place(x=510,y=225,width=30,height=25)

lbJ1=Label(app,text=j1,background="#FFFFFF")
lbJ1.place(x=540,y=225,width=70,height=25)

textJ2=Label(app,text="J2 :",background="#DCDCDC",foreground="#000000")
textJ2.place(x=510,y=255,width=30,height=25)

lbJ2=Label(app,text=j2,background="#FFFFFF")
lbJ2.place(x=540,y=255,width=70,height=25)

textJ3=Label(app,text="J3 :",background="#DCDCDC",foreground="#000000")
textJ3.place(x=510,y=285,width=30,height=25)

lbJ3=Label(app,text=j3,background="#FFFFFF")
lbJ3.place(x=540,y=285,width=70,height=25)

textComSerial=Label(app,text="COM SERIAL :",background="#808080",foreground="#000000")
textComSerial.place(x=10,y=115,width=100,height=25)

lbComSerial=Label(app,background="#DCDCDC")
lbComSerial.place(x=105,y=110,width=215,height=25)


bt_xmenos.bind("<ButtonPress-1>", xmenos_pressed)
bt_xmenos.bind("<ButtonRelease-1>", xmenos_released)

bt_xmais.bind("<ButtonPress-1>", xmais_pressed)
bt_xmais.bind("<ButtonRelease-1>", xmais_released)

bt_ymenos.bind("<ButtonPress-1>", ymenos_pressed)
bt_ymenos.bind("<ButtonRelease-1>", ymenos_released)

bt_ymais.bind("<ButtonPress-1>", ymais_pressed)
bt_ymais.bind("<ButtonRelease-1>", ymais_released)

bt_zmenos.bind("<ButtonPress-1>", zmenos_pressed)
bt_zmenos.bind("<ButtonRelease-1>", zmenos_released)

bt_zmais.bind("<ButtonPress-1>", zmais_pressed)
bt_zmais.bind("<ButtonRelease-1>", zmais_released)

bt_j1menos.bind("<ButtonPress-1>", j1menos_pressed)
bt_j1menos.bind("<ButtonRelease-1>", j1menos_released)

bt_j1mais.bind("<ButtonPress-1>", j1mais_pressed)
bt_j1mais.bind("<ButtonRelease-1>", j1mais_released)

bt_j2menos.bind("<ButtonPress-1>", j2menos_pressed)
bt_j2menos.bind("<ButtonRelease-1>", j2menos_released)

bt_j2mais.bind("<ButtonPress-1>", j2mais_pressed)
bt_j2mais.bind("<ButtonRelease-1>", j2mais_released)

bt_j3menos.bind("<ButtonPress-1>", j3menos_pressed)
bt_j3menos.bind("<ButtonRelease-1>", j3menos_released)

bt_j3mais.bind("<ButtonPress-1>", j3mais_pressed)
bt_j3mais.bind("<ButtonRelease-1>", j3mais_released)

t = Thread(target = calculo, args = ())
t.start()

bt_Gravar=Button(app,text="Gravar Posição",background="#DCDCDC",command=Gravar)
bt_Gravar.place(x=675,y=150,width=100,height=30)

bt_Mover_Linear=Button(app,text="Mover Linear",background="#DCDCDC",command=Mover_Linear)
bt_Mover_Linear.place(x=675,y=190,width=100,height=30)

bt_Mover_Joints=Button(app,text="Mover Joints",background="#DCDCDC",command=Mover_Joints)
bt_Mover_Joints.place(x=675,y=230,width=100,height=30)

bt_Mover_Circular=Button(app,text="Mover Circular",background="#DCDCDC",command=Mover_Circular)
bt_Mover_Circular.place(x=675,y=270,width=100,height=30)

bt_Setar_Saida=Button(app,text="Definir Saídas",background="#DCDCDC",command=Setar_Saida)
bt_Setar_Saida.place(x=675,y=310,width=100,height=30)

bt_Aguardar_Entrada=Button(app,text="Aguardar Entrada",background="#DCDCDC",command=Aguardar_Entrada)
bt_Aguardar_Entrada.place(x=675,y=350,width=100,height=30)

bt_Criar_Prog=Button(app,text="Criar Programa",background="#DCDCDC",command=Criar_Programa)
bt_Criar_Prog.place(x=675,y=390,width=100,height=30)

bt_Executar_Prog=Button(app,text="Rodar Programa",background="#DCDCDC",command=Executar_Programa)
bt_Executar_Prog.place(x=675,y=430,width=100,height=30)

bt_SalvarProg=Button(app, text="Salvar Posições", background="#DCDCDC",command=Salvar_Programa)
bt_SalvarProg.place(x=10,y=70,width=150,height=30)

bt_AbrirProg=Button(app, text="Carregar Posições", background="#DCDCDC",command=Abrir_Programa)
bt_AbrirProg.place(x=170,y=70,width=150,height=30)


app.mainloop()