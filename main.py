from tkinter import *
from tkinter import messagebox, simpledialog


class BankApp:
    def __init__(self):
        self.budget = self.read_account_balance()
        self.setup_gui()

    def setup_gui(self):
        window = Tk()
        window.config(padx=50, pady=50)
        window.title("Bank App")
        canvas=Canvas(width=250,height=104)
        bank_pic=PhotoImage(file="./bank.png")
        picture=canvas.create_image(125,52,image=bank_pic)
        canvas.grid(row=0,column=1)
        withdraw_img = PhotoImage(file="./withdraw.png")
        deposit_img = PhotoImage(file="./deposit.png")
        money_transfer_pic = PhotoImage(file="./money_transfer_pic.png")

        # GUI setup code (buttons, images, etc.)

        deposit_button = Button(window,image=deposit_img, text="Deposit Money", command=self.deposit_money)
        deposit_button.grid(row=2, column=0)

        withdraw_button = Button(window,image=withdraw_img, text="Withdraw Money", command=self.withdraw_money)
        withdraw_button.grid(row=2, column=2)

        money_transfer_button = Button(window,image=money_transfer_pic, text="Money Transfer", command=self.money_transfer)
        money_transfer_button.grid(row=3, column=0)
        balance_pic=PhotoImage(file="account-balance.png")
        account_balance_image=PhotoImage(file="./account-balance.png")
        account_balance_button = Button(window,image=account_balance_image, text="Account Balance", command=self.display_account_balance)
        account_balance_button.grid(row=3, column=2)

        window.mainloop()

    def save_account_balance(self):
        with open("money.txt", "w") as file:
            file.write(str(self.budget))

    def read_account_balance(self):
        try:
            with open("money.txt", "r") as file:
                return float(file.read())
        except (FileNotFoundError, ValueError):
            with open("money.txt","w")as file:
                file.write(str(0))
            return 0.00

    def deposit_money(self):
        amount = simpledialog.askfloat(title="Deposit Amount", prompt="Enter amount: £", minvalue=0, maxvalue=15000)
        if amount is not None:
            self.budget += amount
            self.save_account_balance()

    def withdraw_money(self):
        amount = simpledialog.askfloat(title="Withdrawal Amount", prompt="Enter amount: £", minvalue=0, maxvalue=15000)
        if amount:
            if amount<= self.budget:
                self.budget -= amount
                self.save_account_balance()
            else:
                messagebox.showwarning(title="Ooooops",message=f" You currently have {self.budget}. There is not enough amount for transaction")

    def money_transfer(self):
        amount = simpledialog.askfloat(title="Money Transfer Amount", prompt="Enter amount: £", minvalue=0,
                                       maxvalue=15000)
        if amount:
            if amount<=self.budget:

                account_number = simpledialog.askstring(title="Money Transfer Bank Details", prompt="Enter Account Number")
                while len(account_number)!=8 or not account_number.isdigit():
                    account_number = simpledialog.askstring(title="Money Transfer Bank Details",
                                                            prompt="Enter 8-digit Account Number")

                sort_code = simpledialog.askstring(title="Money Transfer Bank Details", prompt="Enter Sort Code")
                while len(sort_code)!=6 or not sort_code.isdigit():
                    sort_code = simpledialog.askstring(title="Money Transfer Bank Details", prompt="Enter six-digit Sort Code")

                sort_code = f"{sort_code[0:2]}-{sort_code[2:4]}-{sort_code[4:6]}"

                self.budget -= amount
                self.save_account_balance()

                messagebox.showinfo(title="Money Transfer", message=f"£{amount} transferred to\n"
                                                                f"Account Number: {account_number}\n"
                                                                f"Sort Code: {sort_code}")

            else:
                messagebox.showwarning(title="Ooooops",
                                       message=f" You currently have {self.budget}. There is not enough amount for money transfer")
        else:
            messagebox.showerror(title="Ooooops",message="Please enter a number")

    def display_account_balance(self):
        money_in_bank = self.read_account_balance()
        messagebox.showinfo(title="Balance Information", message=f"Account Balance is £{money_in_bank}0")
        self.budget = money_in_bank


if __name__ == "__main__":
    app = BankApp()