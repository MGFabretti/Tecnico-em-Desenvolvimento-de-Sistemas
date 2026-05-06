programa {
  funcao inicio() {
   inteiro numero1, numero2

   escreva("digite o primeiro numero: ") 
   leia(numero1)

   escreva("digite o segundo numero: ")
   leia(numero2)

   se (numero1 > numero2){
    escreva("numero1 > numero2")
   }
   senao se(numero2 > numero1){
    escreva("numero2 > numero1")
   }
   senao se(numero1 == numero2){
    escreva("os numeros são iguais")
   }
  }
}
