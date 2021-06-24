print('*********************************NUMBER TO WORD CONVERTION**********************************')
print('\t\t\t  Program By : - "M.K. MAHOR (MONU)"')
print()
num=int(input('Enter Any Number IN BETWEEN 1 TO 999999999: '))
ones={0:'',1:'ONE',2:'TWO',3:'THREE',4:'FOUR',5:'FIVE',6:'SIX',7:'SEVEN',8:'EIGHT',9:'NINE',10:'TEN',
      11:'ELEVEN',12:'TWELVE',13:'THIRTEEN',14:'FOURTEEN',15:'FIFTEEN',16:'SIXTEEN',17:'SEVENTEEN',
       18:'EIGHTEEN',19:'NINTEEN'}
    
xth={0:'',2:'TWENTY',3:'THIRTY',4:'FORTY',5:'FIFTY',6:'SIXTY',7:'SEVENTY',8:'EIGHTY',9:'NINTY'}

Hundred={0:'HUNDRED',1:'ONE HUNDRED',2:'TWO HUNDRED',3:'THREE HUNDRED',4:'FOUR HUNDRED',5:'FIVE HUNDRED',6:'SIX HUNDRED',
         7:'SEVEN HUNDRED',8:'EIGHT HUNDRED',9:'NINE HUNDRED',10:'TEN HUNDRED',11:'ELEVEN HUNDRED',
         12:'TWELVE HUNDRED',13:'THIRTEEN HUNDRED',14:'FOURTEEN HUNDRED',15:'FIFTEEN HUNDRED',
         16:'SIXTEEN HUNDRED',17:'SEVENTEEN HUNDRED',18:'EIGHTEEN HUNDRED',19:'NINTEEN HUNDRED'}

thousand={0:'THOUSAND',1:'ONE THOUSAND',2:'TWO THOUSAND',3:'THREE THOUSAND',4:'FOUR THOUSAND',
          5:'FIVE THOUSAND',6:'SIX THOUSAND',7:'SEVEN THOUSAND',8:'EIGHT THOUSAND',
          9:'NINE THOUSAND',10:'TEN THOUSAND',11:'ELEVEN THOUSAND',12:'TWELVE THOUSAND',13:'THIRTEEN THOUSAND',
          14:'FOURTEEN THOUSAND',15:'FIFTEEN THOUSAND',16:'SIXTEEN THOUSAND',17:'SEVENTEEN THOUSAND',
          18:'EIGHTEEN THOUSAND',19:'NINTEEN THOUSAND'}

Lakh={0:'LAKH',1:'ONE LAKH',2:'TWO LAKH',3:'THREE LAKH',4:'FOUR LAKH',5:'FIVE LAKH',6:'SIX LAKH',7:'SEVEN LAKH',
      8:'EIGHT LAKH',9:'NINE LAKH',10:'TEN LAKH',11:'ELEVEN LAKH',12:'TWELVE LAKH',13:'THIRTEEN LAKH',
      14:'FOURTEEN LAKH',15:'FIFTEEN LAKH',16:'SIXTEEN LAKH',17:'SEVENTEEN LAKH',18:'EIGHTEEN LAKH',
      19:'NINTEEN LAKH'}

if num > 0 and num < 20:
    if num in ones:
        print(ones[num])
        
elif num > 19 and num <100:
    tenth=num//10
    one=num%10
    output=xth[tenth]+' '+ones[one]
    print(output)

elif num > 100 and num <1000:
    hundred=num//100
    a=num%100
    if a<20:
        output=Hundred[hundred]+' '+ones[a]
        
    else:
        tenth=a//10
        one=a%10
        output=Hundred[hundred]+' '+xth[tenth]+' '+ones[one]
    print(output)

elif num>999 and num<100000:
    #99999
    a=num//1000
    b=num%1000     #999
    hundred=b//100
    c=b%100
    tenth=c//10
    one=c%10
    if a<20:
        thousand1=a//10
        thousand2=a%10
        if c<20:
            output=thousand[a]+' '+Hundred[hundred]+' '+ones[c] 
        else:
            output=thousand[a]+' '+Hundred[hundred]+' '+xth[tenth]+' '+ones[one]
        
    else:
        thousand1=a//10
        thousand2=a%10
        if c<20:
            output=xth[thousand1]+' '+thousand[thousand2]+' '+Hundred[hundred]+' '+ones[c]
        else:
            output=xth[thousand1]+' '+thousand[thousand2]+' '+Hundred[hundred]+' '+xth[tenth]+' '+ones[one]
    print(output)

elif num > 99999 and num < 10000000:
    #9999999
    a=num//100000
    b=num%100000     #99999
    c=b//1000       #99
    thousand1=c//10
    thousand2=c%10
    d=b%1000        #999
    hundred=d//100
    e=d%100         #99
    tenth=e//10
    one=e%10   
    if a<20:
        if e<20:
            output=ones[a]+' '+xth[thousand1]+' '+thousand[thousand2]+' '+Hundred[hundred]+' '+ones[e] 
        else:
            output=Lakh[a]+' '+xth[thousand1]+' '+thousand[thousand2]+' '+Hundred[hundred]+' '+xth[tenth]+' '+ones[one]
    else:
        lakh1=a//10
        lakh2=a%10
        if e<20:
            output=xth[lakh1]+' '+Lakh[lakh2]+' '+xth[thousand1]+' '+thousand[thousand2]+' '+Hundred[hundred]+' '+ones[e]
        else:
            output=xth[lakh1]+' '+Lakh[lakh2]+' '+xth[thousand1]+' '+thousand[thousand2]+' '+Hundred[hundred]+' '+xth[tenth]+' '+ones[one]
    print(output)
    
    
elif num > 9999999 and num < 1000000000:
    #999999999
    carore=num//10000000
    b=num%10000000      #9999999
    c=b//100000         #99
    lakh10=c//10
    lakh=c%10
    th=num%100000       #99999 last five digit
    tho=th//1000
    thousand1=tho//10
    thousand2=tho%10
    d=num%1000          #last 3 digit 999
    hundred=d//100
    e=num%100           #last 2 digit 99
    tenth=e//10
    one=e%10
    if carore<20:
        if e < 20:
            output=ones[carore]+' '+'CARORE'+' '+xth[lakh10]+' '+Lakh[lakh]+' '+xth[thousand1]+' '+thousand[thousand2]+' '+Hundred[hundred]+' '+ones[e]
        else:
            output=ones[carore]+' '+'CARORE'+' '+xth[lakh10]+' '+Lakh[lakh]+' '+xth[thousand1]+' '+thousand[thousand2]+' '+Hundred[hundred]+' '+xth[tenth]+' '+ones[one]
    else:
        carore10=carore//10
        carore1=carore%10
        if e < 20:
            output=xth[carore10]+' '+ones[carore1]+' '+'CARORE'+' '+xth[lakh10]+' '+Lakh[lakh]+' '+xth[thousand1]+' '+thousand[thousand2]+' '+Hundred[hundred]+' '+ones[e]
        else:
            output=xth[carore10]+' '+ones[carore1]+' '+'CARORE'+' '+xth[lakh10]+' '+Lakh[lakh]+' '+xth[thousand1]+' '+thousand[thousand2]+' '+Hundred[hundred]+' '+xth[tenth]+' '+ones[one]
    
    print(output)    
else:
    print('Enter number not in range')
print('\t\t\t\t\t\t\tTHANK YOU FROM :- M.K. MAHOR(MONU)') 
 

    
    

