programa {
  funcao inicio() {
    inteiro lado1, lado2, lado3

    escreva("digite o primeiro lado")
    leia(lado1)

    escreva("digite o segundo lado")
    leia(lado2)

    escreva("digite o terceiro lado")
    leia(lado3)

    se(lado1 == lado2 e lado2 == lado3 e lado1 == lado3){
      escreva("é um triangulo equilátero")
    }
    senao se(lado1==lado2 != lado3){
      escreva("isóceles")
    }
    senao se (lado1 != lado2 != lado3){
      escreva("é um triangulo escaleno")
    }

  }
}

