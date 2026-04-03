from pgzero.actor import Actor 

COIN_TYPES = {
    "gold":  ("tiles/default/coin_gold", 10),
    "silver": ("tiles/default/coin_silver", 5),
    "bronze": ("tiles/default/coin_bronze", 1),
}

class Coin: 
    def __init__(self, x:int, y:int, coin_type: str="gold"):
        entry        = COIN_TYPES.get(coin_type, ("tiles/double/coin_gold", 10))
        image        = entry[0]   
        self.value   = entry[1]   
 
        assert isinstance(image, str), f"Coin image must be a string, got {type(image)}: {image}"
        
        self.actor     = Actor(image)
        self.actor.pos = (x, y)
        self.collected = False

    def draw(self):
        if not self.collected:
            self.actor.draw()
    
    def check_collect(self, player_actor) -> bool: 
        if not self.collected and self.actor.colliderect(player_actor):
            self.collected = True
            return True
        return False