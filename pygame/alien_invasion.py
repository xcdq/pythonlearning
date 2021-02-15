import pygame
from setting import Settings
from ship import Ship
# from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GamesStats


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stats = GamesStats(ai_settings)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建外星人
    # alien = Alien(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 开始游戏主循环
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while(True):
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.updata_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.updata_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
