import getopt
import sys
import cli
import subprocess as sp
from dotenv import load_dotenv

def main(argv):
    _ = sp.call('clear', shell=True)
    tries = 10

    try:
        opts, _ = getopt.getopt(argv, "t", ["tries="])
    except getopt.GetoptError:
        print("cli.py -t <tries>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == 'u':
            print("cli.py -t <tries>")
            sys.exit()
        elif opt in ("-t", "--tries"):
            tries = arg

    connection = cli.connect_db(tries)
    if connection is not None:
        cli.prompt(connection)
        print("Thank you for using the service.")
    else:
        print("Unable to connect to MySQL server. Exiting...")
        sys.exit(1)

if __name__ == '__main__':
    load_dotenv()
    main(sys.argv[1:])
