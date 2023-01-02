import numpy

def char_decode(numbers):
    if numbers == "11":
        return "a"
    if numbers == "12":
        return "b"
    if numbers == "13":
        return "c"
    if numbers == "14":
        return "d"
    if numbers == "15":
        return "e"
    if numbers == "16":
        return "f"
    if numbers == "21":
        return "g"
    if numbers == "22":
        return "h"
    if numbers == "23":
        return "i"
    if numbers == "24":
        return "j"
    if numbers == "25":
        return "k"
    if numbers == "26":
        return "l"
    if numbers == "31":
        return "m"
    if numbers == "32":
        return "n"
    if numbers == "33":
        return "o"
    if numbers == "34":
        return "p"
    if numbers == "35":
        return "q"
    if numbers == "36":
        return "r"
    if numbers == "41":
        return "s"
    if numbers == "42":
        return "t"
    if numbers == "43":
        return "u"
    if numbers == "44":
        return "w"
    if numbers == "45":
        return "x"
    if numbers == "46":
        return "y"
    else:
        print("that's not in the code bruv")

def char_encode(letter):
    if letter == "a":
        return 11
    if letter == "b":
        return 12
    if letter == "c":
        return 13
    if letter == "d":
        return 14
    if letter == "e":
        return 15
    if letter == "f":
        return 16
    if letter == "g":
        return 21
    if letter == "h":
        return 22
    if letter == "i":
        return 23
    if letter == "j":
        return 24
    if letter == "k":
        return 25
    if letter == "l":
        return 26
    if letter == "m":
        return 31
    if letter == "n":
        return 32
    if letter == "o":
        return 33
    if letter == "p":
        return 34
    if letter == "q":
        return 35
    if letter == "r":
        return 36
    if letter == "s":
        return 41
    if letter == "t":
        return 42
    if letter == "u":
        return 43
    if letter == "w":
        return 44
    if letter == "x":
        return 45
    if letter == "y":
        return 46
    else:
        print("input an invalid character")
        
def find_middle_factors(message_length):
    columns = 1
    rows = 1
    if int(numpy.sqrt(message_length)) * int(numpy.sqrt(message_length)) == message_length:
        #accounts for perfect squares the only time when the middle two factors are the same
        rows = int(numpy.sqrt(message_length))
        columns = rows
    else:
        #so basically when taking the sqrt it will always be in between the middle two factors
        #so we truncate and add 1 and calculate from there
        #example of 24: 1, 2, 3, {4, 6}, 8, 12, 24
        #sqrt of 24 is like between 4 and 5 => like 4.5
        counter = int(numpy.sqrt(message_length)) + 1
        #should be 4 + 1 == 5
        while message_length / counter != int(message_length / counter):
            counter = counter + 1
        #this will be the longer factor which is the columns
        columns = counter
        rows = int(message_length / counter)
    return rows, columns

def remove_encoding_anomalies(message):
    #removes all punctuation, capitalization, non-encodable text basically
    message = message.lower()
    edited_message = ""
    for i in message:
        if i == "v":
            edited_message = edited_message + "w"
        elif i == "z":
            edited_message = edited_message + "s"
        elif i == "a" or i == "b" or i == "c" or i == "d" or i == "e" or i == "f" or i == "g" or i == "h" or i == "i" or i == "j" or i == "k" or i == "l":
            edited_message = edited_message + i
        elif i == "m" or i == "n" or i == "o" or i == "p" or i == "q" or i == "r" or i == "s" or i == "t" or i == "u" or i == "w" or i == "x" or i == "y":
            edited_message = edited_message + i
    return edited_message

def assign_to_matrix(encoded_message):
    (rows, columns) = find_middle_factors(len(encoded_message))
    encoded_message_iterator = 0
    arr = [[0 for i in range(columns)] for j in range(rows)]
    #creates the appropriately sized array of all values of 0
    #now assigning the numbers to it per the matrix
    col_iterator = 0
    for i in range(rows):
        col_iterator = 0
        row_iterator = i
        while col_iterator != columns and row_iterator >= 0:
            arr[row_iterator][col_iterator] = encoded_message[encoded_message_iterator]
            encoded_message_iterator = encoded_message_iterator + 1
            col_iterator = col_iterator + 1
            row_iterator = row_iterator - 1
        #success! this does the upper left section of the array like up to the end of the rows
    for i in range(columns - 1):
        col_iterator = i + 1
        row_iterator = rows - 1
        while col_iterator != columns and row_iterator >= 0:
            arr[row_iterator][col_iterator] = encoded_message[encoded_message_iterator]
            encoded_message_iterator = encoded_message_iterator + 1
            col_iterator = col_iterator + 1
            row_iterator = row_iterator - 1
        #this will do everything that is a column past the rows! combined that is everything
        
    #now we just need to create a string which reads the array like a book (row by row left to right)
    matrix_message = ""
    for i in range(rows):
        for j in range(columns):
            matrix_message = matrix_message + arr[i][j]
    return matrix_message
            
