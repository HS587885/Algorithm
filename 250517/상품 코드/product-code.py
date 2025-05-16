product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class Product:
    def __init__(self, product_name, product_code):
        self.product_name = product_name
        self.product_code = product_code
        
    
    def show(self):
        print(f"product {self.product_code} is {self.product_name}")
        

code1 = Product("codetree", 50)
code2 = Product(product_name, product_code)
code1.show()
code2.show()

