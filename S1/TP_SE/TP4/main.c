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
switch (pid)
{
case-1:
return EXIT_FAILURE;
case 0:
printf("Iam the child:");
read (fd, tampon,5);
break;
default:
wait(NULL);
printf("Iam the parent:");
read (fd, tampon,5);
}
sleep (1); printf ("%s\n", tampon ); close (fd);
return EXIT_SUCCESS;
}
