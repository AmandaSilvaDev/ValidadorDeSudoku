<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Validador de Sudoku em Python usando Threads</h1>

<p>Este é um programa simples em Python que utiliza threads para validar a solução de um jogo de Sudoku. Ele verifica se as linhas, colunas e blocos 3x3 do tabuleiro estão preenchidos corretamente, sem repetição de números de 1 a 9.</p>

<h2>Funcionalidades</h2>

<ol>
    <li><strong>Validação de Linhas:</strong> A função LinhaValid verifica se cada linha do Sudoku está corretamente preenchida, sem repetição de números.</li>
    <li><strong>Validação de Colunas:</strong> A função ColValid verifica se cada coluna do Sudoku está corretamente preenchida, sem repetição de números.</li>
    <li><strong>Validação de Blocos 3x3:</strong> A função x3Valid verifica se cada bloco 3x3 do Sudoku está corretamente preenchido, sem repetição de números.</li>
    <li><strong>Validação do Sudoku Completo:</strong> As funções validateSudokuL, validateSudokuC, validateSudoku3 e validateSudoku utilizam threads para validar as linhas, colunas, blocos 3x3 e o tabuleiro completo do Sudoku, respectivamente.</li>
</ol>

<h2>Uso</h2>

<ol>
    <li>Modifique a matriz do Sudoku dentro do código para representar o jogo que deseja validar.</li>
    <li>Execute o script Python.</li>
    <li>O programa utilizará threads para realizar a validação do Sudoku, exibindo mensagens indicando se cada parte do tabuleiro está correta ou não.</li>
</ol>

<h2>Exemplo de Sudoku Válido (inicializado no código)</h2>

<p>O código inclui um exemplo de um Sudoku válido. Modifique a matriz de acordo com o jogo que deseja validar.</p>

<h2>Requisitos</h2>

<p>O código utiliza o módulo threading e time da biblioteca padrão do Python.</p>

<h2>Contribuição</h2>

<p>Contribuições são bem-vindas! Sinta-se à vontade para propor melhorias, relatar problemas ou enviar pull requests para este projeto.</p>

</body>
</html>
