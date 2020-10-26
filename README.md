### A command line interface to a logistics company database, done as part of a database and systems course.
To connect to a database please get the credentials and store them in a .env file in the root directory.

# Command Line Interface

To run the Command Line Interface to the System. Go to the directory where you have cloned this repository and run,

```bash
python3 -t 10
```

Here, the `-t` parameter is not required, but when entered, connects to the db and exits in the argument value times.

## To add new options to the CLI

Create a function for the same in the `options.py` file.
Let's say you want to create a function named `option1` as follows:

```python3
# It is highly important that you take cursor and connection as inputs to any function that you define.
def option1(cursor, connection):
    print("Hi! You are at option 1")
    # Add any code here to perform the needed operation
    if success:
        return True
    else:
        return False
    # Make sure that you return a True or False based on the success of the command
```

Now, Create the entry in the `switcher` data dictionary in `options.py` in the format as below:

```python3
switcher = {
    1: [option1, "This is option 1"]
}
```
