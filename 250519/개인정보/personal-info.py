n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


    def in_show(self):
        print()

person = []
for i in range(len(name)):
    p = Person(name[i], height[i], weight[i])
    person.append(p)

person.sort(key=lambda x: x.name) 
print("name")
for human in person: 
    print(human.name, human.height, human.weight)
   
print()
print("height")
person.sort(key=lambda x: -x.height) 
for human2 in person: 
    print(human2.name, human2.height, human2.weight)