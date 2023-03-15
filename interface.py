import pygame
import sys
from pygame.locals import *
from game_state import GameState

pygame.init()

BOARD_SIZE = 5
CELL_SIZE = 100
PIECE_SIZE = 45
WIDTH = BOARD_SIZE * CELL_SIZE
HEIGHT = BOARD_SIZE * CELL_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Symmetry Puzzles")

def place_piece(board, row, col):
	if board[row][col] != 0:
		return False
	
	while True:
		draw_board(board)
		# Draw the menu
		menu_font = pygame.font.SysFont(None, 30)
		text1 = menu_font.render("Choose a piece to place:", True, BLACK)
		text2 = menu_font.render("1 - Square", True, BLACK)
		text3 = menu_font.render("2 - Circle", True, BLACK)
		text4 = menu_font.render("3 - Triangle", True, BLACK)
		menu_width = max(text1.get_width(), text2.get_width(), text3.get_width(), text4.get_width())
		menu_height = text1.get_height() * 5
		menu_surf = pygame.Surface((menu_width, menu_height))
		menu_surf.fill(WHITE)
		menu_rect = menu_surf.get_rect()
		menu_rect.center = (WIDTH // 2, HEIGHT // 2)
		menu_surf.blit(text1, (menu_width // 2 - text1.get_width() // 2, 0))
		menu_surf.blit(text2, (menu_width // 2 - text2.get_width() // 2, text1.get_height()))
		menu_surf.blit(text3, (menu_width // 2 - text3.get_width() // 2, text1.get_height() * 2))
		menu_surf.blit(text4, (menu_width // 2 - text4.get_width() // 2, text1.get_height() * 3))
		screen.blit(menu_surf, menu_rect)
		pygame.display.flip()

		# Wait for a menu choice
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					return
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_1:
						res = gameb.put_shape([row,col], 1)
						if res == None:
							shape_not_possible()
							return
						else:
							#board = res.board
							board[row][col] = 1
						return True
					elif event.key == pygame.K_2:
						res = gameb.put_shape([row,col], 2)
						if res == None:
							return
						else:
							#board = res.board
							board[row][col] = 2
						return True
					elif event.key == pygame.K_3:
						res = gameb.put_shape([row,col], 3)
						if res == None:
							return
						else:
							#board = res.board
							board[row][col] = 3
						return True

def shape_not_possible():
	menuErro_font = pygame.font.Font(None, 30)
	error_message1 = menuErro_font.render("This shape is not present in this row or col!", True, BLACK)
	error_message2 = menuErro_font.render("You cannot use!", True, BLACK)
	menuErro_width = max(error_message1.get_width(), error_message2.get_width()) + 5
	menuErro_height = error_message1.get_height() * 3
	menuErro_surf = pygame.Surface((menuErro_width, menuErro_height))
	menuErro_surf.fill(WHITE)
	menuErro_rec = menuErro_surf.get_rect()
	menuErro_rec.center = (WIDTH // 2, HEIGHT // 2)
	menuErro_surf.blit(error_message1, (menuErro_width // 2 - error_message1.get_width() // 2, 0))
	menuErro_surf.blit(error_message2, (menuErro_width // 2 - error_message2.get_width() // 2, error_message1.get_height()))
	screen.blit(menuErro_surf, menuErro_rec)
	pygame.display.flip()

	#make the messager disapper after some time or some keystroke
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					return True

def draw_board(board):
	for i in range(BOARD_SIZE):
		for j in range(BOARD_SIZE):
			x = j * CELL_SIZE
			y = i * CELL_SIZE
			rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
			if board[i][j] == 0:
				pygame.draw.rect(screen, WHITE, rect)
				pygame.draw.rect(screen, GRAY, rect, 2)
			elif board[i][j] == 1:
				pygame.draw.rect(screen, GREEN, rect, PIECE_SIZE + 5)
				pygame.draw.rect(screen, GRAY, rect, 2)
			elif board[i][j] == 2:
				pygame.draw.circle(screen, RED, (j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2), PIECE_SIZE)
				pygame.draw.rect(screen, GRAY, rect, 2)
			else:
				pygame.draw.polygon(screen, BLUE, ((10+CELL_SIZE*j,20+CELL_SIZE*i),(90+CELL_SIZE*j,20+CELL_SIZE*i),(50+CELL_SIZE*j,80+CELL_SIZE*i)))
				pygame.draw.rect(screen, GRAY, rect, 2)


#inicializar a board com um jogo e inicializar o jogo
board = [[0, 0, 0, 1, 2], 
		 [0, 0, 0, 2, 0], 
		 [3, 3, 3, 0, 3],
		 [0, 1, 1, 0, 3],
		 [0, 0, 2, 0, 0]]

gameb = GameState(board)

while True:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			x, y = event.pos
			i = y // CELL_SIZE
			j = x // CELL_SIZE
			if i < BOARD_SIZE and j < BOARD_SIZE and board[i][j] == 0:
				place_piece(board, i, j)
	
	screen.fill(WHITE)
	draw_board(board)
	
	pygame.display.update()