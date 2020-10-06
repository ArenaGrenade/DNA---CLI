from tabulate import tabulate

def do_job(option, cur, con):
    (switcher.get(option, invalid_op))[0](cur, con)


def option1(cur, con):
    print("you are at option 1. Works na")

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

def invalid_opfunc(cur, con):
    print("You have selected an invalid operation.")

def option5(cur, con):
	# print("you are at option 1. Works na")
	# return True
	try:
		row = {}
		print("Enter new order details: ")
		row["EMPLOYEE_ID"] = input("Employee id: ")
		row["ID"] = input("ID: ")
		row["NAME"] = input("NAME: ")
		row["VOLUME"] = float(input("VOLUME: "))
		row["WEIGHT"] = float(input("WEIGHT: "))
		row["STATUS"] = input("STATUS: ")
		row["CUSTOMER_ID"] = input("CUSTOMER_ID: ")
		row["PLACED_ON"] = input("Order Date (YYYY-MM-DD): ")

		query = "INSERT INTO ORDERS(ID, NAME, VOLUME, WEIGHT, STATUS, CUSTOMER_ID, PLACED_ON, DELIVERY_COST) VALUES('%s', '%s', '%f', '%f', '%s', '%s', '%s', %f)" % (
			row["ID"], row["NAME"], row["VOLUME"], row["WEIGHT"], row["STATUS"], row["CUSTOMER_ID"], row["PLACED_ON"], (row["VOLUME"]*row["WEIGHT"])/100)

		print(query)
		cur.execute(query)

		query = "INSERT INTO ORDER_PLACEMENT(CUSTOMER_ID, EMPLOYEE_ID, ORDER_ID) VALUES('%s', '%s', '%s')" % (
			row["CUSTOMER_ID"], row["EMPLOYEE_ID"], row["ID"])

		cur.execute(query)
		con.commit()

		print("Inserted Into Database")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print(">>>>>>>>>>>>>", e)

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

def option7(cur, con):
	# print("you are at option 1. Works na")
	# return True
	try:
		row = {}
		row["ID"] = input("Enter ORDER ID: ")

		query = "DELETE FROM ORDERS WHERE ID = %s"
		val = (row["ID"])
		print(query)
		cur.execute(query, val)
		query = "DELETE FROM ORDER_PLACEMENT WHERE ORDER_ID = %s"
		val = (row["ID"])
		print(query)
		cur.execute(query, val)
		con.commit()

		print("Edited Database")

	except Exception as e:
		con.rollback()
		print("Failed to edit into database")
		print(">>>>>>>>>>>>>", e)

def option8(cur, con):
	# print("you are at option 1. Works na")
	# return True
	try:
		row = {}
		row["ID"] = input("Enter ORDER ID: ")
		row["FROM_BRANCH_ID"] = input("Enter dispatching branch ID: ")
		row["TO_BRANCH_ID"] = input("Enter arriving branch ID: ")

		query = "UPDATE ORDERS SET STATUS='DELIVERED' WHERE ID = %s"
		val = (row["ID"])
		cur.execute(query, val)
		query = "INSERT INTO ORDER_SHIPPING(TO_BRANCH_ID, FROM_BRANCH_ID, ORDER_ID) VALUES(%s, %s, %s)"
		val = (row["TO_BRANCH_ID"], row["FROM_BRANCH_ID"], row["ID"])
		cur.execute(query, val)
		con.commit()

		print("Edited Database")

	except Exception as e:
		con.rollback()
		print("Failed to edit into database")
		print(">>>>>>>>>>>>>", e)

def option9(cur, con):
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

def option10(cur, con):
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

def option11(cur, con):
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

def option12(cur, con):
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

def option13(cur, con):
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

def option14(cur, con):
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

def rankCustomersOnOrders(cur, con):
	try:
		# some code here
		query = "SELECT ORDERS.CUSTOMER_ID AS CID, CUSTOMERS.NAME, COUNT(ORDERS.ID) "\
				"FROM ORDERS "\
				"INNER JOIN CUSTOMERS ON ORDERS.CUSTOMER_ID=CUSTOMERS.ID "\
				"GROUP BY ORDERS.CUSTOMER_ID "\
				"ORDER BY COUNT(CUSTOMERS.ID) DESC"
		cur.execute(query)

		table = [[row["CID"], row["NAME"], row["COUNT(ORDERS.ID)"]] for row in cur]

		print(tabulate(table, headers=["Customer", "Name", "Number of Orders"]))

		print("Completed Retrieval of Data.")
	except Exception as e:
		con.rollback()
		print("Failed to get data from database")
		print(">>>>>>>>>>>>>", e)

