from pygame import Rect
from helpers.Button import Button
from helpers.Background import Background
from sprites.player.CAINE import CAINE
from sprites.enemies.Enemy1 import Enemy1
from sprites.enemies.Enemy2 import Enemy2
from sprites.score.Coin import Coin 
import pgzero.builtins as pz 
WIN_TIME = 30.0

class GameScene:
    def __init__(self, screen,sounds):
        self.screen  = screen
        self.sounds = sounds
        self.state = "playing"
        self.timer = 0.0 
        self.player = CAINE(x=100,y=100)

        self.enemies = [
            Enemy1(x = 500, y = 400, patrol_left = 300, patrol_right = 700),
            Enemy2(x = 650, y = 400, patrol_left = 450, patrol_right = 780)
        ]

        self.coins=[
            Coin(200, 340, "gold"),
            Coin(280, 340, "gold"),
            Coin(360, 340, "silver"),
            Coin(440, 340, "silver"),
            Coin(520, 270, "gold"),
            Coin(600, 270, "bronze"),
            Coin(150, 230, "bronze"),
            Coin(700, 340, "silver"),
        ]

        self._heart_full = "tiles/default/hud_heart"
        self._heart_empty = "tiles/default/hud_heart_empty"

        center_x =400
        self.again_btn = Button ("PLAY AGAIN", Rect((center_x-150,320),(300,60)), (25,200,150),screen)
        self.quit_btn = Button ("QUIT", Rect((center_x-150,400),(300,60)), (235,100,100),screen)

    def update(self, dt,keyboard = None):
        if self.state != "playing":
            return 
        self.timer += dt

        if keyboard is None:
            keyboard = pz.keyboard

        self.player.update(dt, keyboard)

        for enemy in self.enemies:
            enemy.update(dt)
            if enemy.collides_with(self.player.actor):
                self.player.take_hit(self.sounds)

        for coin in self.coins:
            if coin.check_collect(self.player.actor):
                self.player.collect_coin(coin.value, self.sounds)


        if not self.player.alive:
            self.state = "lost"
            return 
        
        if self.timer>= WIN_TIME and self.player.score >= 45:
            self.state = "won"
            try:
                self.sounds.win.play()
            except Exception:
                pass
        else:
            if self.timer >= WIN_TIME and self.player.score < 45:
                self.state = "lost"
        
    
    def on_key_down(self, key):
        if key in (pz.keys.SPACE, pz.keys.UP):
            self.player.jump(self.sounds)

    
    def draw(self):
        Background.draw_background(self.screen)
        self.screen.draw.line((0,400),(800,400),(80,50,20))
        for coin in self.coins: 
            coin.draw()
        
        for enemy in self.enemies:
            enemy.draw()
        
        self.player.draw()

        self._draw_hud()

        if self.state=="won":
            self._draw_overlay("YOU WIN!", (50,200,80))
        elif self.state=="lost":
            self._draw_overlay("GAME OVER", (220,50,50))
    
    def _draw_hud(self):
        remaining = max(0, WIN_TIME - self.timer)
        mins = int (remaining) //60
        secs = int (remaining) % 60 
        self.screen.draw.text(
            f"{mins}:{secs:02d}",
            topleft=(10,10),
            fontsize = 36,
            color=(255,255,255),
        )

        self.screen.draw.text(
            f"SCORE: {self.player.score}",
            topleft=(10,50),
            fontsize=30,
            color=(255,220,50),
        )

        for i in range(3): 
            img = self._heart_full if i<self.player.lives else self._heart_empty
            try:
                self.screen.blit(img,(600+ i * 45, 20))
            except:
                color = (220,50,50) if i< self.player.lives else (80,80,80)
                self.screen.draw.filled_circle((712 + i * 36, 22), 12 , color)
    
    def _draw_overlay(self, message: str, color: tuple):
        self.screen.draw.filled_rect(Rect(150, 160, 500, 300), (0,0,0))
        self.screen.draw.text(message, center = (400, 230), fontsize= 72, color = color)
        self.screen.draw.text(
            f"SCORE: {self.player.score}",
            center = {400,295},
            fontsize=36,
            color = (255,220,50),
        )
        self.again_btn.draw()
        self.quit_btn.draw()
    
    def handle_click(self, pos):
        if self.state in ("won", "lost"):
            if self.again_btn.is_clicked(pos):
                return "restart"
            if self.quit_btn.is_clicked(pos):
                return "quit"
        return None 