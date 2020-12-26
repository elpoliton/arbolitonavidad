# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 22:24:32 2020

@author: JOSE
"""
import turtle
from playsound import playsound
playsound('jingle.mp3',block=False)


t= turtle.Turtle()
t.getscreen().bgcolor("#72bcd4")
turtle.title("Feliz Navidad")

t.goto(0,0) #colocar al inicio la pantalla
#comandos -> fd fordward / lt left / bk backward -retroceso / rt right /  círculo -> t.circle(60) / t.dot(20) / t.penup - ocultar línea / t.pendown - mostrar flecha
# t.undo - deshace el último comando / t.clear / t.rest - reseteo  / t.setheading / 
#árbol de navidad

#tallo del árbol
t.pen(pencolor="purple",fillcolor="saddlebrown",pensize=2,speed=3)
t.begin_fill()
for i in range(4):
    t.fd(90)
    t.rt(90)
t.end_fill()
t.bk(75) # retroceder

#árbol triángulo 1
t.pen(pencolor="darkolivegreen",fillcolor="darkolivegreen",pensize=2,speed=3)
t.begin_fill()

for i in range(3):
    t.fd(240)
    t.lt(120)
t.end_fill() #fin de triángulo 1

#dirigirse al siguiente triángulo
t.penup()
t.lt(90)
t.fd(120)
t.rt(90)
t.fd(20)
t.pendown()

#árbol triángulo 2
t.begin_fill()
for i in range(3):
    t.fd(200)
    t.lt(120)
t.end_fill()

#dirigirse al siguiente triangulo
t.penup()
t.lt(90)
t.fd(100)
t.rt(90)
t.fd(20)
t.pendown()

#árbol triángulo 3
t.begin_fill()
for i in range(3):
    t.fd(160)
    t.lt(120)
t.end_fill()

# mover hacia la estrella
t.penup()
t.lt(62)
t.fd(120)
t.rt(26)
t.pendown()

#estrella
t.pen(pencolor="yellow",fillcolor="yellow",pensize=2,speed=3)
t.begin_fill()
a = 1
while a<5:
    t.fd(72)
    t.lt(145)
    a= a+1
t.end_fill() #fin de estrella

#mover para las bolas
t.pen(pencolor="red",fillcolor="orangered",pensize=2,speed=3)
t.penup()
t.fd(170)
t.pendown()
t.begin_fill()#1er círculo
t.circle(15)
t.end_fill()
t.lt(90) #rotar entre más alto más arriba
t.penup()
t.fd(85)
t.pendown()
t.begin_fill()#2do círculo
t.circle(15)
t.end_fill()
t.rt(80)#mover 60 - 80
t.penup()
t.fd(90)
t.pendown()
t.begin_fill()#3er círculo
t.circle(15)
t.end_fill()
t.rt(100)
t.penup()
t.fd(80)
t.pendown()
t.begin_fill()#4to círculo
t.circle(15)
t.end_fill()
t.lt(85)
t.penup()
t.fd(100)
t.pendown()
t.begin_fill()#5to círculo
t.circle(15)
t.end_fill()
t.lt(100) #más alto el valor se mueve para arriba
t.penup()
t.fd(130)
t.pendown()
t.begin_fill()#6to círculo
t.circle(15)
t.end_fill()

t.penup()
t.rt(100)
t.fd(190)
t.pendown()

t.pen(pencolor="dodgerblue",fillcolor="dodgerblue",pensize=2,speed=1)
style = ("bold",30,"italic") 
t.write("FELIZ NAVIDAD" ,font=style,align="center")
t.penup()
t.fd(50)
t.pendown()
t.write("Les desea Jose Guzmán" ,font=style,align="center")


#círculo
t.penup()
t.pen(pencolor="teal",fillcolor="blue",pensize=2,speed=1)
t.begin_fill()
n=10
while n<=1000:
    t.circle(n)
    n = n+10
t.end_fill()


'''
#estrella 2
t.fd(100)
t.lt(120)
for i in range(5):
    t.fd(200)
    t.lt(144)
'''