Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/04/2024
Var
// Seção de Declarações das variáveis 
   nome : caractere
   idade : inteiro
   primeiraNota : real
   segundaNota : real
   terceiraNota : real
   media : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   escreval("=== Solicitando dados para o usuário ===")
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
   escreval("Média: ", media)

   escreval("=== Verificando maioridade ===")
   se media >= 7 entao
      escreval("Aprovado!")
   senao
      escreval("Reprovado!")
   fimse

Fimalgoritmo