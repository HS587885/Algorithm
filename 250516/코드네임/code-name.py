MAX_N = 5

class Codename:
    def __init__(self, name, score):
        self.name = name
        self.score = score

# Codename 객체들을 저장할 리스트
agents = []

# 입력받기
for _ in range(MAX_N):
    name, score = input().split()
    agents.append(Codename(name, int(score)))

# 가장 점수가 낮은 요원 찾기
min_agent = agents[0]
for agent in agents[1:]:
    if agent.score < min_agent.score:
        min_agent = agent

# 결과 출력
print(min_agent.name, min_agent.score)
