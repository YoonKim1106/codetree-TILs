import math

def gcd(n, m):
    return math.gcd(n, m)

if __name__ == "__main__":
    # 사용자 입력 받기
    n, m = map(int, input().split())
    
    # 최대공약수 계산
    result = gcd(n, m)
    
    # 결과 출력
    print(result)