m = [
    "*        *",
    "**      **",
    "* *    * *",
    "*  *  *  *",
    "*   **   *",
    "*        *",
    "*        *",
    "*        *",
    "*        *",
    "*        *",
]

i = [
    "**********",
    "**********",
    "    **    ",
    "    **    ",
    "    **    ",
    "    **    ",
    "    **    ",
    "    **    ",
    "**********",
    "**********",
]

s = [
    " ******** ",
    "**      **",
    "**        ",
    "**        ",
    " ******** ",
    "        **",
    "        **",
    "**      **",
    " ******** ",
    "          ",
]

p = [
    "**********",
    "**      **",
    "**      **",
    "**      **",
    "**********",
    "**        ",
    "**        ",
    "**        ",
    "**        ",
    "**        ",
]




#def print_vertical(letter):
  #  for row in letter:
  #      print(row)

    #print_vertical(letter)
height = len(m)

def print_Horizontal(letter):
        for row in range(height):
            for letter in [m, i, s, s, i, s, s, i, p, p, i]:
                    print((letter[row]), end="  ")
            print()
        print()


for letter in [m, i, s, s, i, s, s, i, p, p, i]:
    print_Horizontal(letter)