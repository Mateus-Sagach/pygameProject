from code.Const import ENTITY_SPEED
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Item(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
