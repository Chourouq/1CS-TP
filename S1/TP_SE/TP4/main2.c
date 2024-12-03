#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
char tampon [6];
int main (int argc, char* argv[])
{
    int fd;
    pid_t pid;
    if ((fd = open ("toto.txt", O_RDONLY)) <0) return EXIT_FAILURE;
    pid = fork (); sleep (1);
    if (pid == -1) {
        perror(" failed");
    } else if (pid == 0) {
        if (read(fd, tampon, 5) < 0) {
            perror("Error");
            close(fd);
            return EXIT_FAILURE;
        }
        tampon[5] = '\0';
        printf("Child: %s\n", tampon);
    } else {
        wait(NULL);
        if (read(fd, tampon, 5) < 0) {
            perror("Error");
            close(fd);
            return EXIT_FAILURE;
        }
        tampon[5] = '\0';
        printf("Parent: %s\n", tampon);
    }
    close(fd);
    return EXIT_SUCCESS;
}