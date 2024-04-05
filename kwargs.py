def names(**kwargs):
    print("my name is  "+kwargs['name'])
names(name="varun")
names(name="simha")


def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3,7,9)
