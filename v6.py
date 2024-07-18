class Messages:
    def __init__(self, len, p, p2):
        self.len = len
        self.p1 = p
        self.p2 = p2

    def print_info(self, message):
        len_m = len(message)

        if len_m <= self.len:
            result = self.p1
            return result
        else :
            result = self.p2
            return result


my_text = Messages(20, "50", "100")
print(my_text.print_info("message"))
