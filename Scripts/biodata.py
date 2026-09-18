def biodata():
	fname = input("Enter your first name:")
	lname = input("Enter your last name:")
	city = input("Enter the city you live in:")
	state = input("Enter the state you live in:")
	print("Your name is: %s %s" % (fname, lname))
	print("You live in: %s, %s" % (city, state))


biodata()
