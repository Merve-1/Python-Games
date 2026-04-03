from pygame import Rect
from pgzero.actor import Actor
from helpers.Button import Button
from helpers.Background import Background
import random 

class MenuScene:
    def __init__(self, screen,sounds):
        self.screen = screen
        self.sounds = sounds
        self.music_on = True
        self.play_btn = Button("PLAY", Rect((300,200),(200,60)), (25, 200, 150), screen)
        self.quit_btn = Button("QUIT", Rect((300,300),(200,60)), (235, 100, 100),   screen)
        self.music_btn = Button("MUSIC ON", Rect((10, 10), (120, 30)), (60, 60, 160), screen,  fontsize=15)
        
        self.objects = []

        self._start_music()
 
        forbidden = [
            Rect(150, 60, 500, 80),  
            Rect(280, 180, 240, 200), 
            Rect(  0,   0, 180,  60),
        ]

        images = [
            "characters/default/character_green_walk_b",
            "tiles/default/hud_key_blue",
            "tiles/default/coin_gold",
            "tiles/default/coin_silver",
            "tiles/default/coin_bronze",
        ]
        placed   = 0
        attempts = 0

        while placed < 7 and attempts < 1000:
            x = random.randint(0, 800)
            y = random.randint(0, 600)

            if any(zone.collidepoint(x, y) for zone in forbidden):
                attempts += 1
                continue  

            obj = Actor(random.choice(images))
            obj.pos = (x, y)
            self.objects.append(obj)
            placed   += 1
            attempts += 1
       


    def draw(self):
        Background.draw_background(self.screen)
        self.screen.draw.text("Mr. CAINE Game", center=(400,100), fontsize=60,color=(20,20,20))
        
        for obj in self.objects:
            obj.draw()

        self.play_btn.draw()
        self.quit_btn.draw()
        self.music_btn.draw()

    def handle_click(self, pos):
        if self.music_btn.is_clicked(pos):
            self._toggle_music()
            return None 
        if self.play_btn.is_clicked(pos):
            return "scene1"
        if self.quit_btn.is_clicked(pos):
            self.stop_music()
            quit()
        return None
    
    def _start_music(self):
        try:
            self.sounds.menu_music.play(-1) 
        except Exception:
            pass

    def _stop_music(self):
        try:
            self.sounds.menu_music.stop()
        except Exception:
            pass
 
    def _toggle_music(self):
        self.music_on = not self.music_on

        if self.music_on:
            self._start_music()
            self.music_btn.label = "MUSIC ON"
            self.music_btn.color = (60, 60, 160)
        else:
            self._stop_music()
            self.music_btn.label = "MUSIC OFF"
            self.music_btn.color = (100, 100, 100)
    
    def stop_music(self):
        self._stop_music()