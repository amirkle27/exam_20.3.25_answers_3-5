from abc import ABC, abstractmethod
from typing import override
import random
import statistics

class Array(ABC):
    def __init__(self):
        self.next_equation = None
        self.number_array = []

    def set_next(self, equation):
        self.next_equation = equation


    @abstractmethod
    def equation(self): 
        pass


    def next_equation(self):
        if self.next_equation:
            self.next_equation.number_array = self.number_array
            self.next_equation.equation()

class GetArray(Array):

    def get_array(self):
        numbers = input("Please enter an array of numbers or press [A] if you want the system to do it for you Automatically")
        if numbers.lower() == 'a':
            self.number_array = [random.randint(1, 100) for _ in range(10)]
        else:
            self.number_array = [int(num.strip()) for num in numbers.split(',')]
        print(f" Initial Array:  {self.number_array}\n")

        Array.next_equation(self)

    @override
    def equation(self):
        pass

class ArraySorter(Array):
    def __init__(self):
        super().__init__()

    @override
    def equation(self):
        sort = input("Would you like to sort the numbers in the array?")
        if sort.lower() in ['y','yes']:
            self.number_array = sorted(self.number_array)
            print(f"\n Sorted numbers:  {self.number_array}")

        Array.next_equation(self)


class ArrayMultiplier(Array):

    @override
    def equation(self):
        multiply = input("Would you like to multiply the numbers?")
        if multiply.lower() in ['y','yes']:
            multiplication_factor = input("Please enter a multiplication_factor for the numbers in the array press [A] if you want the system to do it for you Automatically")
            if multiplication_factor.lower() == 'a':
                multiplication_factor = random.randint(1, 10)
            multiplication_factor = int(multiplication_factor)
            self.number_array = [num * multiplication_factor for num in self.number_array]
            print(f"\n - Multiplexed numbers by {multiplication_factor}:  {self.number_array}")

        Array.next_equation(self)

class ArrayAverager(Array):

    @override
    def equation(self):
        multiply = input("Would you like to calculate an average for the numbers?")
        if multiply.lower() in ['y', 'yes']:
            average_calc = sum(num for num in self.number_array) / len(self.number_array)
            print(f"\n - Average number for {self.number_array}:  {average_calc:.2f}")
        else:
            Array.next_equation(self)

        Array.next_equation(self)


class ArraySTD(Array):
    def __init__(self):
        super().__init__()
        self.std_deviation = None

    @override
    def equation(self):
        std = input("Would you like to see an STD for the array?")
        if std.lower() in ['y', 'yes']:
            if len(self.number_array) > 1:
                self.std_deviation = statistics.stdev(self.number_array)
                print(f"\n - Standard deviation: {self.std_deviation:.2f}\n")
            else:
                print(f"\n - Cannot calculate standard deviation with less than 2 numbers")

            print(f"\n - Final array: {self.number_array}\n\n")

        print("End of program.\n Thank you so much, and May The Force Be With You!")



get_array = GetArray()
sorter = ArraySorter()
multiplier = ArrayMultiplier()
averager = ArrayAverager()
std = ArraySTD()

get_array.set_next(sorter)
sorter.set_next(multiplier)
multiplier.set_next(averager)
averager.set_next(std)

get_array.get_array()


