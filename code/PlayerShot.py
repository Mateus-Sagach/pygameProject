from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple, owner: str, shot_type: str):
        super().__init__(name, position)
        self.owner = owner
        self.shot_type = shot_type

    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.shot_type+"Shot"]

