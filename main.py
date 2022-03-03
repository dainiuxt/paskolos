from modules.loan import Loans
loans = Loans()

loans.append((100, 1000, 10, 10))
loans.append((101, 10000, 100, 7))
loans.append((102, 500, 6, 18))
loans.append((103, 100, 3, 25))
loans.append((104, 1000, 10, 10))

main_menu_items = {
  1: 'New loan',
  2: 'Loans list',
  3: 'Loan details',
  0: 'Exit'
}

def main_menu():
  for key in main_menu_items.keys():
    print(key, '-', main_menu_items[key])

def new_loan():
  l_id = int(input("Enter loan id: "))
  loan = int(input("Enter loan ammount: "))
  term = int(input("Enter loan term (months): "))
  interest = float(input("Enter yearly interest rate: "))
  loans.append((l_id, loan, term, interest))
  print(f'Loan {l_id} ammount is €{loan}, term is {term} months, yearly interest rate is {interest}%')
  return

def list_loans():
  for loan in loans.book:
    id = loan[0]
    amount = loan[1]
    term = loan[2]
    interest = loan[3]
    print(f'Loan No. {id} amount is €{amount}, term is {term} months with {interest}% interest.')

def loan_details(loan_id):
    for loan in loans.book:
      if loan[0] == loan_id:
        l_amount = loan[1]
        l_term = loan[2]
        l_int_rate = loan[3]
        down_payment = round(l_amount / l_term, 2)

    sum_string = str(f'Loan amount: €{l_amount}, yearly interest rate is {l_int_rate}%, payment term is {l_term} months.')
    period = 1
    payment_sum = 0
    prate_sum = 0
    head_str = '{:<8} {:<8} {:<12} {:<12} {:<8}'.format('Month','Balance','Down payment','Interest','Payment')
    dashline = '-----------------------------------------------------------------'
    with open(f'{loan_id}.csv', 'w') as file:
      file.write('Month, Balance, Down payment, Interest, Payment\n')
    print(f'{head_str}')
    print(dashline)
    while l_amount > 0:
      if l_amount >= down_payment:
        p_rate = round(l_amount /100 * l_int_rate / 12, 2)
        prate_sum = round(prate_sum + p_rate, 2)
        pay = round(down_payment + p_rate, 2)
        payment_sum = round(payment_sum + pay, 2)
        print('{:<8} {:<8} {:<12} {:<12} {:<8}'.format(period, l_amount,down_payment, p_rate, pay))
        with open(f'{loan_id}.csv', 'a') as file:
          file.write(f'{period}, {l_amount}, {down_payment}, {p_rate}, {pay}\n')
        l_amount = round(l_amount - down_payment, 2)
        period += 1
      else:
        down_payment = l_amount
        p_rate = round(l_amount /100 * l_int_rate / 12, 2)
        prate_sum = round(prate_sum + p_rate, 2)
        pay = round(down_payment + p_rate, 2)
        payment_sum = round(payment_sum + pay, 2)
        print(f'{period}\t|{l_amount}\t\t|{down_payment}\t\t|{p_rate}\t\t|{pay}')
        with open(f'{loan_id}.csv', 'a') as file:
          file.write(period, l_amount, down_payment, p_rate, pay)        
        l_amount = round(l_amount - down_payment)
        period += 1    
    print(dashline)
    print(sum_string)
    print(f'Total payed amount: €{payment_sum} of which interest is €{prate_sum}')

def main():
  while True:
    main_menu()
    selection = ''
    try:
      selection = int(input('Enter your selection: '))
    except ValueError:
      print("Please enter a number: ")
      continue
    if selection == 1:
      new_loan()
      continue
    elif selection == 2:
      list_loans()
      continue
    elif selection == 3:
      try:
        list_loans()
        loan_id = int(input('Enter loan id: '))
      except ValueError:
        print('Please enter a number: ')
        continue
      loan_details(loan_id)  
    elif selection == 0:
      print("Quit")
      break
    else:
      print('Select number from list!')

if __name__ == '__main__':
    main()