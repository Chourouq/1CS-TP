#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int i;
    float s = 0.0;
    float min, max;

    if (argc <= 1) {
        printf("No arguments provided.\n");
        exit(-1);
    } else {
        min = max = atof(argv[1]);

        for (i = 1; i < argc; i++) {
            float current = atof(argv[i]);

            if (current < min) {
                min = current;
            }

            if (current > max) {
                max = current;
            }

            s += current;
        }

        printf("lastprog calcuated the minimum ,the maximum and the sum of the array ,and found:min=%f \t max=%f \t sum=%f ", min, max,s);
        
    }

    return 0;
}





