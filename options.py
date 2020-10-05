def do_job(option, cur, con):
    return (switcher.get(option, invalid_op))[0](cur, con)


def option1(cur, con):
    print("you are at option 1. Works na")
    return True

def option2(cur, con):
	# print("you are at option 1. Works na")
	# return True
	try:
		row = {}
		print("Enter new employee's details: ")
		row["ID"] = input("ID: ")
		row["NAME"] = input("NAME: ")
		row["DOB"] = input("Birth Date (YYYY-MM-DD): ")
		row["SEX"] = input("Sex: ")
		row["SUPER_ID"] = input("Superior ID: ")
		row["CLASSID"] = input("Employee Category: ")
		row["DEPARTMENT_ID"] = input("Department id: ")
		row["BRANCH_ID"] = input("Branch id: ")
		row["PHONE_NO"] = input("Phone no: ")
		row["PIN_CODE"] = input("Pin code: ")
		row["BUILDING_INFO"] = input("Building name: ")
		row["LANDMARK"] = input("Landmark (if any): ")
		row["AREA"] = input("Area: ")


		query = "INSERT INTO EMPLOYEE(ID, NAME, DOB, SEX, SUPER_ID, CLASSID, DEPARTMENT_ID, BRANCH_ID, PHONE_NO) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
			row["ID"], row["NAME"], row["DOB"], row["SEX"], row["SUPER_ID"], row["CLASSID"], row["DEPARTMENT_ID"], row["BRANCH_ID"], row["PHONE_NO"])

		print(query)
		cur.execute(query)
		query = "INSERT INTO ADDRESS(ID, PIN_CODE, BUILDING_INFO, LANDMARK, AREA) VALUES('%s', '%s', '%s', '%s', '%s')" % (
			row["ID"], row["PIN_CODE"], row["BUILDING_INFO"], row["LANDMARK"], row["AREA"])
		cur.execute(query)
		con.commit()

		print("Inserted Into Database")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print(">>>>>>>>>>>>>", e)
	return True

def option3(cur, con):
	# print("you are at option 1. Works na")
	# return True
	try:
		row = {}
		row["ID"] = input("Enter Employee ID: ")
		row["NAME"] = input("New name: ")
		row["DOB"] = input("New Birth Date (YYYY-MM-DD): ")
		row["SEX"] = input("Sex: ")
		row["SUPER_ID"] = input("New Superior ID: ")
		row["CLASSID"] = input("New Employee Category: ")
		row["DEPARTMENT_ID"] = input("New Department id: ")
		row["BRANCH_ID"] = input("New Branch id: ")
		row["PHONE_NO"] = input("New Phone no: ")

		query = "UPDATE EMPLOYEE SET NAME = %s, DOB = %s, SEX = %s, SUPER_ID = %s, CLASSID = %s, DEPARTMENT_ID = %s, BRANCH_ID = %s, PHONE_NO = %s WHERE ID = %s"
		val = (row["NAME"], row["DOB"], row["SEX"], row["SUPER_ID"], row["CLASSID"], row["DEPARTMENT_ID"], row["BRANCH_ID"], row["PHONE_NO"], row["ID"])
		print(query)
		cur.execute(query, val)
		con.commit()

		print("Edited Database")

	except Exception as e:
		con.rollback()
		print("Failed to edit into database")
		print(">>>>>>>>>>>>>", e)
	return True

def option4(cur, con):
	# print("you are at option 1. Works na")
	# return True
	try:
		row = {}
		row["ID"] = input("Enter Employee ID: ")

		query = "DELETE FROM EMPLOYEE WHERE ID = %s"
		val = (row["ID"])
		print(query)
		cur.execute(query, val)
		query = "DELETE FROM ADDRESS WHERE ID = %s"
		val = (row["ID"])
		cur.execute(query, val)
		query = "DELETE FROM DEPENDENT WHERE EMPLOYEE_ID = %s"
		val = (row["ID"])
		cur.execute(query, val)
		con.commit()

		print("Edited Database")

	except Exception as e:
		con.rollback()
		print("Failed to edit into database")
		print(">>>>>>>>>>>>>", e)
	return True

def invalid_opfunc(cur, con):
    print("You have selected an invalid operation.")
    return False

