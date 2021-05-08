from pygame import*

w = 700

h = 500

win = display.set_mode((w,h))
class Alpha(sprite.Sprite):
    def __init__(self,x,y,h,w,image_name,speed):
        super().__init__()
        self.image = image.load(image_name)
        self.rect = Rect(w,h,y,x)
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))

ball = Alpha(550,550,)


win.fill((255,255,255))



while True:



    for e in event.get():
        if e.type == 12:
            exit()


    display.update()
