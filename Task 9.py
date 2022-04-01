print('========================Task9.1===============================')
print('Clock')
#hours=  '60 minute'
#minutes= '60 sec'
#seconds=  3600
#hour
print('Clock')
#hour
while True:
   h= 1
   while h<=12:
       print('One hour',h)
       h=h+1
#minute
       m=1
       while m<=60:
        print("minutes",m)
        m = m+1
# seconds
        s = 1
        while s<=60:
          print("Seconds",s)
          s =s+1
print('=============================Task9.2===================================')
car = "_|'''''''''|_\n"\
     "|______|"
a =1
while a<=10:
    print(car.rjust(90))
    run =1
    while run <=10:
        print(car.rjust(90))
        run = run +1
    a = a +1
    d = 1
    while d<=1:
        print('car is movin downside')
        d = d+1
print('===================task9.4================')
while True:
  print('Welcome to  money exchanger office')
  user = input('you want to exchange your currency yes or no:\n')
  if user =='yes':
    pass
  elif user =='no':
    break

  print('which currency you want to change')
  a = 'euro'
  b  = 'dollar'
  c = 'pkr'
  d = 'INR'
  e = 'yen'
  customer = input('select the currency')
  if customer==a:
    print('in which currency ')
    accountant = input('euro ,dollar,pkr,inr,yen')
    if accountant=='dollar':
     print('your process is complete')
    elif accountant =='pkr':
        print('your process is complete')
    elif accountant =='INR':
        print('your process is complete')
    elif accountant == 'yen':
        print('your process is complete')
    else:
        print('sorry sir')
  elif customer == b:
    print('in which currency')
    accountant = input('euro ,pkr,inr,yen')
    if accountant =='euro':
       print('your process is complete')
    elif accountant == 'pkr':
        print('your process is complete')
    elif accountant == 'INR':
        print('your process is complete')
    elif accountant == 'yen':
        print('your process is complete')
    else:
        print('sorry sir')
  elif customer==c:
    print('in which currency')
    accountant = input('euro ,dollar,pkr,yen')
    if accountant == 'euro':
        print('your process is complete')
    elif accountant == 'dollar':
        print('your process is complete')

    elif accountant == 'yen':
        print('your process is complete')
    else:
        print('sorry sir')
  elif customer==d:
    print('in which currency')
    accountant = input('euro ,dollar,pkr,inr,yen')
    if accountant == 'euro':
        print('your process is complete')
    elif accountant == 'dollar':
        print('your process is complete')
    elif accountant == 'INR':
        print('your process is complete')
    elif accountant == 'yen':
        print('your process is complete')
    else:
        print('sorry sir')
  elif customer==e:
    print('in which currency')
    accountant = input('euro ,dollar,pkr,inr,yen')
    if accountant == 'euro':
        print('your process is complete')
    elif accountant == 'dollar':
        print('your process is complete')
    elif accountant == 'INR':
        print('your process is complete')

    else:
        print('sorry sir')
        print('Thank you for coming')






