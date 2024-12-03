#include <stdio.h>
#include <unistd.h>
int main(){
 int i;
 for(i=0;i<3;i++){
   fork();
   printf("Hello world\n");
 }
    return 0;










}