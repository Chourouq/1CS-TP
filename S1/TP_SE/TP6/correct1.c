#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>

int compte = 100000;
int threadReady = 0;

void* threadFunc(void* arg) {
    printf("Thread Function :: Start\n");

    // Indique que le thread est prêt
    threadReady = 1;

    if (compte >= 100000)
        for (int i = 1; i <= 100000; i++)
            compte--;

    printf("Thread Function End\n");
    return NULL;

}

int main() {
    // Thread id
    pthread_t threadId;

    // Create a thread that will function threadFunc()
    int err = pthread_create(&threadId, NULL, &threadFunc, NULL);

    // Check if thread is created successfully
    if (err) {
        printf("Thread creation failed: %s\n", strerror(err));
        return err;
    } else
        printf("Thread Created with ID: %lu\n", (unsigned long)threadId);

    // Attente active : attend que le thread soit prêt
    while (!threadReady) {
        // Peut-être ajouter une pause courte pour éviter le surutilisation du processeur
        usleep(1000); // Pause d'un milliseconde
    }

    // Do some stuff in Main Thread
    for (int i = 1; i <= 10000; i++)
        compte++;

    printf("Waiting for thread to exit\n");

    // Wait for thread to exit
    err = pthread_join(threadId, NULL);

    // check if joining is successful
    if (err) {
        printf("Failed to join Thread: %s\n", strerror(err));
        return err;
    }

    printf("solde: %d\n", compte);

    printf("Exiting Main\n");
    return 0;
}
