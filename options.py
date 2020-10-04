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

		query = "INSERT INTO EMPLOYEE(ID, NAME, DOB, SEX, SUPER_ID, CLASSID, DEPARTMENT_ID, BRANCH_ID, PHONE_NO) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
			row["ID"], row["NAME"], row["DOB"], row["SEX"], row["SUPER_ID"], row["CLASSID"], row["DEPARTMENT_ID"], row["BRANCH_ID"], row["PHONE_NO"])

		print(query)
		cur.execute(query)
		con.commit()

		print("Inserted Into Database")

	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print(">>>>>>>>>>>>>", e)
	return True

def invalid_opfunc(cur, con):
    print("You have selected an invalid operation.")
    return False


switcher = {
    1: [option1, "Option 1"],
    2: [option2, "Add an employee"]
}

invalid_op = [invalid_opfunc, "Invalid Operation"]
