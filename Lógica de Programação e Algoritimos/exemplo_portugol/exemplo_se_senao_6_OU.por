programa {
  funcao inicio() {
    inteiro valor_compra
    cadeia possui_cupom

    escreva("qual o valor da compra? ")
    leia(valor_compra)

    escreva("possui cupom de desconto? ")
    leia(possui_cupom)

    se(valor_compra>=200 ou possui_cupom == "sim"){
      escreva("voce ganhou um desconto de 15%!")
    }
    senao{
      escreva("infelizmente voce não ganhou cupom")
    }
  }
}
