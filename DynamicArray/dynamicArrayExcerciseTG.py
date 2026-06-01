#Write the code. How many lines does it require?
    # 3 lines of code
#Does your approach generalize? If data had eight elements and you needed to double to sixteen, what would you need to change?
    # I would need to add 12 in place of 4 to get 16 elements into the list, my approach may generalize as 
#Now imagine add_zip_code could call this doubling operation automatically whenever the array is full. What would that mean for the current if self.size < 4 guard — what should replace it?

data = [60611, 60614, 60647, 60660]
data += [-1] * (4*3)
print(data)