programa {
  funcao inicio() {
    inteiro inicio, fim, soma_pares = 0

    escreva("digite o numero inicial: ")
    leia(inicio)

    escreva("digite o numero final: ")
    leia(fim)

    para(inteiro i=inicio;i<=fim;i++){
      se(i%2 == 0){
        soma_pares = soma_pares + 1
      }
    }
    escreva("a soma dos pares é: ",soma_pares)
  }
}
