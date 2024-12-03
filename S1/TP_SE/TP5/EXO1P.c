#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include<string.h>
#include<sys/wait.h>
#include <fcntl.h>
char tampon[6];
int main (int argc, char *argv[]){
 int fd;
 pid_t pid;
 if (argc > 1){
   fd = open(argv[1],O_RDWR | O_CREAT | O_TRUNC,0644);
   if (fd == -1){
     perror("Erreur lors de l'ouverture du fichier");
     return EXIT_FAILURE;
   }
   printf("Je suis le pere\n");
   write(fd,"pere\n",5);
   pid = fork();
   if (pid == 0) {
      sleep(1);
     fd = open(argv[1], O_RDWR);//On Reouvere ici pour forcer le fils de revenir a la premier ligne du fichier si on fait pas ca il va trouver le vide.
     read(fd, tampon, 5);
     printf("Le fils lit: %s\n",tampon);
     write(fd, "fils\n", 5);
     close(fd);
   }
   else if (pid > 0){
      sleep(2);
       wait (NULL); //Attendre la fin du fils
       read(fd, tampon, 5);
       printf("Le père lit: %s\n", tampon);
       close(fd);}
      else{
         perror("Erreur lors de la création du processus fils");
         return EXIT_FAILURE;
      }
}
 else {
     fprintf(stderr,"Usage:%s<texte>\n",argv[0]);
     return EXIT_FAILURE;
 }
 return EXIT_FAILURE;
}