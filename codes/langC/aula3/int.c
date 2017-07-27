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
  unsigned int i = UINT_MAX;//constant in  header limits.h
  uint32_t k = UINT32_MAX;// header stdint.h. Define size 32 bits for k
  // In the headers limits.h and stdint have other constats defined
  // for integers, chars. Use $ man stdint example or 
  // locate file and view content (with $ view <file>)
  size_t s; // In header stdlib.h
  // Put l in memory of register of the machine (registers: ax,bx,...)
  // Used in variable count for loops.
  register int l = 0;
  printf("\nO tamanho de i(int): %zu bytes / %zu bits\n",sizeof i, sizeof i *8);
  printf("\nValor de i: %u\n", i);
  printf("\nValue of k: %u\n", k);

  return 0;
}
