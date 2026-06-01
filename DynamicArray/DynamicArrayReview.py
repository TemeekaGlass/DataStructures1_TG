#Before running: trace through __init__ and the two add_zip_code calls step by step. What are the values of self.data and self.size after each call? What will print(a) display?
    #2, 1, [60611, 60614] 

#After running: was your prediction correct? If it was not, identify the specific step where your mental model diverged.


#What would happen if you inserted a.add_zip_code(99999) between the two existing calls? Would print(a) change?
    #yes,it would change by adding that code to the list in its order of run

#After three calls to add_zip_code, what is the value of self.size? What index in self.data does that number represent?
    #2 is the size, 1 is the index

#Suppose you swapped the last two lines — incrementing self.size before placing value into self.data. What would go wrong? Trace through one call to show the effect.
    #the code would error

#Why does self.data[:self.size] in __str__ correctly show only the occupied slots?
    #self.size is only icremented when an item is added and displays the amount that is in the list.

#What does print(a) display when __str__ is present?


#What does print(a) display when __str__ is removed? Copy the exact output.


#The second output is not an error — Python still ran without raising an exception. What does the output tell you about how Python handles objects that have no __str__ defined? What information is in that default output?

class DynamicArray:
    def __init__(self):
        self.data = [-1, -1, -1, -1]
        self.size = 0

    def add_zip_code(self, value):
        if self.size < 4:
            self.data[self.size] = value
            self.size += 1

    def __str__(self):
        return str(self.data[:self.size])

a = DynamicArray()
a.add_zip_code(60611)
a.add_zip_code(99999)
a.add_zip_code(60614)
print(a)