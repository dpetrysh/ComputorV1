NAME = computor
SRC := $(wildcard src/*.c)
SRO := $(notdir $(patsubst %.c, %.o, $(SRC)))
VPATH := src includes

all: $(NAME)

$(NAME): $(SRO)
	gcc $^ -o $(NAME)

%.o : %.c
	gcc -c -I ./includes/ $< -Wall -Wextra -Werror 

clean:
	/bin/rm -f $(SRO)

fclean: clean
	/bin/rm -f $(NAME)

re: fclean all