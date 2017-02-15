

#This is a program that draws a house using the SimpleGraphics module.

#Five primitives are used - rect, line, poly, blob, and elipse
#Twelve colors are used (Sky blue, light green, dark green, brown, saddle brown, beige, black, dark grey, grey, light blue, gold, white)


from SimpleGraphics import*
#imports everything from simplegraphics module   

     
#Sky
setFill("sky blue")
#Colours the sky
sky = rect(0,0,getWidth(),getHeight())
#Determines size of shape - in this case, it is the size of the window.

#Grass
setFill("light green")
sky = rect(0, 550, getWidth(), getHeight())

#Chimney
setColor('brown')
setOutline("black")
setWidth(5)
rect (580, 170, 100, 260)

#ChimneyLine 1
setColor ('black')
setWidth (3)
line (680, 200, 580, 200)

#ChimneyLine 2
setColor ('black')
setWidth (3)
line (680, 250, 580, 250)

#ChimneyLine 3
setColor ('black')
setWidth (3)
line (680, 225, 580, 225)

#Building
setFill("beige")
setOutline("black")
setWidth(5)
rect(300, 300, 400, 300)

#Roof
setColor('dark grey')
setOutline('black')
polygon(720, 300, 280, 300, 500, 160)       

#Door
setColor('brown')
setOutline("black")
rect (450, 440, 100, 160)

#opentext
setFont("Times", "20", "bold")
setColor("white")
text(500, 460, "OPEN")

#Left Window
setColor('light blue')
setOutline("grey")
rect (350, 320, 100, 100)

#Right Window
setColor('light blue')
setOutline("grey")
rect (550, 320, 100, 100)

#Door Handle
setColor("gold")
setOutline("black")
setWidth(2)
ellipse(525, 520, 18, 18)

#Cloud
setColor("white")
blob(600, 80, 250, 40, 225, 200)

setColor("white")
blob(150, 80, 450, 60, 400, 220)

setColor("white")
blob(300, 210, 500, 110, 250, 0)


#Sun
img = loadImage("Sun.gif")
drawImage(img, 0, 0)

#Tree1
setColor("saddle brown")
setOutline("black")
rect (195, 520, 15, 30)

setColor("dark green")
setOutline("black")
polygon(250, 520, 150, 520, 200, 300)

#tree2
setColor("saddle brown")
setOutline("black")
rect (95, 520, 15, 30)

setColor("dark green")
setOutline("black")
polygon(50, 520, 150, 520, 100, 300)

#In case the user doesn't know where to find the house. It isn't on this page!

print("\nPlease switch to the image window to view your house!")

