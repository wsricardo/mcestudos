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
  float f = 1;
  long double d = 1;

  printf("\nO tamanho de f(float): %zu bytes / %zu bits\n",sizeof f, sizeof f *8);
  printf("\nO tamanho de d(long double): %zu bytes / %zu bits\n", sizeof d, sizeof d *8);

  printf("\nValor de i: %f\n ~ %.2f ", f, f);

  return 0;
}
