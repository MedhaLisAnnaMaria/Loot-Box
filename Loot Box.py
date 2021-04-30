import random
def open_box():

	print("Opening loot box:")

	mylist = ["Legentary item", "Epic item", "Rare item", "Common item"]
	return random.choices(mylist, weights = [5, 10, 35, 50], k = 4)


num=1
gems=0
boxes=0
boxes_opn=0
total_spt=0
gem_cost=19.95
gem_amt=550
box_cost=100
item=[]
print("Welcome to loot box simulator")
while num!=5:

	print("\nYou have "+ str(gems)+" gems and "+ str(boxes)+" loot boxes.")
	print("\nChoose from the following options:")
	print(" 1)Buy the gems(550 gems for just $19.95!")
	print(" 2)Buy loot box(costs 100 gems)")
	print(" 3)open loot box")
	print(" 4)view statistis")
	print(" 5)Quit")
	num = int(input(""))
	print()
	if num < 0:
		print("This cannot be true!")
	elif num == 0:
	    print("This corresponds to 0 human years!")
	elif num == 1:

	    gems=gems+gem_amt
	    total_spt=total_spt+gem_cost
	    print("Thank you for your purhase!")

	elif num == 2:
		if gems>=100:
			gems=gems-box_cost
			boxes=boxes+1
			print("loot box purhased")
		else :
			print("Insufficient gems")


	elif num == 3:
		if boxes>0:
			boxes=boxes-1
			boxes_opn=boxes_opn+1
			item=open_box()
			print(" Item 1 of 4..."+item[0])
			print(" Item 2 of 4..."+item[1])
			print(" Item 3 of 4..."+item[2])
			print(" Item 4 of 4..."+item[3])
		else:
			print("Insufficient loot boxes")

	elif num == 4:

	    print("Total spent : $"+'%.2f'%total_spt)
	    print("Loot Boxes opened: "+ str(boxes_opn))
	    print("Legentary Items: "+ str(item.count("Legentary item")))

if num == 5:
	print("Good bye!!!")