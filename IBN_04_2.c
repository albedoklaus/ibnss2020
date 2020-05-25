#include <sys/wait.h>
#include <sys/types.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define BUFSIZE 1024

int main(void) {

    int fd[2];
    int n;
    int i;

    pid_t cpid;

    char buf[BUFSIZE];
    char lower_bound = 32;
    char upper_bound = 126;
    char interval_size = upper_bound - lower_bound + 1;

    char shift_value = 5;

    if (pipe(fd) < 0) {
        perror("Error creating pipe");
        exit(EXIT_FAILURE);
    }

    if ((cpid = fork()) < 0) {
        perror("Error forking");
        exit(EXIT_FAILURE);
    }

    if (!cpid) {
        /* Child process */
        n = read(fd[0], buf, BUFSIZE);
        for (i = 0; i < n; i++) {
            if (buf[i] < lower_bound || buf[i] > upper_bound) {
                /* Do not convert these characters */
                continue;
            }
            buf[i] = ((int) buf[i] - lower_bound + shift_value) % interval_size + lower_bound;
        }
        write(fd[1], buf, strlen(buf));
        _exit(EXIT_SUCCESS);
    }

    printf("Unencrypted: ");
    fgets(buf, BUFSIZE, stdin);
    write(fd[1], buf, strlen(buf));

    /* Wait for child process */
    if (waitpid(cpid, NULL, 0) < 0) {
        perror("Error waiting for child process");
        exit(EXIT_FAILURE);
    }

    n = read(fd[0], buf, BUFSIZE);
    printf("%s%s", "Encrypted: ", buf);

    exit(EXIT_SUCCESS);

}
