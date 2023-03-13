from tkinter import Tk, Entry, Button, Label
import string
import random

root = Tk()

root.title("Password Generator")
#root.geometry('400x100+0+0')
global  password_history 
password_history = []

def generate_password() :
    
    
    password_characters = list(string.ascii_letters+string.ascii_lowercase+string.ascii_uppercase+string.punctuation+"!@#$%&_")
    random.shuffle(password_characters)
    password_length = 12

    global password 
    password = []

    for i in range(password_length) :
        password.append(random.choice(password_characters))
    
    random.shuffle(password_characters)
    password = "".join(password)
    
    password_result = Label(root, text="Generated Password: " + password, font=('Arial semi-Bold', 10) )
    password_result.grid(row=4)

    # show_history.grid(row=5, pady=10)
   
    password_history.append(password)
    showHistory()
    # for passwords in password_history :
    #     print("Password: " + passwords)
        
def showHistory() :
        print(password_history)




# Create Widget
header = Label(root, text="Password Generator", font=('Arial Bold', 28))
subHeader = Label(root, text="Do you Want to Generate a New Password?")
yes_button = Button(root, text='Yes', command=generate_password)
no_button = Button(root, text='No', command=root.quit)



# history_button = Button(root, text="Show History")
# show_history = Button(root, text="Show History", width=10, command=showHistory)



# Display Widget
header.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
subHeader.grid(row=1, column=0, columnspan=2, pady=5)
yes_button.grid(row=2, column=0)
no_button.grid(row=2, column=1, pady=10)




root.mainloop()
