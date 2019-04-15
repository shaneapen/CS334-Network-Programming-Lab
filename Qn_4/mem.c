#include<stdio.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<sys/ipc.h>
#include<sys/shm.h>
int main(int argc,char *argv[])
{
int p;
char *shm,*shm2;
int shmid;
key_t key;
key=IPC_PRIVATE;
shmid=shmget(key,1000,0666|IPC_CREAT);
p=fork();
if(p==0)
printf("Shared memory=%d \n",shmid);
shm=(char *)shmat(shmid,0,0);
if(p>0)
printf("shared memory(parent)=%d \n",shmid);
sprintf(shm,"running \n");
printf("Shared memory content:PROCESS:%s",shm);
return 0;
}
