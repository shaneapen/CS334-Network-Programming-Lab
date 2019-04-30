// C Program for Message Queue (Writer Process) 
#include <stdio.h> 
#include <sys/ipc.h> 
#include <sys/msg.h> 
  
// structure for message queue 
struct mesg_buffer { 
    long mesg_type; 
    char mesg_text[100]; 
} message; 

int p;
  
int main() 
{ 
    key_t key; 
    int msgid; 
    key = IPC_PRIVATE; 
    msgid = msgget(key, 0666 | IPC_CREAT); 
    p = fork();

   if(p==0){
        msgrcv(msgid, &message, sizeof(message), 2, 0); 
        printf("\nInside Child Process\nReceived message:%s\n",message.mesg_text);
    }else if(p>0){
        printf("Inside Parent Process");
        printf("\nSend message to child: "); 
        gets(message.mesg_text);
        message.mesg_type = 2; 
        msgsnd(msgid, &message, sizeof(message), 0);  
    } 
    return 0; 
} 