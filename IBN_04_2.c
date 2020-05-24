#include <ctype.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_INPUT_LENGTH 1024

int main(void) {

    int fd[2], n, i;
    pid_t pid;
    char zeile[MAX_INPUT_LENGTH];
    char shift_value = 2;

    if (pipe(fd) < 0) {
        fprintf(stderr, "Couldn't create pipe");
    }

    if ((pid = fork()) > 0) {

        close(fd[0]);
        fprintf(stdout, "Unencrypted: ");
        fgets(zeile, MAX_INPUT_LENGTH, stdin);
        write(fd[1], zeile, strlen(zeile));
        if (waitpid(pid, NULL, 0) < 0)
            fprintf(stderr, "Fehler bei waitpid()????");
        }

    else {

        close(fd[1]);
        n = read(fd[0], zeile, MAX_INPUT_LENGTH);
        for (i = 0; i < n; i++) {
            if (zeile[i] == '\n') {
                /* Don't convert newline character */
                continue;
            }
            printf("%i\n", zeile[i]);
            zeile[i] += shift_value;
        }
        fprintf(stderr, "Encrypted: ");
        write(STDOUT_FILENO, zeile, n);

    }
    exit(0);
}
