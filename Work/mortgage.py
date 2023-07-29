# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000



while principal > 0:
    cur_payment = payment
    if month >= extra_payment_start_month or month <= extra_payment_end_month:
        cur_payment = payment + extra_payment

    if cur_payment > principal * (1+rate/12):
        cur_payment =  principal * (1+rate/12)
    principal = principal * (1+rate/12) - cur_payment
    total_paid = total_paid + cur_payment
    month = month + 1
    print(month, round(total_paid,4), round(principal,4))

print('Total paid', total_paid)
print('total months', month)
