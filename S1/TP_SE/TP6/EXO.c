#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>
int compte=100000;
void* threadFunc(void *arg)
{
    printf("Thread Function :: Start\n");
    if (compte>=100000)
        for(int i=1;i<=100000;i++) compte--;
    printf("Thread Function End\n");
    return NULL;
}
int main() {
// Thread id
     pthread_t threadId;
// Create a thread that will function threadFunc()
int err = pthread_create(&threadId, NULL, &threadFunc, NULL);
// Check if thread is created sucessfuly
   if (err)

    {
        printf("Thread creation failed: %s\n",strerror(err));
        return err;

    } else
       printf("Thread Created with ID: %lu\n", (unsigned long)threadId);


// Do some stuff in Main Thread
    for(int i=1;i<=10000;i++) compte++; printf("Waiting for thread to exit\n");
// Wait for thread to exit
    err = pthread_join(threadId, NULL);
// check if joining is sucessful
     if (err) {
         printf("Failed to join Thread: %s\n",strerror(err));
         return err;
     }
     printf("solde: %d\n",compte);
     printf("Exiting Main\n");
     return 0;
}
