#include<stdio.h>
#include<stdlib.h>

int main(void){
    int whatToDo = 0;
    do{
        printf("\nMENU\n");
        
        printf("\n 1. Novo");
        printf("\n 2. Abrir");
        printf("\n 3. Salvar");
        printf("\n 4. Sair\n");
        
        printf("\n:");
        scanf(" %d",&whatToDo);
        
        // Escolhas de opção 'switch'
        switch(whatToDo){
        case 1:
            printf("\n Novo arquivo\n");
            break;
        case 2:
            printf("\n Abir arquivo\n");
            break;
        case 3:
            printf("\n Salvar arquivo\n");
            break;
        case 4:
            printf("\n Sair\n");
            exit(0);
        default:
            printf("\n Opção errada...\n");
            //exit(0);
        }
    }while(whatToDo>1 || whatToDo < 4);
    
    
            
    
    print("\nBye\n");
    return 0;
}
