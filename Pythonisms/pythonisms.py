from functools import wraps
from time import sleep


class Node:

    def __init__(self, value):
        """A method to create a new node"""
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, collection=None):
        """A method to create the linked list nodes"""
        self.head = None
        if collection:
            for item in reversed(collection):
                self.insert(item)

    def __iter__(self):
        def generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return generator()

    def __getitem__(self, index):
        for i, item in enumerate(self):
            if i == index:
                return item
        raise IndexError('Index out of range')

    def insert(self, value):
        """
        function that called insert that insert value in to the linked list

        """
        self.head = Node(value, self.head)

    def find_sum(self):
        """method to claculate the sum of the nodes value in the linked list 
        Args : linked list
        Return : the sum of the value """
        current = self.head
        result = 0
        while current:
            result += current.value
            current = current.next

        return result

    def find_product(self):
        """
        Find the product of all values

        :input (None)
        :output (int)
        """
        total = 1
        current = self.head
        while current:
            total *= current.value
            current = current.next
        return total

    def linked_list_squared(self):
        """
        returns a list with the values of the linked list nodes linked list squared
        input: linked list
        Returns: list
        """
        arr_of_values = []
        current = self.head
        while current:
            arr_of_values.append(current.value*current.value)
            current = current.next
        return arr_of_values

    def __str__(self):
        current = self.head
        output = []
        while current:
            output.append(f"{{{current.value}}}")
            current = current.next

        return "->".join(output)

    def traverse(self, action):
        current = self.head
        result = None
        while current:
            result = action(current.value)
            current = current.next
        return result


def procrastinate(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        """
        Wrapper wraps the stuff
        """
        sleep(3)
        return function(*args, **kwargs)
    return wrapper


def sarcastic_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        output = function(*args, **kwargs)
        return f'Yes I will, "{output}" '
    return wrapper


@procrastinate
@sarcastic_decorator
def say(text):
    """ 
    Say says the things
    """
    return text


if __name__ == "__main__":
    # print(say.__doc__)
    print("Sleeping")
    print(say("It's night"))
