import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_WHITE, GAME_TITLE, C_YELLOW, SCORE_POS, MENU_OPTION
from code.DBProxy import DBProxy


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)  # parametro -1 faz a musica tocar infinitamente
        db_proxy = DBProxy('DBScore')
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # primeiro desenha o background depois desenha o texto
            self.score_text(48, 'YOU WIN!!!', C_YELLOW, SCORE_POS['Title'])
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Enter Player 1 name (4 characters):'
            if game_mode == MENU_OPTION[1]:
                score = (player_score[0]+player_score[1]) / 2
                text = 'Enter Team name (4 characters):'

            if game_mode == MENU_OPTION[2]:
                if player_score[0] > player_score[1]:
                    score = player_score[0]
                    text = 'Enter Player 1 name (4 characters):'
                if player_score[1] > player_score[0]:
                    score = player_score[1]
                    text = 'Enter Player 2 name (4 characters):'
                if player_score[1] == player_score[0]:
                    score = player_score[0]
                    text = 'Enter Player 1 and 2 name together (4 characters ):'



            pygame.display.flip()
            pass


    def show(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)  # parametro -1 faz a musica tocar infinitamente
        self.window.blit(source=self.surf, dest=self.rect)  # primeiro desenha o background depois desenha o texto
        while True:
            pygame.display.flip()
            pass

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)