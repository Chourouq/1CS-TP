#include<stdio.h>
#include<stdlib.h>


int main(int argc , char *argv[]){
     int i;
     float s=0;
     if(argc<=1)exit(-1);
     else{
        for(i=1; i<argc; i++){
          s+=atof(argv[i]);
        }
     } 
     printf("%f", s/(argc-1)); 
}