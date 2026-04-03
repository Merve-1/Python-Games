class Background:
    @staticmethod
    def draw_background(screen):
        screen.blit('backgrounds/double/background_solid_sky',  (0,   0))
        screen.blit('backgrounds/double/background_solid_sand', (0,   400))
        screen.blit('backgrounds/double/background_solid_sky',  (400, 0))
        screen.blit('backgrounds/double/background_solid_sand', (300, 400))