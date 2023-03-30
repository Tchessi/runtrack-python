# Créer un programme qui modélise un plateau de jeu, carré, de n x n cases. Placez sur ce
# plateau n dames de jeu d'échecs, de manière à ce qu’aucune dame ne puisse se
# “prendre”, quand cela est possible. La valeur de n est renseignée par l’utilisateur. Quand
# cela est possible, le programme devra afficher dans le terminal le plateau de jeu avec le
# caractère ‘O’ pour les cases vides et le caractère ‘X’ pour représenter les dames.

def solve_n_queens(n):
    # Initialisation du plateau de jeu
    board = [['O' for i in range(n)] for j in range(n)]
    
    def is_safe(board, row, col):
        # Vérifie si une dame est attaquée par une autre dame
        for i in range(col):
            if board[row][i] == 'X':
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'X':
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 'X':
                return False
        return True
    
    def solve(board, col):
        # Résout le problème en utilisant le backtracking
        if col >= n:
            return True
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 'X'
                if solve(board, col+1):
                    return True
                board[i][col] = 'O'
        return False
    
    if solve(board, 0):
        # Affiche le plateau de jeu
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=' ')
            print()
    else:
        print("Pas de solution trouvée.")
n = int(input("Entrez la taille du plateau de jeu : "))
solve_n_queens(n)