def option5(cur, con):
	# print("you are at option 1. Works na")
	# return True
	try:
		row = {}
		print("Enter new order details: ")
		row["ID"] = input("ID: ")
		row["NAME"] = input("NAME: ")
		row["VOLUME"] = input("VOLUME: ")
		row["WEIGHT"] = input("WEIGHT: ")
		row["STATUS"] = input("STATUS: ")
		row["CUSTOMER_ID"] = input("CUSTOMER_ID: ")
		row["PLACED_ON"] = input("Order Date (YYYY-MM-DD): ")

		query = "INSERT INTO ORDERS(ID, NAME, VOLUME, WEIGHT, STATUS, CUSTOMER_ID, PLACED_ON) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
			row["ID"], row["NAME"], row["VOLUME"], row["WEIGHT"], row["STATUS"], row["CUSTOMER_ID"], row["PLACED_ON"])

		print(query)
		cur.execute(query)
		con.commit()

		print("Inserted Into Database")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print(">>>>>>>>>>>>>", e)
	return True

def option6(cur, con):
	# print("you are at option 1. Works na")
	# return True
	try:
		row = {}
		row["ID"] = input("Enter order ID: ")
		row["NAME"] = input("NAME: ")
		row["VOLUME"] = input("VOLUME: ")
		row["WEIGHT"] = input("WEIGHT: ")
		row["STATUS"] = input("STATUS: ")
		row["CUSTOMER_ID"] = input("CUSTOMER_ID: ")
		row["PLACED_ON"] = input("Order Date (YYYY-MM-DD): ")

		query = "UPDATE ORDERS SET NAME = %s, VOLUME = %s, WEIGHT = %s, STATUS = %s, CUSTOMER_ID = %s, PLACED_ON = %s WHERE ID = %s"
		val = (row["NAME"], row["VOLUME"], row["WEIGHT"], row["STATUS"], row["CUSTOMER_ID"], row["PLACED_ON"], row["ID"])
		print(query)
		cur.execute(query, val)
		con.commit()

		print("Edited Database")

	except Exception as e:
		con.rollback()
		print("Failed to edit into database")
		print(">>>>>>>>>>>>>", e)
	return True

def option7(cur, con):
	# print("you are at option 1. Works na")
	# return True
	try:
		row = {}
		row["ID"] = input("Enter ORDER ID: ")

		query = "DELETE FROM ORDER WHERE ID = %s"
		val = (row["ID"])
		print(query)
		cur.execute(query, val)
		con.commit()

		print("Edited Database")

	except Exception as e:
		con.rollback()
		print("Failed to edit into database")
		print(">>>>>>>>>>>>>", e)
	return True

def option8(cur, con):
	# print("you are at option 1. Works na")
	# return True
	try:
		row = {}
		print("Enter new customer details: ")
		row["ID"] = input("ID: ")
		row["NAME"] = input("NAME: ")
		row["SEX"] = input("Sex: ")
		row["DOB"] = input("Birth Date (YYYY-MM-DD): ")
		row["PHONE_NO"] = input("Phone no: ")
		row["ADDRESS"] = input("Address: ")

		query = "INSERT INTO CUSTOMERS(ID, NAME, SEX, DOB, PHONE_NO, ADDRESS) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (
			row["ID"], row["NAME"], row["VOLUME"], row["DOB"], row["PHONE_NO"], row["ADDRESS"])

		print(query)
		cur.execute(query)
		con.commit()

		print("Inserted Into Database")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print(">>>>>>>>>>>>>", e)
	return True

def option9(cur, con):
	# print("you are at option 1. Works na")
	# return True
	try:
		row = {}
		row["ID"] = input("Enter Customer ID: ")
		row["NAME"] = input("New name: ")
		row["SEX"] = input("Sex: ")
		row["DOB"] = input("New Birth Date (YYYY-MM-DD): ")
		row["PHONE_NO"] = input("New Phone no: ")
		row["ADDRESS"] = input("New Address: ")

		query = "UPDATE CUSTOMERS SET NAME = %s, SEX = %s, DOB = %s, PHONE_NO = %s, ADDRESS = %s WHERE ID = %s"
		val = (row["NAME"], row["SEX"], row["DOB"], row["PHONE_NO"], row["ADDRESS"], row["ID"])
		print(query)
		cur.execute(query, val)
		con.commit()

		print("Edited Database")

	except Exception as e:
		con.rollback()
		print("Failed to edit into database")
		print(">>>>>>>>>>>>>", e)
	return True

