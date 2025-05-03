print ("Please enter the required info to login")
username = input("Username: ")
password = input("Password: ")
age = input("Age: ")

if username == "admin" and password == "admin" and age >= "18":
    otp = input("Enter OTP: ")
    if otp == "123456":
        print("Access Granted")
    else:
        print("Invalid OTP")
else:
    print("Access Denied")
