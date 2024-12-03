#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int i, j=0, p;
    if (argc>=2)
        for (i=0;i<5;i++)
        {
            p=fork();
            if (p==0) {j=j-1;printf("Je suis le processus fils numéro : %d\n", i+1);}
            else if (p>0) {
                wait(NULL);
                j=j+1;
                printf("Je suis un processus père, mon résultat est : %d\n", j);
                exit(1);}
        }
    return 0;
}