def option10(cur, con):
	# print("you are at option 1. Works na")
	# return True
	try:
		row = {}
		row["ID"] = input("Enter CUSTOMER ID: ")

		query = "DELETE FROM CUSTOMERS WHERE ID = %s"
		val = (row["ID"])
		cur.execute(query, val)
		query = "DELETE FROM PROFILE WHERE CUSTOMER_ID = %s"
		val = (row["ID"])
		cur.execute(query, val)
		con.commit()

		print("Edited Database")

	except Exception as e:
		con.rollback()
		print("Failed to edit into database")
		print(">>>>>>>>>>>>>", e)
	return True

def option11(cur, con):
	# print("you are at option 1. Works na")
	# return True
	try:
		row = {}
		print("Enter new address details: ")
		row["ID"] = input("Employee ID: ")
		row["PIN_CODE"] = input("Pin code: ")
		row["BUILDING_INFO"] = input("Building name: ")
		row["LANDMARK"] = input("Landmark (if any): ")
		row["AREA"] = input("Area: ")


		query = "INSERT INTO ADDRESS(ID, PIN_CODE, BUILDING_INFO, LANDMARK, AREA) VALUES('%s', '%s', '%s', '%s', '%s')" % (
			row["ID"], row["PIN_CODE"], row["BUILDING_INFO"], row["LANDMARK"], row["AREA"])
		cur.execute(query)
		con.commit()

		print("Inserted Into Database")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print(">>>>>>>>>>>>>", e)
	return True

def option12(cur, con):
	# print("you are at option 1. Works na")
	# return True
	try:
		row = {}
		print("Enter new dependent details: ")
		row["EMPLOYEE_ID"] = input("Employee ID: ")
		row["NAME"] = input("Dependent name: ")
		row["SEX"] = input("Sex: ")
		row["DOB"] = input("Birth Date (YYYY-MM-DD): ")
		row["RELATIONSHIP"] = input("Relationship: ")

		query = "INSERT INTO DEPENDENT(EMPLOYEE_ID, NAME, SEX, DOB, RELATIONSHIP) VALUES('%s', '%s', '%s', '%s', '%s')" % (
			row["ID"], row["NAME"], row["SEX"], row["DOB"], row["RELATIONSHIP"])

		print(query)
		cur.execute(query)
		con.commit()

		print("Inserted Into Database")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print(">>>>>>>>>>>>>", e)
	return True

def option13(cur, con):
	# print("you are at option 1. Works na")
	# return True
	try:
		row = {}
		print("Enter new profile details: ")
		row["NAME"] = input("Profile name: ")
		row["CUSTOMER_ID"] = input("Customer ID: ")
		row["ADDRESS"] = input("Address: ")
		row["PHONE_NO"] = input("Phone no: ")

		query = "INSERT INTO PROFILE(NAME, CUSTOMER_ID, ADDRESS, PHONE_NO) VALUES('%s', '%s', '%s', '%s')" % (
			row["NAME"], row["CUSTOMER_ID"], row["ADDRESS"], row["PHONE_NO"])
		print(query)
		cur.execute(query)
		con.commit()

		print("Inserted Into Database")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print(">>>>>>>>>>>>>", e)
	return True


switcher = {
    1: [option1, "Option 1"],
    2: [option2, "Add an employee"],
    3: [option3, "Edit employee details"],
    4: [option4, "Remove an Employee"],
    5: [option5, "Add new Order"],
    6: [option6, "Edit Order details"],
    7: [option7, "Remove an Order"],
    8: [option8, "Add a Customer"],
    9: [option9, "Edit Customer Details"],
    10: [option10, "Remove Customer"],
    11: [option11, "Add an employee Address"],
    12: [option12, "Add an employee dependent"],
    13: [option13, "Add a customer profile"]
}

invalid_op = [invalid_opfunc, "Invalid Operation"]
