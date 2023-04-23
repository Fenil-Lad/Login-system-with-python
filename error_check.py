def get_input(data_type):
    while True:
        try:
            value = data_type(input())
            return value
        except ValueError:
            print("\nError: the input is not a valid", data_type.__name__)
            print("Please enter a valid option: ")
        except TypeError:
            print("\nError: the data type", data_type.__name__, "is not supported")
            print("Please enter a valid option: ")
