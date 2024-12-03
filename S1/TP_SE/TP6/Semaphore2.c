#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>

int compte = 100000;
sem_t semaphore;

void* threadFunc(void* arg) {
    printf("Thread Function :: Start\n");
    if (compte>=100000)
        for(int i=1;i<=100000;i++) compte--;
    sem_post(&semaphore);
    printf("Thread Function :: End\n");
    return NULL;

}

int main() {
    // Thread id
    sem_init(&semaphore, 1, 0);
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

    // Do some stuff in Main Thread
    sem_wait(&semaphore);
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
    sem_destroy(&semaphore);
    printf("Exiting Main\n");
    return 0;
}