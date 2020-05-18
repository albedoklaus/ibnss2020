#include <stdio.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <stdlib.h>

int main() {
  int i, shmID, *shared_mem, count=0, total=0,rnd;
  shmID = shmget(IPC_PRIVATE, sizeof(int), IPC_CREAT | 0644);
  // shmget() returns the identifier of the System V shared memory segment
  // associated with the value of the argument key.

  shared_mem = (int*)shmat(shmID,0,0);
  // shmat() attaches the shared memory segment identified by
  // shmid to the address space of the calling process.

  *shared_mem = 0;
  if (fork())
    for (i=0; i<500; i++){
      *shared_mem+=1;
      printf("\n Elternprozess: %i", *shared_mem);
      sleep(2);
    }
  else
    for (i=0; i<500;i++){
      *shared_mem+=1;
      printf("\n Kindprozess: %i", *shared_mem);
      rnd=rand();
      sleep(rnd%3);
    }
  shmdt(shared_mem);
  // shmdt() detaches the shared memory segment located at the address
  // specified by shmaddr from the address space of the calling process.

  shmctl(shmID, IPC_RMID, 0);
  // shmctl() performs the control operation specified by cmd on the
  // System V shared memory segment whose identifier is given in shmid.

  return 0;
}








