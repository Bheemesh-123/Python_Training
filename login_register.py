def loginandreg():
    d={}
    print("Welcome to Registration")
    u_name=input("Enter the username:")
    u_pwd=input("Enter the user password:")
    name=input("Enter the name:")
    phone_no=input("Enter the phone number:")
    d[u_name]=u_pwd
    u_name=u_pwd
    while(True):
        print("Welcome to Login")
        l_name=input("Enter the username:")
        l_pwd=input("Enter the password:")
        if l_name in d:
            if d[l_name]==l_pwd:
                print("Login Success")
                break
            else:
                print("Enter valid passcode")
        else:
            print("User not found")
            break
loginandreg()