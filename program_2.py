
def average_age():
    # Get User Input
    print('Hello, user! My name is Steve and my job is to find the average age of a group of people.\n')
    print('Input age of person 1: ')
    person1 = int(input())
    print('Input age of person 2: ')
    person2 = int(input())
    print('Input age of person 3: ')
    person3 = int(input())
    print('Input age of person 4: ')
    person4 = int(input())
    print('Input age of person 5: ')
    person5 = int(input())

    # Sum ages
    result = (person1 + person2 + person3 + person4 + person5)

    # Average the ages
    average = float((result / 5))
    # Print the results
    print('The average age of your age group equals', average, 'years old')
    # Line which calls the above function.

    # Jadon Anderstrom, 9/10/24, "Average Age".
average_age()
