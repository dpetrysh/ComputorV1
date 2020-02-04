class Validator():
    def __init__(self, equation):
        print("from Validator constructor " + equation)

    def check_for_equal(self, nod_list):
        for node in nod_list:
            if node == "=":
                return True
        return False
    
    def min_or_plus(self, ch):
        return ch == "+" or ch == "-"

    def prepared_symbol(self, ch):
        return self.min_or_plus("ch") or (ch == "x") or (ch == "X") or (ch == "^") or (ch.isdigit()) or (ch == ".") or (ch == "*")
