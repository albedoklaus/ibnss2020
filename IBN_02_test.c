#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

/*int main ()
{
	if (fork() > 0)
	{
		printf("%s %ld %ld\n", "fork>0", (long)getpid(), (long)getppid());
		sleep(10);
	}
	else
	{
		printf("%s %ld %ld\n", "else", (long)getpid(), (long)getppid());
		exit(0);
	}
	return 0;
}
*/
int main ()
{
	if (fork() > 0)
	{
		for (int i = 0; i < 10; i++)
		{
			printf("%s %d\n", "parent", i);
			sleep(1);
			int a = 5;
			printf("%d",a);
		}
	}
	else
	{
		for (int i = 0; i < 10; i++)
		{
			printf("%s %d\n", "child", i);
			sleep(1);
			int a = 1;
		}
		//exit(0);
	}
	return 0;
}
