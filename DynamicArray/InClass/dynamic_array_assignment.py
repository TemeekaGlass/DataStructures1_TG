import math

# Dynamic array -- accessor methods assignment.
#
# The class below is complete except for five methods marked with pass.
# Your task: implement those methods according to the spec in their comments.
# Do not modify any other method.
# Run this file to check your work against the expected output shown below.

class DynamicArray:

    # Class-level constants: shared by every instance, not stored per object.
    # The underscore signals "internal detail -- not part of the public interface."
    _DEFAULT_RESIZE_BY: float = 2
    _DEFAULT_CAPACITY: int = 4

    def __init__(self, capacity: int = _DEFAULT_CAPACITY, resize_by: float = _DEFAULT_RESIZE_BY) -> None:
        self._underlying: list[int] = list()
        self._capacity: int = capacity
        self._resize_by: float = resize_by
        # Pre-fill every slot with -1 as a sentinel value that marks "nothing stored here."
        # This keeps _underlying at a fixed length equal to _capacity at all times.
        for i in range(self._capacity):
            self._underlying.append(-1)
        # _size tracks stored values; _capacity tracks total slots (including sentinel slots).
        # They start equal to 0 and _DEFAULT_CAPACITY and diverge as elements are added.
        self._size: int = 0

    def __str__(self) -> str:
        if self._size == 0:
            return "nothing to show"
        output = "["
        # Loop up to _size, not _capacity -- sentinel slots are internal and never displayed.
        for i in range(self._size):
            output = output + str(self._underlying[i])
            if i < self._size - 1:
                output = output + ", "
        output = output + "]"
        return output

    def resize(self) -> None:
        # math.ceil guarantees the new capacity is always larger than the old one.
        # int() would round down: int(3 * 1.1) == 3, so the array would never grow.
        temp_capacity = math.ceil(self._resize_by * self._capacity)
        temp = list()
        for i in range(temp_capacity):
            temp.append(-1)
        # Copy only the old _capacity elements -- temp already has sentinels beyond that.
        for i in range(self._capacity):
            temp[i] = self._underlying[i]
        self._underlying = temp
        self._capacity = temp_capacity

    def add(self, value: int) -> None:
        # Resize before writing; after resize there is guaranteed room at index _size.
        if self._size >= self._capacity:
            self.resize()
        # _size is always the index of the next empty slot.
        self._underlying[self._size] = value
        self._size = self._size + 1

    def __len__(self) -> int:
        # Return the number of values stored in this array.
        # Enables: len(da) and truthiness checks like "if da:"
        # replace with your implementation

        #returns the size of the array by getting and reporting the dunder size attribute.
        return self._size
            
               
    def get_size(self) -> int:
        # Return the number of values stored in this array.
        # Same value as __len__; explicit name for readers unfamiliar with dunder methods.
        # replace with your implementation

        #returns the size of the array by putting the dunder size attribute into a named variable and retrieving that value
        self.arrayLength = self._size
        return self.arrayLength
    

    def get_capacity(self) -> int:
        # Return the total number of slots in the underlying array,
        # including empty sentinel slots. This is the hotel room count, not the guest count.
        # replace with your implementation

        #returns the capacity of the array by putting the dunder capacity attribute into a named variable and retrieving that value
        self.arrayCapacity = self._capacity
        return self.arrayCapacity

    def get(self, index: int) -> int:
        # Return the value at position index.
        # Valid positions are 0 through _size - 1 (filled slots only).
        # Return -1 for any index outside that range -- including negative indices.
        # Caution: Python lists accept negative indices natively; you must check for them
        # explicitly, or get(-1) will silently return the last element instead of -1.
        # replace with your implementation

        #use the Capacity mthod to grab the array size 
        positionValue = self.get_capacity()
        #put the array into a variable to be be referenced using the str method
        posValueItem = self._underlying
        #if the input  index variable is greater than the capacity put into the positionValue, return -1 as those will not be in the array
        #the index acts as the index indicator, returning the items at that position
        if index > positionValue:
            return (-1)
        else:
            return str(posValueItem[index])
       

        

    def index_of(self, value: int) -> int:
        # Return the position of the first occurrence of value.
        # Search only filled slots: positions 0 through _size - 1.
        # Do not search sentinel slots -- they all hold -1 and would give false matches.
        # Return -1 if value is not found.
        # replace with your implementation
        positionIndexNum = 0
        positionIndexItem = self._underlying

    
        #using the size as a ceiling for running the loop, i can iterrate over the 
        #values and compare them until it matches and returns the count of positionIndexNum
        #if the count of postindexnum counts greater than the size len(self) then it should return -1 line 
        # since the value was not found
        for positionIndexNum in range(len(self)):
            if value == positionIndexItem[positionIndexNum]:
                return positionIndexNum #, posIndexItem, len(self)-1
            else:
                if value != positionIndexItem[positionIndexNum]:
                     positionIndexNum += 1
                if len(self) <= positionIndexNum:
                    return "-1  (not in array)"#, positionIndexNum, len(self)

        
       




if __name__ == "__main__":
    da = DynamicArray()
    da.add(10001)
    da.add(60626)
    da.add(90210)
    #da.add(90211)
    #da.add(90212)
    #da.add(90213)
    #da.add(90214)
    print(da)                    # expected: [10001, 60626, 90210]

    print()
    print("__len__ and size/capacity getters")
    print(len(da))               # expected: 3
    print(da.get_size())         # expected: 3
    print(da.get_capacity())     # expected: 4

    print()
    print("get() tests")
    print(da.get(0))             # expected: 10001
    print(da.get(1))             # expected: 60626
    print(da.get(2))             # expected: 90210
    print(da.get(-1))            # expected: -1  (below valid range)
    print(da.get(3))             # expected: -1  (at size, no data there)
    print(da.get(100))           # expected: -1  (well beyond size)

    print()
    print("index_of() tests")
    print(da.index_of(10001))    # expected: 0
    print(da.index_of(60626))    # expected: 1
    print(da.index_of(90210))    # expected: 2
    print(da.index_of(99999))    # expected: -1  (not in array)

    da.add(11111)
    da.add(22222)
    print()
    print("after 2 more adds (triggers resize)")
    print(da)                    # expected: [10001, 60626, 90210, 11111, 22222]
    print(len(da))               # expected: 5
    print(da.get_capacity())     # expected: 8