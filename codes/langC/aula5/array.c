/*
 * Aulas: "Programação Moderna em C"
 * Site/Youtube Channel: Mente Binária 
 *
 */

#include<stdio.h>
#include<limits.h>
#include<stdint.h>
#include<stdlib.h>

int main(void) {
  //constant in  header limits.h
  // header stdint.h. Define size 32 bits for k
  // In the headers limits.h and stdint have other constats defined
  // for integers, chars. Use $ man stdint example or 
  // locate file and view content (with $ view <file>)
  //float f = 3e2; //3 * 10^2
  //
  char c[3];
  char *p=NULL;
  
  printf("\nO tamanho de c é: %zu\n", sizeof c);
  printf("\nO numero de elementos de c eh: %zu\n", sizeof c/sizeof c[0]);
  printf("\nO valor do ponteiro p inicializado: %p\n",p);
  c[0] = 'A';
  c[1] = 0x42;
  c[2] = 67;
  p = &c[0];// O ponteiro p aponta para o endereço de memória do primeiro elemento do array de char c
  printf("\nO elemento 1 de c eh: %d \n",c[0]);
  printf("\nO elemento 2 e c eh: %d \n",c[1]);
  printf("\nO elemento 3 e c eh: %d \n\n",c[2]);
  printf("\nAgora ponteiro p (p=&c[0]) aponta para endereço de c[0]");
  printf("\nO endereço do ponteiro p aponta é: %p\n", p);
  printf("\nO endereço do ponteiro p (&p)  é: %p\n", &p);

  printf("\nO endereço do array  c em memoria  eh: %p \n",c);
  printf("\nO endereço do array  &c em memoria  eh: %p \n",&c);
  printf("\nO endereço do array  c[0] em memoria  eh: %p \n",&c[0]);
  printf("\nO endereço do array  c[1] em memoria  eh: %p \n",&c[1]);
  printf("\nO endereço do array  c[2] em memoria  eh: %p \n",&c[2]);

  
  return 0;
}
