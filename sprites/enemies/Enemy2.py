from pgzero.actor import Actor 
from helpers.Animation import Animation 


ENEMY_SPEED = 200
GROUND_Y = 520

WALK_FRAMES= [
    "enemies/default/slime_block_walk_a",
    "enemies/default/slime_block_walk_b"
]

class Enemy2:
    def __init__(self, x:int, y:int, patrol_left:int, patrol_right:int):
        self.actor = Actor(WALK_FRAMES[0])
        self.actor.pos = (x,y)
        self.patrol_left= patrol_left
        self.patrol_right= patrol_right
        self.direction = -1
        self._anim = Animation(WALK_FRAMES, fps = 8)

    def update(self, dt:float):
        self.actor.x += ENEMY_SPEED * self.direction *dt 
        if self.actor.x <= self.patrol_left:
            self.actor.x = self.patrol_left 
            self.direction = 1
        elif self.actor.x >= self.patrol_right:
            self.actor.x = self.patrol_right
            self.direction = -1
        self._anim.update(dt)
        self.actor.image = self._anim.current_frame()

    def draw(self):
        self.actor.draw()

    def collides_with(self, player_actor) -> bool:
        return self.actor.colliderect(player_actor)