n = int(input())
name = []
height = []
weight = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
    def show(self):
        print()

person = []
for i in range(len(name)):
    p = Person(name[i], height[i], weight[i])
    person.append(p)

person.sort(key=lambda x: (x.height, -x.weight)) 
for human in person: 
    print(human.name, human.height, human.weight)
