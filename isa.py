#!/usr/bin/env python

# Income Share Agreement


min = 50000.0
max = 88235.3
max_pay = 30000.0
max_income = 2117647.06

monthly_increment = (max - min)/23

print('\n24 months maximum payment with a minimum of $50,000 annual income')
print('Maximum  income for 24 month repayment is $88,235.30\n')
print('For incomes exceeding $88,235.30 see chart below,\nfor reduced payback period on $30,000 repayment cap')

print('\nmonth\tannual_income\tless_isa\tmonthly\t\tless_isa\tmonthly_payment\n')

for n in range(24):
    print(
        "%d\t%.2f\t%.2f\t%.2f\t\t%.2f\t\t%.2f" % (n+1, (min+(n*monthly_increment)), (min+(n*monthly_increment))*0.83, (min+(n*monthly_increment))/12, (min+(n*monthly_increment))*0.83/12, ((min+(n*monthly_increment))/12) - (min+(n*monthly_increment))*0.83/12 
    ))

print('\n')
print('$30,000 Maximum Shared Income\n')


print('total\t\tannual\t\tmonthly\npayments\tincome\t\tpayment\n')

for n in range(24,0,-1):
    print('%d\t\t%.2f\t%.2f' % (n, max/(max*n/max_income), max_pay/n))

print('\n')
