/*
 *  Author: Wandeson Ricardo
 *  Blog: wanartsci.blogspot.com
 *  gaenos.wordpress.com
 * Correções feitas no código de acordo com comentários e 
 * linhas de comando comentadas
 * Links (fonte para correções):
 * https://www.ime.usp.br/~pf/algoritmos/aulas/io.html
 * https://programacaodescomplicada.wordpress.com/2013/01/08/aula-81-limpar-o-buffer/
 * http://www.cprogressivo.net/2012/12/Buffer--o-que-e-como-limpar-e-as-funcoes-fflush-e-fpurge.html
 *
 *
 */
#include<stdio.h>
#include<stdlib.h>

int main(void){
  char cmd;

  for(;;){
    printf("/$ ");
    //setfbuf(stdin,NULL);//limpar buffer colando valor NULL em 'stdin'.
    scanf(" %c",&cmd); //espaço antes de %c pode previni funcionamento incorreto, executando 'default' em todos os 'casos'.
    //fflush(stdin); // limpando buffer.

    if (cmd=='q') exit(0);
    switch(cmd){
      case 'h':
        printf("Ajuda prompt.... Comandos");
        break;
      case 'v':
        printf("Version 0.1");
        break;
      case 'e':
        printf("echo");
        break;
      default:
        printf("Syntax comand error!");
    } 
  printf("\n");
  }

  return 0;

}
