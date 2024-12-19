import pgzrun,random
WIDTH=1900
HEIGHT=1000
TITLE="PATTERN"
def draw():
    w=WIDTH
    h=HEIGHT-500
    screen.fill("yellow")
    for i in range(50):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        rect=Rect((200,100),(w,h))
        rect.center=950,500
        screen.draw.rect(rect, (r,g,b))
        w-=10
        h+=10
        r+=50
        g-=50
def update():
    pass


pgzrun.go()