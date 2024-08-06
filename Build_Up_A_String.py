constructed_string = ""
user_string =input("please inset a string")
user_string_length = len(user_string)
if user_string_length == 10:
    print("perfect string")
    for charactor in user_string:
        constructed_string += charactor
        print(constructed_string)

elif user_string_length > 10:
    print("string too long")
else:
    print("string not long enough")


