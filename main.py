import pygame
from console2048 import *
from board import Board

score = 0
open("score.txt", "w").write("")


def main():
    global score
    pygame.init()
    size = 500, 900
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('2048: Colors')

    board = Board(4, 4)
    board.set_view(50, 200, 100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                s0 = 0
                s1 = 0
                for i in range(4):
                    for j in range(4):
                        s0 += newmp[i][j]
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and not(gameover()):
                    put_down()
                if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and not(gameover()):
                    put_right()
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and not(gameover()):
                    put_up()
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and not(gameover()):
                    put_left()
                for i in range(4):
                    for j in range(4):
                        s1 += newmp[i][j]

                f = open("score.txt", "r")
                line = f.readline()
                if line != '':
                    score = int(line) + s1 - s0
                f.close()
                f = open("score.txt", "w")
                f.write(str(score))
                f.close()
                if score > int(open("best_score.txt", "r").readline()):
                    open("best_score.txt", "w").write(str(score))

            if event.type == pygame.MOUSEBUTTONUP:
                x_pos = event.pos[0]
                y_pos = event.pos[1]
                if 50 <= x_pos <= 150 and 625 <= y_pos <= 725:
                    board.index = 0
                elif 200 <= x_pos <= 300 and 625 <= y_pos <= 725:
                    board.index = 1
                elif 350 <= x_pos <= 450 and 625 <= y_pos <= 725:
                    board.index = 2
                elif 125 <= x_pos <= 225 and 750 <= y_pos <= 850:
                    board.index = 3
                elif 275 <= x_pos <= 375 and 750 <= y_pos <= 850:
                    board.index = 4

            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        board.render(screen)
        board.draw(screen)
        if gameover():
            pygame.draw.rect(screen, (54, 54, 54), (45, 195, 405, 405))
            font = pygame.font.Font("ClearSans-Bold.ttf", 75)
            text1 = font.render("Игра", True, (255, 255, 255))
            text2 = font.render("Окончена!", True, (255, 255, 255))
            text3 = font.render(f"Счёт: {score}", True, (255, 255, 255))
            screen.blit(text1, (160, 200))
            screen.blit(text2, (60, 275))
            screen.blit(text3, (75, 475))
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
