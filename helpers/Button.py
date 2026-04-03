class Button:
    def __init__(self, label, rect, color,screen,fontsize=30):
        self.label = label
        self.rect = rect
        self.color = color
        self.screen = screen 
        self.fontsize = fontsize

    def draw(self):
        self.screen.draw.filled_rect(self.rect, self.color)
        self.screen.draw.text(
            self.label,
            center=self.rect.center,
            color="white",
            fontsize=self.fontsize,

        )
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)