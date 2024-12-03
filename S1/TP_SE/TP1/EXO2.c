#include <stdio.h>  // Include the necessary header for printf and FILE
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    // Check if the program was called with the correct number of arguments
    if (argc < 2) {
        printf("Error: Not enough arguments\n");
        exit(-1);
    }

    // Open a file for writing
    FILE *file = fopen("result.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        exit(-1);
    }

    // Get the input string from the command line argument
    char *inputString = argv[1];

    // Loop through the input string and print each character on a new line
    for (int i = 0; i < strlen(inputString); i++) {
        printf("%c\n", inputString[i]);       // Display character on the screen
        fprintf(file, "%c\n", inputString[i]); // Write character to the file
    }

    // Close the file
    fclose(file);

    return 0;
}
