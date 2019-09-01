#include "token.hpp"

Token::Token(void)
{
	std::cout << "Token is created" << std::endl;
}

Token::~Token(void)
{
	std::cout << "Destructor is called" << std::endl;
}

int Token::some_func(void)
{
    std::cout << "Hello, World!\n";

    return 1;
}