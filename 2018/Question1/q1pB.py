debt = 100
payments = 0

interest, repay = map(lambda x: int(x), input().split())
interest /= 100
repay /= 100

while debt != 0:
    debt *= (1 + interest)
    payment = min(max(debt * repay, 50), debt)
    payments += 1
    debt -= payment

print(payments)