#include"vetor.h"

void add(Vetor v, Vetor u, Vetor *w)
{
    w->x = v.x + u.x;
    w->y = v.y + u.y;
}