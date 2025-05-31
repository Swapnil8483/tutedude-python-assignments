first_nm = input("Enter your first name :")
last_nm = input("Enter your last name :")

full_nm = first_nm + " " + last_nm

msg = ("Hello, ") + (full_nm.title()) + ("! Welcome to the python program.")
print(msg)

'''
Or It can also be done as follows.

print(f"Hello, {first_nm.title()} {last_nm.title()}! Welcome to the python program.")
'''