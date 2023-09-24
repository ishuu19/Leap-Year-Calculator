# Leap year Calender

year = int(input('Enter your year:'))

if year%4==0:
    
    if year%100 !=0 and year/100 and year/400:
        print('Leap Year')
    else:
        print('Not a Leap Year')

else:
    print('Not a Leap Year')
