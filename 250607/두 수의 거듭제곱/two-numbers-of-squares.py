from multiprocessing import Pool

def f(args):
    a, b = args
    return a ** b

if __name__ == "__main__":
    a, b = map(int, input().split())

    with Pool(4) as p:
        # [(a, b)] 하나의 작업만 있지만 구조적으로 여러 개 처리 가능
        result = p.map(f, [(a, b)])
    
    print(result[0])
