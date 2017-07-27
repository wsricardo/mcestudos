#include<stdio.h>
#include<stdbool.h>

int main(void){
  bool b;
  //Outro caminho [antigo] antes stdbool.h
  char c;
  c = 0; //falso
  c = 1; //verdadeiro

  b = false;
  
  //Em printf, %lu -> long unsigned [tipo] p/ exibir.
  printf("\nTamanho de b (bool) eh: %lu\n",sizeof b);

  printf("\nO valor de b eh: %i\n",b);

  return 0;

}
