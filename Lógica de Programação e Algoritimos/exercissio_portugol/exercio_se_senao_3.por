programa {
  funcao inicio() {
    inteiro numero

    escreva("digite um dia")
    leia(numero)

    se(numero == 1){
      escreva("segunda")
    }
    senao se(numero == 2){
      escreva("terça")
    }
    senao se(numero == 3){
      escreva("quarta")
    }
    senao se(numero == 4){
      escreva("quinta")
    }
      senao se(numero == 5){
        escreva("sexta")
      }
      senao se(numero == 6){
        escreva("sabado")
      }
      senao se(numero == 7){
        escreva("domingo")
      }
      senao{
        escreva("esse dia não existeeeee")
      }
    }
  }
}
