#!/usr/bin/env python3
import sys


def main():
    game = NoughtsAndCrosses()

    print('Input a square from 1-9 to move.')

    while not game.finished():
        try:
            print(game.turn + ' to play: ', end='')
            sys.stdout.flush()
            action = sys.stdin.readline()
            game.move(action)
            game.display()
        except KeyboardInterrupt:
            return
        except:
            print('Invalid position')

    game.display_result()


class NoughtsAndCrosses:
    def __init__(self):
        self.turn = 'X'
        self.position = [None, None, None, None, None, None, None, None, None]

    def move(self, action):
        position = int(action)

        if self.position[position - 1]:
            print('Square already occupied')
            return

        self.position[position - 1] = self.turn

        if self.turn == 'O':
            self.turn = 'X' 
        else:
            self.turn = 'O'

    def finished(self):
        if self.winner():
            return True

        for square in self.position:
            if not square:
                return False
        return True

    def winner(self):
        for player in ['X', 'O']:
            # Rows
            for i in range(3):
                win = True
                for j in range(3):
                    if self.position[i*3+j] != player:
                        win = False
                        break
                if win:
                    return player

            # Columns
            for i in range(3):
                win = True
                for j in range(3):
                    if self.position[i+j*3] != player:
                        win = False
                        break
                if win:
                    return player

            # Diagonals
            if (self.position[0] == player 
                    and self.position[4] == player 
                    and self.position[8] == player):
                return player
            if (self.position[2] == player 
                    and self.position[4] == player 
                    and self.position[6] == player):
                return player

        return None

    def display(self):
        for i in range(3):
            for j in range(3):
                print(self.position[i*3 + j] or ' ', end='')
                if j < 2:
                    print('|', end='')
            print()

    def display_result(self):
        winner = self.winner()
        if winner:
            print(winner + ' wins!')
        else:
            print('Draw')


if __name__ == '__main__':
    main()
