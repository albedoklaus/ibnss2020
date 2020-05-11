#include <stdlib.h>

int main ()
{
	if (fork() > 0)
	{
		printf("%s\n", "fork > 0");
		sleep(1000);
	}
	else
	{
		printf("%s\n", "else");
		exit(0);
	}
	return 0;
}
