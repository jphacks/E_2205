#include <stdio.h>
#include <math.h>
void Hello(int i)
{
    char c;
    switch (i)
    {
    case 0:
        c = 'h'; break;
    case 1:
        c = 'e'; break;
    case 2:
        c = 'l'; break;
    case 3:
        c = 'o'; break;
    default:c = 0; break;
    }
    printf("%c", c);
}

int main(void) {
    for (int i = 0; i < 4096; ++i)
    {
        for (int j = 0; j < 6; ++j)
        {
            int temp = i / pow(4, j);
            temp %= 4;
            Hello(temp);
        }
        printf("\n");

    }
    printf("hello\n");

    return 0;
}