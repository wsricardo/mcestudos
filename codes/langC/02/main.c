#include<stdio.h>
#include<stdlib.h>
#include"vetor.h"

int main(int argc, char *argv[]){
    Vetor u, v,w;
    u.x = 1.0f; u.y = 2.0f;
    v.x = 0.0f; v.y = -1.0f;
    w.x = 0.0f; w.y = 0.0f;
    add(u,v, &w);
    printf("\n w:= u + v = [ %.6f, %.6f ] + [ %.6f, %.6f ]", u.x,u.y, v.x,v.y );
    printf("\n\t [ %.6f, %.6f ]\n", w.x,w.y);

    return 0;
}
