#include <stdio.h>
#include <stdlib.h>
int main()
{
    system("ps u");

    int *a;
    a = (int*)malloc(sizeof(int) * 300000000);

    printf("%p\n", a);

    system("ps u");

    free(a);

    system("ps u");

}