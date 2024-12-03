#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/wait.h>
#include<fcntl.h>
int main(int argc, char* argv[])
{
  int index;
  char* c = (char*) calloc(100,sizeof(char));
  char* cc = (char*) calloc(100,sizeof(char));
  pid_t pid;
  pid = fork();
  index = open(argv[1],O_RDWR);
  if (pid > 0)
  {
     write(index,"Pere\n",5);
     sleep(2);
     read(index,cc,5);
     printf("%d\t%s\n",pid,cc);
  }
  if (pid == 0)
  {
     sleep(1);
     read(index,c,5);
     printf("%d\t%s\n",pid,c);
     write(index,"fils\n",5);
  }
 close(index);
 return 0;
}
