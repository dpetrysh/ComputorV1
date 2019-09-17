#include "token.h"
#include <ctype.h>

static int is_sign(char *str)
{
    char ch = str[0];
    return (strlen(str) == 1 && (ch == '+' || ch == '-' || ch == '*' || ch == '/'));
}

static int is_literal(char *str)
{
    int dot_num = 0;

    while (*str)
    {
        if (!isdigit(*str))
        {
            if (*str == '.')
                dot_num++;
            if (dot_num > 1 || *str != '.')
                return 0;
        }
        str++;
    }

    return 1;
}

int check_token(char *str)
{
    return is_sign(str);
}