def option15(cur, con):
	try:
		row = {}
		row["EMPLOYEE_ID"] = input("Employee id: ")
		row["YEAR"] = input("Year(YYYY): ")
		row["MONTH"] = input("Month(MM): ")
		# some code here
		query = "SELECT SUM(DELIVERY_COST) FROM ((EMPLOYEE INNER JOIN ORDER_PLACEMENT on ORDER_PLACEMENT.EMPLOYEE_ID = EMPLOYEE.ID) INNER JOIN ORDERS on ORDER_PLACEMENT.ORDER_ID = ORDERS.ID) WHERE PLACED_ON LIKE '%s-__-__' AND EMPLOYEE_ID='%s'"%(row["YEAR"],row["EMPLOYEE_ID"])
		cur.execute(query)

		table = [[row["SUM(DELIVERY_COST)"]] for row in cur]

		print(tabulate(table, headers=["Yearly Income", "date"]))

		query = "SELECT SUM(DELIVERY_COST) FROM ((EMPLOYEE INNER JOIN ORDER_PLACEMENT on ORDER_PLACEMENT.EMPLOYEE_ID = EMPLOYEE.ID) INNER JOIN ORDERS on ORDER_PLACEMENT.ORDER_ID = ORDERS.ID) WHERE PLACED_ON LIKE '%s-%s-__' AND EMPLOYEE_ID='%s'"%(row["YEAR"],row["MONTH"], row["EMPLOYEE_ID"])
		cur.execute(query)

		table = [[row["SUM(DELIVERY_COST)"]] for row in cur]

		print(tabulate(table, headers=["Monthly Income for month %s"%(row["MONTH"]), "date"]))

		print("Completed Retrieval of Data.")
	except Exception as e:
		con.rollback()
		print("Failed to get data from database")
		print(">>>>>>>>>>>>>", e)

def option16(cur, con):
	try:
		row = {}
		row["YEAR"] = input("Year(YYYY): ")
		row["MONTH"] = input("Month(MM): ")
		# some code here
		query = "SELECT COUNT(*) FROM ORDERS WHERE PLACED_ON LIKE '%s-__-__' "%(row["YEAR"])
		cur.execute(query)

		table = [[row["COUNT(*)"]] for row in cur]

		print(tabulate(table, headers=["Yearly Orders", "date"]))
		query = "SELECT COUNT(*) FROM ORDERS WHERE PLACED_ON LIKE '%s-%s-__' "%(row["YEAR"], row["MONTH"])

		cur.execute(query)

		table = [[row["COUNT(*)"]] for row in cur]

		print(tabulate(table, headers=["Monthly Number of orders for month %s"%(row["MONTH"]), "date"]))

		print("Completed Retrieval of Data.")
	except Exception as e:
		con.rollback()
		print("Failed to get data from database")
		print(">>>>>>>>>>>>>", e)


switcher = {
    1: [option1, "Option 1"],
    2: [option2, "Add an employee"],
    3: [option3, "Edit employee details"],
    4: [option4, "Remove an Employee"],
    5: [option5, "Add new Order"],
    6: [option6, "Edit Order details"],
    7: [option7, "Remove an Order"],
    8: [option8, "Assign branches and change delivery status"],
    9: [option9, "Add a Customer"],
    10: [option10, "Edit Customer Details"],
    11: [option11, "Remove Customer"],
    12: [option12, "Add an employee Address"],
    13: [option13, "Add an employee dependent"],
    14: [option14, "Add a customer profile"],
    15: [option15, "Get monthly and yearly income of an employee"],
    16: [option16, "Get monthly and yearly order quantity"],
	17: [rankCustomersOnOrders, "Get an Descending order of customers based on orders made"],
}

invalid_op = [invalid_opfunc, "Invalid Operation"]
