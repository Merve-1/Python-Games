from screens.Menu import MenuScene
from screens.SceneOne import GameScene
import pgzrun
WIDTH = 800
HEIGHT = 600
TITLE = "Mr CAINE Mission"


current_scene = None
def _load_menu():
    global current_scene
    current_scene = MenuScene(screen,sounds)

def _load_game():
    global current_scene
    current_scene = GameScene(screen,sounds)

def draw():
    global current_scene
    if current_scene is None:
        _load_menu()
    screen.clear()
    current_scene.draw()

def update(dt):
    if current_scene is None:
        return 
    if isinstance(current_scene, GameScene):
        current_scene.update(dt,keyboard)

def on_mouse_down(pos):
    if current_scene is None: 
        return 
    result = current_scene.handle_click(pos)
    if result == "scene1":
        _load_game()
    elif result == "restart":
        _load_game()
    elif result == "quit":
        quit()


def on_key_down(key):
    if isinstance(current_scene, GameScene):
        current_scene.on_key_down(key)

pgzrun.go()