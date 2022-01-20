# Tran Phuong Minh Pham, tranppha@usc.edu
# ITP 115, Fall 2021
# Section: Bagel
# Assignment 8
# Description: create a tic-tac-toe game for 2 players with 3 x 3 board

import TicTacToeHelper


def isValidMove(boardList, spot):
    while spot < 0 or spot > 8:
        return False
    if boardList[spot] == "x" or boardList[spot] == "o":
        return False
    return True


def updateBoard(boardList, spot, playerLetter):
    boardList[spot] = playerLetter


def playGame(player1, player2):
    boardList = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    moves = 0
    winner = "n"
    while winner == "n":
        TicTacToeHelper.printPrettyBoard(boardList)
        if moves % 2 == 1:
            player = player2
        else:
            player = player1
        selection = int(input("\nPlayer " + player + ", pick a spot: "))
        while isValidMove(boardList, selection) is False:
            selection = int(input("\nPlayer " + player + ", pick a spot: "))
        updateBoard(boardList, selection, player)
        moves += 1
        winner = TicTacToeHelper.checkForWinner(boardList, moves)
    TicTacToeHelper.printPrettyBoard(boardList)
    print("\nGame over!")
    if winner == "x" or winner == "o":
        print("Player", winner, "is the winner!")
    if winner == "s":
        print("Stalemate reached!")


def main():
    print("Welcome to Tic Tac Toe")
    new_game = "y"
    while new_game == "y":
        player_select = input("Please select who will go first (x or o): ")
        player1 = None
        player2 = None
        if player_select == "x":
            player1 = "x"
            player2 = "o"
        elif player_select == "o":
            player1 = "o"
            player2 = "x"
        playGame(player1, player2)
        new_game = input("\nWould you like to play another round? (y or n): ")
        new_game = new_game.lower()
    else:
        print("Goodbye!")


main()
