Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/04/2024
Var
// Se��o de Declara��es das vari�veis 
   nome : caractere
   idade : inteiro
   primeiraNota : real
   segundaNota : real
   terceiraNota : real
   media : real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   escreval("=== Solicitando dados para o usu�rio ===")
   escreva("Digite seu nome: ")
   leia(nome)
   
   escreva("Digite sua idade: ")
   leia(idade)
   
   escreva("Digite sua primeira nota: ")
   leia(primeiraNota)
   
   escreva("Digite sua segunda nota: ")
   leia(segundaNota)
   
   escreva("Digite sua terceira nota: ")
   leia(terceiraNota)

   media <- (primeiraNota + segundaNota + terceiraNota) / 3

   escreval("=== Exibindo resultado ===")
   escreval("Nome: ", nome)
   escreval("Idade: ", idade)
   escreval("M�dia: ", media)

   escreval("=== Verificando maioridade ===")
   se media >= 7 entao
      escreval("Aprovado!")
   senao
      escreval("Reprovado!")
   fimse

Fimalgoritmo