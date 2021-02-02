import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    bullets = Group()
    # 开始游戏主循环
    while(True):
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.updata_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
