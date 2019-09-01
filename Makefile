NAME = computor
SRC := $(wildcard src/*.cpp)
SRO := $(notdir $(patsubst %.cpp, %.o, $(SRC)))
VPATH := src includes

all: $(NAME)

$(NAME): $(SRO)
	g++ $^ -o $(NAME)

%.o : %.cpp
	g++ -c -I ./includes/ $< -Wall -Wextra -Werror 

clean:
	/bin/rm -f $(SRO)

fclean: clean
	/bin/rm -f $(NAME)

re: fclean all