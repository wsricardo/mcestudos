#include<stdio.h>
#include<stdlib.h>

struct vetor2D{
    float x;
    float y;
};

// Outra forma de declarar tipo vetor
typedef struct vetor{
    float x;
    float y;
}Vect;

typedef struct vetor2D Vector;
//typedef struct Vect Vector2D;

int main(int argc, char *argv[])
{
    Vector v;
    v.x=0.0f; v.y=0.0f;
    printf("\nv := \n\t ( %.8f, %.8f )", v.x, v.y);
    printf("\n");

    return 0;
}