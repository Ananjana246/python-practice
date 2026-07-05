# action function
def log(message):
    with open(r"C:\Main\Python\app.log","a") as file:
        file.write(message + "\n")
# log("hello")
# log("good morning")

# transformation function
def clean(email):
    cl_email=email.strip().lower()
    username,domain=cl_email.split("@")
    return {"username":username,"domain":domain}
# print(clean("ananjanak246@gmail.com"))

# validation function
def valid(password):
    return len(password)>=8
# print(valid("anank"))

def valid_email(email):
   return "@" in email and "." in email
# print(email("ananjana.com"))
# print(email("ananjana@gmail.com"))

# Orchestrator function
def process_user_email(email):
    log("app started")
    # check if it is valid
    # if not, we log the problem
    if not valid_email(email):
        log(f"invalid email receive:{email}")
    # if  valid, we clean it and store structured info 
    else:
        clean_email=clean(email)
        log(f"processed email:{clean_email}") # we log what happened
    log("app stopped")

          
email=input("enter your email: ") # we receive an email from the user
process_user_email(email)