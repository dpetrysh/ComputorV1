#ifndef TOKEN_H
# define TOKEN_H

#include <iostream>

class Token 
{
public:
    Token(void);
    ~Token(void);

    int some_func();

private:
    int is_sign;
    int is_member;
    int power;
}; 

#endif