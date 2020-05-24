#include <ctype.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_INPUT 1024

int main(void) {

    int fd[2];
    int n;
    int i;
    pid_t pid;
    char input[MAX_INPUT];
    char shift_value = 2;

    if (pipe(fd) < 0) {
        fprintf(stderr, "Error creating pipe");
    }

    /* Parent process */
    if ((pid = fork()) > 0) {

        close(fd[0]);
        printf("Unencrypted: ");
        fgets(input, MAX_INPUT, stdin);
        write(fd[1], input, strlen(input));

        /* Wait for child process */
        if (waitpid(pid, NULL, 0) < 0) {
            perror("Error waiting for child process");
            exit(1);
        }
        close(fd[1]);
        strcpy(input, "abc\n");
        n = read(fd[0], input, MAX_INPUT);
        printf("%s%s", "Encrypted: ", input);

    }

    /* Child process */
    else {

        close(fd[1]);
        n = read(fd[0], input, MAX_INPUT);
        /*sleep(3);*/
        for (i = 0; i < n; i++) {
            if (input[i] == '\n') {
                /* Don't convert newline character */
                continue;
            }
            printf("%i\n", input[i]);
            input[i] += shift_value;
        }
        printf("%s%s", "Encrypted: ", input);
        close(fd[0]);
        write(fd[1], input, strlen(input));


    }

    exit(0);

}
