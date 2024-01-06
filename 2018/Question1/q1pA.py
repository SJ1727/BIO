debt = 100
amount_paid = 0

interest, repay = map(lambda x: int(x), input().split())
interest /= 100
repay /= 100

while debt != 0:
    debt *= (1 + interest)
    payment = min(max(debt * repay, 50), debt)
    amount_paid += payment
    debt -= payment

print(round(amount_paid, 2))