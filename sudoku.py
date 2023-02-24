import threading
import time

matriz = []

#validar linhas
def LinhaValid(linha_num):
    #vai retornar a quantidade em set(sem repet) dentro das linhas
    #caso não tiver numeros repitidos dentro da linha retorna true, else false
    #considerando que o usuario não coloque valores maiores de 9 e menores que 1
    return len(set(matriz[linha_num])) == 9

#validar colunas
def ColValid(col_num):
    #vai retornar a quantidade em set(sem repet) dentro das colunas
    #caso não tiver numeros repitidos dentro da coluna retorna true, else false
     #considerando que o usuario não coloque valores maiores de 9 e menores que 1
    col = [item[col_num] for item in matriz]
    return len(set(col)) == 9

#validar 3x
def x3Valid(x3_lin, x3_col):
    #pega primeira linha e todas suas colunas e vai add em vals.
    #caso não tiver numeros repitidos dentro da coluna retorna true, else false#caso não tiver numeros repitidos dentro da coluna retorna true, else false
    vals = matriz[x3_lin][x3_col: x3_col+3]
    vals.extend(matriz[x3_lin+1] [x3_col: x3_col+3])
    vals.extend(matriz[x3_lin+2] [x3_col: x3_col+3])
    return len(set(vals)) == 9

#validate sudoku
def validateSudokuL():
    for i in range(0,9):
        print("SUDOKU LINHA EM ANÁLISE") 
        if not LinhaValid(i):
            print("SUDOKU LINHA INVÁLIDO")
            return False
    print("SUDOKU LINHA VÁLIDO")
    return True        
def validateSudokuC(): 
    for i in range(0,9): 
        print("SUDOKU COLUNA EM ANÁLISE")      
        if not ColValid(i):
            print("SUDOKU COLUNA INVÁLIDO")
            return False
    print("SUDOKU COLUNA VÁLIDO")
    return True
def validateSudoku3():
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            print("SUDOKU 3X EM ANÁLISE")
            if not x3Valid(i, j):
                print("SUDOKU 3X INVÁLIDO")
                return False
    print("SUDOKU 3X VÁLIDO")
    return True

def validateSudoku():
    for i in range(0,9):
        if not LinhaValid(i):
            print("SUDOKU INVÁLIDO!!!!!")
            return False
        if not ColValid(i):
            print("SUDOKU INVÁLIDO!!!!!")
            return False  
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not x3Valid(i, j):
                print("SUDOKU INVÁLIDO!!!!!")
                return False  
    print("SUDOKU VÁLIDO!!!!!")
    return True


#criando matriz
for i in range(9):
    matriz.append([])
for l in range(9):
    for c in range(9):
        matriz[l].append(0)

#sudoku valores
#modificar por dentro do cod
#exemplo de sudoku válido
matriz[0][0] = 6
matriz[0][1] = 9
matriz[0][2] = 4
matriz[0][3] = 5
matriz[0][4] = 3
matriz[0][5] = 9
matriz[0][6] = 1
matriz[0][7] = 8
matriz[0][8] = 7

matriz[1][0] = 5
matriz[1][1] = 1
matriz[1][2] = 9
matriz[1][3] = 7
matriz[1][4] = 2
matriz[1][5] = 8
matriz[1][6] = 6
matriz[1][7] = 3
matriz[1][8] = 4

matriz[2][0] = 8
matriz[2][1] = 3
matriz[2][2] = 7
matriz[2][3] = 6
matriz[2][4] = 1
matriz[2][5] = 4
matriz[2][6] = 2
matriz[2][7] = 9
matriz[2][8] = 5

matriz[3][0] = 1
matriz[3][1] = 4
matriz[3][2] = 3
matriz[3][3] = 8
matriz[3][4] = 6
matriz[3][5] = 5
matriz[3][6] = 7
matriz[3][7] = 2
matriz[3][8] = 9

matriz[4][0] = 9
matriz[4][1] = 5
matriz[4][2] = 8
matriz[4][3] = 2
matriz[4][4] = 4
matriz[4][5] = 7
matriz[4][6] = 3
matriz[4][7] = 6
matriz[4][8] = 1

matriz[5][0] = 7
matriz[5][1] = 6
matriz[5][2] = 2
matriz[5][3] = 3
matriz[5][4] = 9
matriz[5][5] = 1
matriz[5][6] = 4
matriz[5][7] = 5
matriz[5][8] = 8

matriz[6][0] = 3
matriz[6][1] = 7
matriz[6][2] = 1
matriz[6][3] = 9
matriz[6][4] = 5
matriz[6][5] = 6
matriz[6][6] = 8
matriz[6][7] = 4
matriz[6][8] = 2

matriz[7][0] = 4
matriz[7][1] = 9
matriz[7][2] = 6
matriz[7][3] = 1
matriz[7][4] = 8
matriz[7][5] = 2
matriz[7][6] = 5
matriz[8][7] = 7
matriz[7][8] = 3

matriz[8][0] = 2
matriz[8][1] = 8
matriz[8][2] = 5
matriz[8][3] = 4
matriz[8][4] = 7
matriz[8][5] = 3
matriz[8][6] = 9
matriz[8][7] = 1
matriz[8][8] = 6

#Thread
threading.Thread(target=validateSudokuL).start()

threading.Thread(target=validateSudokuC).start()

threading.Thread(target=validateSudoku3).start()

time.sleep(1)

threading.Thread(target=validateSudoku).start()