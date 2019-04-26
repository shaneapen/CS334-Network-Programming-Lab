#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>
                       
int main(){
 int p[2],q[2],pid;
 char str1[20],str2[20],buff[20];
 pipe(p);
 pipe(q);
 pid=fork();
 //if child
 if(pid==0){
   printf("Enter message from child to parent:");
   scanf("%s",str1);
   write(p[1],str1,sizeof(str1)); //writes to parent write end
   read(q[0],buff,sizeof(buff));  //read from child pipe's read end
   printf("Parent said: %s\n",buff);
 }else if(pid>0){ 
   read(p[0],buff,sizeof(buff));
   printf("Child said: %s",buff);
   printf("\nEnter message from parent to child:");
   scanf("%s",str2);
   write(q[1],str2,sizeof(str2));
 }
 return 0;
}
