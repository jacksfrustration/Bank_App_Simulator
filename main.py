from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
def save_account_balance(money):
    '''saves the current balance to the text file. first the variable is converted to string
    so it can be written in the text file'''
    with open("money.txt","w")as file:
        str_money=str(money)
        file.write(str_money)
def read_account_balance():
    '''outputs the money in the account based on the contents of the text file
    if the text file doesnt exist create it. If the text file is vacant
    fill it with the default value of 0'''
    try:
        with open("money.txt","r") as file:
            money=float(file.read())
    except FileNotFoundError:
        with open("money.txt","w")as file:
            money=0.00
            str_money=str(money)
            file.write(str_money)
    except ValueError:
        with open("money.txt","w")as file:
            money=0.00
            str_money=str(money)
            file.write(str_money)
    return money
budget=read_account_balance()



def deposit_money():
    '''deposit money in the account. saves the new balance to the text file'''
    global budget
    amount = simpledialog.askfloat(title="Deposit Amount", prompt="Enter amount: £", parent=window, minvalue=0,
                                   maxvalue=15000)
    budget += amount
    save_account_balance(budget)



def withdraw_money():
    '''this function simulates a money withdrawal
    if the remaining value after the money withdrawal is less than 0
    it then sends the money back to the account and opens
    a messagebox with an appropriate message'''
    global budget
    amount = simpledialog.askfloat(title="Withdrawal Amount", prompt="Enter amount: £", parent=window, minvalue=0,
                                   maxvalue=15000)
    budget -= amount
    if budget<0:
        budget+=amount
        messagebox.showerror(title="Ooops",message="You don't have enough money for this transaction.\n"
                                                   "You are getting your money back!!")
        return None
    save_account_balance(budget)

def money_transfer():
    '''this function simulates a money transfer
    there is a pop up window for the amount of money to be sent
    another about the sort code of the receiving account
    and finally one more for the account number of the receiving account
        if the remaining value after the money transfer is less than 0
        it then sends the money back to the account and opens
        a messagebox with an appropriate message'''
    global budget
    amount = simpledialog.askfloat(title="Money Transfer Amount", prompt="Enter amount: £", parent=window, minvalue=0,
                                   maxvalue=15000)
    account_number=simpledialog.askstring(title="Money Transfer Bank Details",prompt="Enter Account Number",parent=window)
    sort_code=simpledialog.askstring(title="Money Transfer Bank Details",prompt="Enter Sort Code",parent=window)
    sort_code=f"{sort_code[0:2]}-{sort_code[2:4]}-{sort_code[4:6]}"

    budget -= amount
    if budget<0:
        budget+=amount
        messagebox.showerror(title="Ooops",message="You don't have enough money for this transaction.\nYou are getting your money back!!")
        return None

    save_account_balance(budget)
    messagebox.showinfo(title="Money Transfer",message=f"£{amount} is being transferred to\n"
                                                       f"Account Number : {account_number}\n"
                                                       f"Sort Code: {sort_code}")


def display_account_balance():
    '''displays account balance based in the text file contents'''
    global budget
    money_in_bank=read_account_balance()

    messagebox.showinfo(title="Balance Information",message=f"Account Balance is £{money_in_bank}0")
    budget=money_in_bank


window=Tk()
window.config(padx=50,pady=50)
window.title("Bank App")
canvas=Canvas(width=250,height=104)
bank_pic=PhotoImage(file="./bank.png")
picture=canvas.create_image(125,52,image=bank_pic)
canvas.grid(row=0,column=1)
withdraw_img=PhotoImage(file="./withdraw.png")
deposit_img=PhotoImage(file="./deposit.png")
money_transfer_pic=PhotoImage(file="./money_transfer_pic.png")
deposit_button=Button(window,text="Deposit Money",image=deposit_img,command=deposit_money,compound=BOTTOM)
deposit_button.grid(row=2,column=0)
withdraw_button=Button(window,text="Withdraw Money",image=withdraw_img,command=withdraw_money,compound=BOTTOM)
withdraw_button.grid(row=2,column=2)
money_transfer_button=Button(window,text="Money Transfer",image=money_transfer_pic,command=money_transfer,compound=BOTTOM)
money_transfer_button.grid(row=3,column=0)

account_balanace_image=PhotoImage(file="./account-balance.png")
account_balanace_button=Button(window,text="Account Balance",image=account_balanace_image,command=display_account_balance,compound=BOTTOM)
account_balanace_button.grid(row=3,column=2)
window.mainloop()