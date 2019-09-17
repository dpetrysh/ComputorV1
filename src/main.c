#include <stdio.h>
#include "token.h"

// head means starting element in the list
t_tok *head = NULL;

int parse_args(int ac, char **av, t_tok **list)
{
    if (ac < 2 || av == NULL)
        return 1;

    while (*av)
    {
        if (check_token(*av))
            return 1;

        av++;
    }

    return 0;
}

int main(int ac, char **av)
{
    if (parse_args(ac, av, NULL))
        printf("Sorry...your equation isn't valid\n");

    t_tok *list;
    parse_args(ac, av, &list);

    return 0;
}
    