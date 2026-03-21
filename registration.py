MSG_NAME_ERROR = "MSG_NAME_ERROR"
MSG_AGE_OK = "MSG_AGE_OK"
MSG_AGE_ERROR = "MSG_AGE_ERROR"
MSG_PHONE_OK = "MSG_PHONE_OK"
MSG_PHONE_ERROR = "MSG_PHONE_ERROR"
MSG_NAME_OK = "MSG_NAME_OK"
name_input = input("Ввести ім`я: ")
name = name_input.strip()
if name.isalpha():
    print(f"{MSG_NAME_OK}: {name.title()}")
else:
    print(MSG_NAME_ERROR)
    age_input = input("Ввести вік:")
    age = age_input.strip()
    if age.isdigit():
        age = int(age)
        print(f"Вік правильний: {age}")
phone_input = input("ввести номер телефону: ")
clean_phone = phone_intput.replace("-", "")
if clean_phone.isdigit():
    print(MSG_PHONE_OK)
else:
    print(MSG_PHONE_ERROR)
    print(MSG_PHONE_FINISH)
