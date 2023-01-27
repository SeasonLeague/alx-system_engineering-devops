#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * main - creates 5 zombie processes
 *
 * Return: Always 0 (Success)
 */
int main(void)
{
    pid_t pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        pid = fork();
        if (pid == 0)
        {
            printf("Zombie process created, PID: %d\n", getpid());
            _exit(0);
        }
    }
    sleep(30);
    return (0);
}
