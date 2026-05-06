programa {
  funcao inicio() {
  real area, volume, raio, altura, pi = 3.14

  escreva("digite o raio: ") 
  leia(raio) 

  escreva("digite a altura: ")
  leia(altura)

  area = 2*pi*raio*(raio+altura)
  escreva("\n Área = ", area)

  volume = pi*raio*raio*altura
  leia("\n volume = ", volume)


  }
}
