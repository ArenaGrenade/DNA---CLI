import pymysql
import pymysql.cursors
import subprocess as sp
import sys
import time
import options
import os

def connect_db(tries):
    for tryindex in range(tries):
        print("Connecting to Database. Try " + str(tryindex + 1) + "...")
        try:
            con = pymysql.connect(host=os.getenv("HOST"),  
                                user=os.getenv("USERNAME"),
                                password=os.getenv("PASSWORD"),
                                db=os.getenv("DB"),
                                cursorclass=pymysql.cursors.DictCursor)
            _ = sp.call('clear', shell=True)

            if(con.open):
                print("Connected to the Database.")
            else:
                print("Failed to connect. Exiting now...")
                sys.exit(1)

            _ = input("Enter any key to continue...")

            return con

        except:
            _ = sp.call('clear', shell=True)
            print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
            if (tryindex != tries - 1):
                print("Now retrying...")
                time.sleep(0.5)
    return None

def prompt(con):
    with con.cursor() as cur:
        while(1):
            _ = sp.call('clear', shell=True)

            # print the options
            for (index, option) in enumerate(options.switcher.items()):
                print("{index}.  {option}".format(index = index + 1, option = option[1][1]))
            print("{index}.  Logout".format(index = index + 2))

            ch = int(input("Enter your choice> "))
            
            _ = sp.call('clear', shell=True)
            if ch == index + 2:
                return
            else:
                # Handle the option select
                status = options.do_job(ch, cur, con)

                if status is not False:
                    print("\nOperation Complete.")
                else:
                    print("")
                _ = input("Enter any key to continue...")
