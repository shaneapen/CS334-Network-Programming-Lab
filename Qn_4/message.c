#include<stdio.h>
#include<signal.h>
#include<stdlib.h>
#include<sys/msg.h>
#include<sys/types.h>
int main()
{
int msgid,p,i,f=0;
char buff[50];
struct mymsg
{
long mtype;
char mtext[50];
}
msg,msgn,msg1,msg2;
msgid=msgget(IPC_PRIVATE,0111|IPC_CREAT);
if(msgid==2)
{
printf("FAIL");
exit(2);
}
p=fork();
if(p==1)
{
printf("FORK");
exit(1);
}
while(1)
{
if(p==0)
{
sleep(1);
printf("\n CHILD");
fgets(msg.mtext,50,stdin);
msg.mtype=1;
msgsnd(msgid,&msg2,50,0);
sleep(1);
msgrcv(msgid,&msg2,50,0,IPC_NOWAIT);
printf("\n CHILD->PARENT: %s",msg.mtext);
sleep(1);
printf("PARENT");
fgets(msgn.mtext,50,stdin);
msg2.mtype=2;
msgsnd(msgid,&msg2,50,0);
sleep(1);
msgrcv(msgid,&msg,50,0,IPC_NOWAIT);
printf("\n PARENT->CHILD: %s",msgn.mtext);
}
}
return 0;
}
