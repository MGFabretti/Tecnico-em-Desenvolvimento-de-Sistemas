programa {
  funcao inicio() {
   inteiro idade

   escreva("digite sua idade: ") 
   leia(idade)

   se(idade >=0 e idade <=12){
    escreva("você é criança")
   }

   senao se(idade >=13 e idade <=17){
    escreva("você é adolecente")
   }
   senao se(idade >=18 e idade <=59){
    escreva("você é adulto")
   }
   senao se(idade >=60 e idade <=100){
    escreva("você é idoso")
   }
   senao se (idade >=101){
    escreva("você é um cadaver")
   }

  }
}
