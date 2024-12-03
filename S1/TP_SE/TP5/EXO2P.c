#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <semaphore.h>
#include <fcntl.h>
#include <string.h>
char tampon[6];
int main(int argc, char *argv[]) {
    sem_t *sem;
    pid_t pid;
    int fd;
    // Création du sémaphore
    sem = sem_open("/my_semaphore", O_CREAT | O_EXCL, 0644, 0);
    if (sem == SEM_FAILED) {
        perror("Erreur lors de la création du sémaphore");
        return EXIT_FAILURE;
    }
    if (argc > 1) {
        pid = fork();

        if (pid == 0) { // Processus fils
            printf("Fils : J'ai commencé mon exécution.\n");
            fd = open(argv[1], O_RDWR | O_CREAT | O_TRUNC, 0644);
            write(fd, "fils\n", 5);
            sleep(2);
            printf("Fils : Attente du sémaphore pour reprendre l'exécution...\n");
            sem_wait(sem); // Attente du signal du père (sémaphore)
            printf("Fils : Exécution reprise, je continue...\n");
            // Ajoutez ici le code que vous souhaitez exécuter dans le processus fils après avoir repris
            read(fd, tampon, 5);
            printf("Le fils lit : %s\n",tampon);
            sem_close(sem);
        } else if (pid > 0) { // Processus père
            // Ajoutez ici le code que vous souhaitez exécuter dans le processus père avant de libérer le sémaphore
            sleep(1);
            fd = open(argv[1], O_RDWR);
            read(fd, tampon, 5);
            printf("Le père lit : %s\n",tampon);
            write(fd, "pere", 5);
            close(fd);
            printf("Père : Libération du sémaphore pour le fils...\n");
            sem_post(sem); // Libération du sémaphore pour le fils
            wait(NULL); // Attente de la fin du fils

            printf("Père : Exécution terminée.\n");

            sem_close(sem);
            sem_unlink("/my_semaphore"); // Suppression du sémaphore
        } else {
            perror("Erreur lors de la création du processus fils");
            return EXIT_FAILURE;
        }
    } else {
        fprintf(stderr, "Usage: %s <texte>\n", argv[0]);
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}

