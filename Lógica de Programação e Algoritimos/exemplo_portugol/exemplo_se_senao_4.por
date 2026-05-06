programa {
  funcao inicio() {
    cadeia operacao
    inteiro num1, num2
    real resultado

    escreva("digite a operção (+,-,*,/): ")
    leia(operacao)

    escreva("digite o primeiro número: ")
    leia(num1)

    escreva("digite o segundo número: ")
    leia(num2)
    
    se(operacao == "+"){
      resultado = num1 + num2
    }
    senao se(operacao == "-"){
      resultado = num1 - num2
    }
    senao se(operacao == "*"){
      resultado = num1 * num2
    }
    senao se(operacao == "/"){
      resultado = num1 / num2
    }
    senao{
      escreva("operação inválida!")
    }

    escreva("o resultado é: ", resultado)
  }
}
