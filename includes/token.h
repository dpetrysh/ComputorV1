#ifndef TOKEN_H
# define TOKEN_H

int check_token(char *str);

typedef enum e_token_type
{
	IS_SIGN = 0,
	IS_LITERAL,
	IS_VARIABLE
} token_type;

typedef struct s_tok
{
    struct s_tok    *next;
    token_type      type;
    char            sign;
    double          value;
    int             pow;
} t_tok;

#endif