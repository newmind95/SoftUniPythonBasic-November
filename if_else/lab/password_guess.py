password = input()

is_valid_password = password == "s3cr3t!P@ssw0rd"

if is_valid_password:
    print("Welcome")
else:
    print("Wrong password!")
