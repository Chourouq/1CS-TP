#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/wait.h>
#include<fcntl.h>
#include<semaphore.h>
int main(int argc, char* argv[])
{
    FILE* index;
    char* c = (char*) calloc(100,sizeof(char));
    char* cc = (char*) calloc(100,sizeof(char));
    pid_t pid;
    index = fopen(argv[1],"r+");
    pid = fork();
    if (pid > 0)
    {
        sleep(1);
        fseek(index,-5,SEEK_CUR);
        fread(cc,1,5,index);
        printf("%d\t%s\n",pid,cc);
        fwrite("pere\n",1,5,index);
        fclose(index);
    }
    else if (pid == 0)
    {
        fwrite("fils\n",1,5,index);
        fflush(index);
        sleep(2);
        fseek(index,-5,SEEK_CUR);
        fread(c,1,5,index);
        printf("%d\t%s\n",pid,c);
        fclose(index);
    }
    return 0;
}