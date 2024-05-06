
def wrap(string, length):
    result = ""
    counter=0;

    for letter in string:
        #About to reach end of line, we check if the next letter to append is an alphanumeric character
        if counter==length-1 and letter.isalpha():
            #if the previous character was alphanumeric, append a '-'
            if result[-1].isalpha():
                result+='-'
            #this increment will trigger the end of line
            counter+=1

        #we've reached the end line, append a '\n' and reset counter
        if counter==length:
            result+="\n"
            counter=0

        #appends the current letter 
        result+=letter
        counter+=1

    return result

string = "Hello, world! I am hungry."
length = 10

for length in range(5,12):
    print(wrap(string, length))