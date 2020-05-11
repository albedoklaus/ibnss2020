#include <stdlib.h>
#include <stdio.h>

int main ()
{
	if (fork() > 0)
	{
		printf("%s\n", "fork > 0");
		printf("%ld %ld", (long)getpid(), (long)getppid());
		printf("\n");
		sleep(1000);
	}
	else
	{
		printf("%s\n", "else");
		printf("%ld %ld", (long)getpid(), (long)getppid());
		exit(0);
	}
	return 0;
}
