#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

int compte = 100000;
sem_t semaphore;

void* threadFunc(void* arg) {
    printf("Thread Function :: Start\n");

    // Attendez que le sémaphore soit posté (déverrouillé)
    sem_wait(&semaphore);

    if (compte >= 100000)
        for (int i = 1; i <= 100000; i++)
            compte--;

    printf("Thread Function End\n");

    // Poste (déverrouille) le sémaphore pour signaler la fin de la tâche
    sem_post(&semaphore);

    return NULL;
}

int main() {
    // Thread id
    pthread_t threadId;

    // Initialiser le sémaphore avec une valeur initiale de 0
    sem_init(&semaphore, 0, 0);

    // Create a thread that will function threadFunc()
    int err = pthread_create(&threadId, NULL, &threadFunc, NULL);

    // Check if thread is created successfully
    if (err) {
        printf("Thread creation failed: %s\n", strerror(err));
        return err;
    } else
        printf("Thread Created with ID: %ld\n", threadId);

    // Attendez que le sémaphore soit posté (déverrouillé) par le thread créé
    sem_wait(&semaphore);

    // Do some stuff in Main Thread
    for (int i = 1; i <= 10000; i++)
        compte++;

    printf("Waiting for thread to exit\n");

    // Poste (déverrouille) le sémaphore pour permettre au thread créé de se terminer
    sem_post(&semaphore);

    // Wait for thread to exit
    err = pthread_join(threadId, NULL);

    // check if joining is successful
    if (err) {
        printf("Failed to join Thread: %s\n", strerror(err));
        return err;
    }

    printf("solde: %d\n", compte);

    // Détruire le sémaphore une fois qu'il n'est plus nécessaire
    sem_destroy(&semaphore);

    printf("Exiting Main\n");
    return 0;
}
