class Animation:
    def __init__(self, frames:list, fps: int = 8):
        self.frames = frames
        self.fps = fps
        self._indexer = 0
        self._timer = 0.0

    def update(self,dt:float):
        self._timer +=dt
        frame_duration = 1.0 / self.fps
        while self._timer >=frame_duration:
            self._timer -= frame_duration
            self._index = (self._indexer + 1) % len(self.frames)
    
    def current_frame(self) -> str:
        return self.frames[self._indexer]  
    
    def reset(self):
        self._indexer = 0 
        self._timer = 0.0