def encode(message):
    #So for this we need to convert to code, then we need to find the factors of the length of the string,
    #then we need to use an algorithm to create the new string using the diagonal method of finding
    #should be able to do this without using matrices
    
    encoded_message = ""
    message = remove_encoding_anomalies(message)
    for i in message:
        encoded_message = encoded_message + str(char_encode(i))
    #it is now fully coded into the code
    #now just on to the for looping stuff
    (rows, columns) = find_middle_factors(len(encoded_message))
    encoded_message_iterator = 0
    arr = [[0 for i in range(columns)] for j in range(rows)]
    #creates the appropriately sized array of all values of 0
    
    #now assigning the numbers to it per the matrix
    for i in range(rows):
        col_iterator = 0
        row_iterator = i
        while col_iterator != columns and row_iterator >= 0:
            arr[row_iterator][col_iterator] = encoded_message[encoded_message_iterator]
            encoded_message_iterator = encoded_message_iterator + 1
            col_iterator = col_iterator + 1
            row_iterator = row_iterator - 1
        #success! this does the upper left section of the array like up to the end of the rows
    for i in range(columns - 1):
        col_iterator = i + 1
        row_iterator = rows - 1
        while col_iterator != columns and row_iterator >= 0:
            arr[row_iterator][col_iterator] = encoded_message[encoded_message_iterator]
            encoded_message_iterator = encoded_message_iterator + 1
            col_iterator = col_iterator + 1
            row_iterator = row_iterator - 1
        #this will do everything that is a column past the rows! combined that is everything
        
    #now we just need to create a string which reads the array like a book (row by row left to right)
    matrix_message = ""
    for i in range(rows):
        for j in range(columns):
            matrix_message = matrix_message + arr[i][j]
    print(matrix_message)
    print("")
    new_message = input("message to encode (quit! to leave, home! for menu): ")
    if new_message == "quit!":
        return
    elif new_message == "home!":
        chooser()
    else:
        encode(new_message)

def decode(message):
    message_iterator = 0
    (rows, columns) = find_middle_factors(len(message))
    arr = [[0 for i in range(columns)] for j in range(rows)]
    #creates the appropriately sized array of all values of 0
    
    #now we need to assign the message to it in book order
    
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = message[message_iterator]
            message_iterator = message_iterator + 1
    #so we now have the completed array from the encoder thing, we just have to go backwards and read the array the same way we assigned to it
    decoded_code = ""
    for i in range(rows):
        col_iterator = 0
        row_iterator = i
        while col_iterator != columns and row_iterator >= 0:
            decoded_code = decoded_code + arr[row_iterator][col_iterator]
            col_iterator = col_iterator + 1
            row_iterator = row_iterator - 1
    for i in range(columns - 1):
        col_iterator = i + 1
        row_iterator = rows - 1
        while col_iterator != columns and row_iterator >= 0:
            decoded_code = decoded_code + arr[row_iterator][col_iterator]
            col_iterator = col_iterator + 1
            row_iterator = row_iterator - 1
    #successfully translates into a left to right encoded message
    #reads it using the char_decoder I just wrote, meaning isolate every 2 digits of the message which is in decoded_code
    code_iterator = 0
    code_checker = ""
    fully_decoded_message = ""
    for i in decoded_code:
        code_iterator = code_iterator + 1
        code_checker = code_checker + i
        if code_iterator % 2 == 0 and code_iterator != 0:
            fully_decoded_message = fully_decoded_message + str(char_decode(code_checker))
            code_checker = ""
    print(fully_decoded_message)
    print("")
    new_message = input("message to decode (quit! to leave, home! for menu): ")
    if new_message == "quit!":
        return
    elif new_message == "home!":
        chooser()
    else:
        decode(new_message)

def chooser():
    choice = input("encode or decode: ")
    if(remove_encoding_anomalies(choice) == "encode"):
        encode(input("message to encode: "))
    elif(remove_encoding_anomalies(choice) == "decode"):
        decode(input("message to decode: "))
    else:
        print("Not one of the choices boi")
        chooser()
chooser()
