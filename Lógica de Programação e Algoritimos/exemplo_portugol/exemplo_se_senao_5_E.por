programa {
  funcao inicio() {
    inteiro idade 
    cadeia possui_cnh

    escreva("digite sua idade: ")
    leia(idade)

    escreva("você tem CNH? ")
    leia(possui_cnh)

    se(idade>=18 e possui_cnh == "sim"){
      escreva("pode dirigir!")
    }
    senao{
      escreva("voce não pode dirigir!")
    }
  }
}
