import pygame 
import sys

t.mostrar()
pygame.init()

tela =  pygame.display.set_mode([500,500])
# run = True

quadrado   =  pygame.Rect(15,20,10,10)

clock =  pygame.time.Clock()

while True:
      for eventos in pygame.event.get():
          if eventos.type  == pygame.QUIT:
            #    run = False 
               pygame.quit()
               sys.exit()       
      
          if eventos.type == pygame.KEYDOWN:
               if eventos.key  == pygame.K_RIGHT:
                  quadrado.move_ip([10,0])
               if eventos.key == pygame.K_LEFT:
                    quadrado.move_ip([-10,0])  

               if eventos.key == pygame.K_UP:
                    quadrado.move_ip([0,-10])

               if eventos.key == pygame.K_DOWN:
                    quadrado.move_ip([0,10])            
          tela.fill('red')
          pygame.draw.rect(tela, 'green', quadrado)
    
          pygame.display.update()   