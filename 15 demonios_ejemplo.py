import sys
import pygame
import time
import requests
import threading

pygame.init()

width, height = 800, 600

TEXT = ''

def get_btc_price(url='https://api.bitso.com/v3/ticker/?book=btc_usd'):
    response = requests.get(url)
    if response.status_code != 200:
        return
    data = response.json()
    btc_price = data['payload']['last']
    global TEXT
    TEXT = f'Precio de BTC: ${btc_price}'

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(TEXT)


white = (255, 255, 255)
red = (115, 38, 80)
black = (0, 0, 0)




thread = threading.Thread(target=get_btc_price, daemon=True)
thread.start()



font = pygame.font.Font(None, 36)

while True:

    text = font.render(TEXT, True, black)
    rect = text.get_rect()
    rect.center = (width // 2, height // 2)

    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(text, rect)

    pygame.display.update()