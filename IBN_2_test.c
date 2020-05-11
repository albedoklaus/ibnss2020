#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main ()
{
	if (fork() > 0)
	{
		printf("%s %ld %ld\n", "fork>0", (long)getpid(), (long)getppid());
		sleep(1000);
	}
	else
	{
		printf("%s %ld %ld\n", "else", (long)getpid(), (long)getppid());
		exit(0);
	}
	return 0;
}
