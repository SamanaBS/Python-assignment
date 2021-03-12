while True: 
	try: 
		B = float(input("Enter your budget : ")) 
		t = B 
	except ValueError: 
		print("PRINT NUMBER AS A AMOUNT") 
		continue
	else: 
		break

a ={"name":[], "quant":[], "price":[]} 

b = list(a.values()) 

name = b[0] 

quantity = b[1] 

product = b[2] 

while True: 
	try: 
		ch = int(input("1.ADD\n2.EXIT\nEnter your choice : ")) 
	except ValueError: 
		print("\nERROR: Choose only digits from the given option") 
		continue
	else: 
		if ch == 1 and t>0:	 

			pn = input("Enter product name : ") 
			q = input("Enter quantity : ") 
			p = float(input("Enter price of the product : ")) 

			if p>t: 
				print("\nCAN, T BUT THE PRODUCT") 
				continue

			else: 
				if pn in name: 
					ind = name.index(pn) 

					quantity.remove(quantity[ind]) 

					product.remove(product[ind]) 

					quantity.insert(ind, q) 

					product.insert(ind, p) 
				    
					t = B-sum(product) 

					print("\namount left", t) 
				else: 
					name.append(pn) 

					quantity.append(q) 

					product.append(p)	 

					
					t = B-sum(product) 

					print("\namount left", t) 

		elif t<= 0: 
			print("\nNO BUDGET") 
		else: 
			break

print("\nAmount left : Rs.", t) 

if t in product: 
	print("\nAmount left can buy you a", name[product.index(t)]) 

print("\n\n\nGROCERY LIST") 

for i in range(len(name)): 
	print(name[i], quantity[i], product[i]) 

