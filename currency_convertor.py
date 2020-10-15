with open('currency_data.txt') as f:
    lines = f.readlines()

# print(lines)
dic = {}
for line in lines:
    parsed = line.split('\t')
    dic[parsed[0]] = parsed[1]
    

# print(dic)
print("\nIf you want list of currency available press Q ?")
while True: 
    data = input("\n\t\tEnter your choise : ")
    if data == "p":
        for i in dic:
            print(i)
        continue
    elif data == 'q':
        print('Thanks for uiing indian curency converter ? ')
        break
    elif type(data) == str:
        amt = int(input("Enter the amount : "))        
        print(dic[data])
        ans = float(dic[data]) * amt
        print(ans)




