
KEYBOARD = ['a','z','e','r','t','y','u','i','o','p','^',
            'q','s','d','f','g','h','j','k','l','m','ù',
            'w','x','c','v','b','n',',',';',':','!']

def translateRightShift(str):

    result = ""

    for letter in str:
        if letter==" ":
            result+=" "
            continue
        result+= KEYBOARD[KEYBOARD.index(letter)-1]
    return result

input = "mpm xpxor"
print(translateRightShift(input))

input = "xjp zù o"
print(translateRightShift(input))