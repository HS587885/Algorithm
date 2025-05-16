unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class Code:
    def __init__(self,unlock_code, wire_color, seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds
    
    def show(self):
        print(f"code : {self.unlock_code}")
        print(f"color : {self.wire_color}") 
        print(f"second : {self.seconds}")

    
code1 = Code(unlock_code, wire_color, seconds)
code1.show()