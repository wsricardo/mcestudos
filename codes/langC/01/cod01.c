#include<stdio.h>
#include<string.h>
#include<stdlib.h>


int main(int argc, char *argv[])
{
    int count = 0, age, dd, mm, yy;
    char name[10];

    printf("\nDigite seu nome: ");
    scanf(" %s", name);
    printf("\nDigite sua data de nascimento(dd/mm/yy): ");
    scanf(" %d/%d/%d", &dd, &mm, &yy);
    printf("\nDigite dua idade: ");
    scanf(" %d", &age);

    printf("\n\tDados\n\tNome: %s\n\tData de Nascimento: %d/%d/%d\n\tIdade: %d \n", name, dd, mm, yy, age);

    return 0;

}