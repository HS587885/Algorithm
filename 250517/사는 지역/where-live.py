n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class Person:
    def __init__(self, name, street_address, region):
        self.name = name
        self.street_address = street_address
        self.region = region

    def print_info(self):
        print(f"name {self.name}")
        print(f"addr {self.street_address}")
        print(f"city {self.region}")


people = []
for i in range(n):
    person = Person(name[i], street_address[i], region[i])
    people.append(person)

# 사전순으로 가장 뒤에 있는 이름을 가진 사람 찾기
max_person = people[0]
for p in people[1:]:
    if p.name > max_person.name:
        max_person = p

# 결과 출력
max_person.print_info()