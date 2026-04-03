from pgzero.actor import Actor
from helpers.Animation import Animation 

GRAVITY = 800
JUMP_SPEED = -420 
MOVE_SPEED = 180 
GROUND_Y = 520
MAX_LIVES = 3
HIT_COOLDOWN = 1.5

WALK_FRAMES = ["characters/default/character_yellow_walk_a",
               "characters/default/character_yellow_walk_b"]

IDLE_FRAMES = ["characters/default/character_yellow_idle"]

JUMP_FRAMES = ["characters/default/character_yellow_jump"]

LOSE_FRAME = ["characters/default/character_yellow_hit"]

class CAINE: 
    def __init__(self, x:int, y: int):
        self.actor = Actor(IDLE_FRAMES[0])
        self.actor.pos = (x,y)

        self.vel_y = 0.0
        self.on_ground = False 
        self.facing_right = True 
        self.lives = MAX_LIVES
        self.hit_timer = 0.0
        self.alive = True
        self.score = 0

        self._walk_anim = Animation(WALK_FRAMES, fps = 8)
        self._idle_anim = Animation(IDLE_FRAMES, fps = 2)
        self._jump_anim = Animation(JUMP_FRAMES, fps = 2)
        self._moving = False
    def update(self, dt: float, keyboard): 
        if not self.alive:
            return
        self._moving = False
        if keyboard.left:
            self.actor.x -= MOVE_SPEED *dt 
            self.facing_right = False
            self._moving = True
            
        if keyboard.right:
            self.actor.x += MOVE_SPEED *dt 
            self.facing_right = False
            self._moving = True

        self.actor.x = max(20, min(780, self.actor.x))

        self.vel_y += GRAVITY * dt 
        self.actor.y += self.vel_y * dt 

        if self.actor.y >= GROUND_Y:
            self.actor.y = GROUND_Y
            self.vel_y = 0 
            self.on_ground = True
        else: 
            self.on_ground = False 
        
        if self.hit_timer > 0:
            self.hit_timer -= dt 

        if not self.on_ground:
            self._jump_anim.update(dt)
            self.actor.image = self._jump_anim.current_frame()
        elif self._moving:
            self._walk_anim.update(dt)
            self.actor.image = self._walk_anim.current_frame()
        else:
            self._idle_anim.update(dt)
            self.actor.image = self._idle_anim.current_frame()
        


    def jump (self, sounds):
        if self.on_ground:
            self.vel_y = JUMP_SPEED
            try: 
                sounds.jump.play()
            except Exception:
                pass
    
    def take_hit(self, sounds):
        if self.hit_timer> 0:
            return False
        self.lives -= 1
        self.hit_timer = HIT_COOLDOWN
        try:
            sounds.hurt.play()
        except Exception:
            pass 
        if self.lives <= 0: 
            self.alive = False 
            self.actor.image = LOSE_FRAME[0]
            try: 
                sounds.gameover.play()
            except Exception:
                pass 
        return True
    def collect_coin(self, value:int, sounds):
        self.score += value 
        try: 
            sounds.coin.play()
        except Exception:
            pass
    def draw(self):
        if self.hit_timer>0 and int(self.hit_timer * 8 )% 2 == 0:
            return 
        self.actor.draw()