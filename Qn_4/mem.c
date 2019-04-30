#include<stdio.h>
#include<sys/ipc.h>
#include<sys/shm.h>
int main(){
    int p;
    char *str;
    int shmid;
    key_t key;
    //generare unique key. You can also use ftok('filename',id) to generate key 
    key = IPC_PRIVATE;
    shmid = shmget(key,1000,0666|IPC_CREAT);     //shmget(key,size,flag)
    p = fork();
    str = (char *)shmat(shmid,0,0);

    if(p==0){
        printf("\nInside Child Process\nShared memory id:%d\nShared memory content: %s\n",shmid,str);
         
        shmdt(str);     //detach from shared memory  
        shmctl(shmid,IPC_RMID,NULL);  // destroy the shared memory 
     
    }else if(p>0){
        sprintf(str,"HELLO WORLD"); //sprintf is used to write string to a variable
        printf("\nInside Parent Process\nShared memory id:%d\nShared memory content: %s\n",shmid,str);
    }

    return 0;
}
