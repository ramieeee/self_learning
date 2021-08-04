def solution(price, money, count):
    acc = 0
    
    for i in range(count + 1):
        acc = acc + price * i
    if money > acc:
        return 0
    return acc - money
