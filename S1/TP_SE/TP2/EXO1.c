#include <stdio.h>
#include <unistd.h>
//#include <time.h>
int main() {
    int p =getpid();
    printf("debut %i\n",p);
    //clock_t start = clock(); // Record the start time.

    unsigned n= 2111111111;
    while(n--);
    //clock_t end = clock(); // Record the end time.

   // double execution_time = (double)(end - start) / CLOCKS_PER_SEC;
    printf("FIN %i\n",p);
    //printf("Execution time: %f seconds\n", execution_time);
    return 0;
}
