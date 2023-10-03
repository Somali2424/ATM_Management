#!/usr/bin/env python
# coding: utf-8

# CREATING A ACCOUNT CLASS

# In[27]:


class Account():
    def __init__(self,first_name,last_name,account_number,age,date_of_birth):
        self.first_name=first_name.upper()
        self.last_name=last_name.upper()
        self.account_number=account_number
        self.age=age
        self.date_of_birth=date_of_birth
    def account_summary(self):
        print(f"Personal Information\nName:{self.first_name} {self.last_name}\nAge:{self.age}\nDOB:{self.date_of_birth}\nAccount Number:{self.account_number}")


# In[28]:


my_account=Account(first_name='somali',last_name='sen',account_number=1111111,age=18,date_of_birth="8/3/1997")


# In[29]:


my_account.account_summary()


# In[ ]:





# In[30]:


# We are going to inherit the base calss Account in the Checking account class


# In[31]:


class CheckingAccount(Account):
    def __init__(self, first_name, last_name, account_number, age, date_of_birth, deposit_amount):
        # Call the constructor of the parent class (Account) with the correct arguments
        super().__init__(first_name, last_name, account_number, age, date_of_birth)
        self.deposit_amount=deposit_amount
        self.withdraw_whole=0
        self.withdraw_part=0
        
        self.numstr = "%.2f" % deposit_amount
        self.deposit_amount_whole=int(self.numstr[:self.numstr.find('.')])
        self.deposit_amount_part=int(self.numstr[self.numstr.find('.')+1:])
    def deposit(self,deposit_amount):
        self.deposit_amount+=deposit_amount
    def withdraw(self, withdraw_amount):
        
        # separates the whole number from decimal number of the amount to withdraw
        withdraw_amount_str=str(withdraw_amount)
        self.withdraw_whole = int(withdraw_amount_str[:withdraw_amount_str.find('.')])
        self.withdraw_part = int( withdraw_amount_str[ withdraw_amount_str.find('.') + 1:])

        # if the amount in the account is greater than the requested amount,
        # then it is allowed to withdraw that amount
        if self.deposit_amount > float(withdraw_amount):
            #self.deposit_amount_whole -= self.withdraw_whole
            self.deposit_amount_whole-=self.withdraw_whole
            
            if self.withdraw_part > self.deposit_amount_part:
                self.deposit_amount_part = (100-self.withdraw_part)+self.deposit_amount_part
                self.deposit_amount_whole -= 1
            else:
                self.deposit_amount_part -= self.withdraw_part

            # puts back together the whole number and decimal value as one but as a string
            new_amount = str(self.deposit_amount_whole) + "." + str(self.deposit_amount_part)

            # type cast the value back to floating point value
            self.deposit_amount = round(float(self.deposit_amount-withdraw_amount), 2)
        else:
            print("Error! Cannot withdraw larger than what you have.")

    def display_amount(self):
        print(self.deposit_amount)

    def get_amount(self):
        return self.deposit_amount

        


# In[ ]:





# In[32]:


if __name__ == "__main__":
    # Create a CheckingAccount object with an initial deposit of $100.25
    checking_acc = CheckingAccount("John", "Doe", "12345", 30, "01/01/1990", 90)
    
    # Display the initial balance
    checking_acc.display_amount()


# In[33]:


checking_acc.deposit(50.75)
    


# In[34]:


checking_acc.display_amount()


# In[35]:


checking_acc.withdraw(40.90)


# In[36]:


checking_acc.withdraw_part


# In[37]:


checking_acc.display_amount()


# In[38]:


checking_acc.get_amount()


# In[39]:


class SavingsAccount(Account):
    def __init__(self, first_name, last_name, account_number, age, date_of_birth, deposit_amount):
        super().__init__(first_name, last_name, account_number, age, date_of_birth)
        self.deposit_amount=deposit_amount
        self.withdraw_whole=0
        self.withdraw_part=0
        
        self.numstr = "%.2f" % deposit_amount
        self.deposit_amount_whole=int(self.numstr[:self.numstr.find('.')])
        self.deposit_amount_part=int(self.numstr[self.numstr.find('.')+1:])
    def deposit(self,deposit_amount):
        self.deposit_amount+=deposit_amount
    def withdraw(self, withdraw_amount):
        
        # separates the whole number from decimal number of the amount to withdraw
        withdraw_amount_str=str(withdraw_amount)
        self.withdraw_whole = int(withdraw_amount_str[:withdraw_amount_str.find('.')])
        self.withdraw_part = int( withdraw_amount_str[ withdraw_amount_str.find('.') + 1:])

        # if the amount in the account is greater than the requested amount,
        # then it is allowed to withdraw that amount
        if self.deposit_amount > float(withdraw_amount):
            #self.deposit_amount_whole -= self.withdraw_whole
            self.deposit_amount_whole-=self.withdraw_whole
            
            if self.withdraw_part > self.deposit_amount_part:
                self.deposit_amount_part = (100-self.withdraw_part)+self.deposit_amount_part
                self.deposit_amount_whole -= 1
            else:
                self.deposit_amount_part -= self.withdraw_part

            # puts back together the whole number and decimal value as one but as a string
            new_amount = str(self.deposit_amount_whole) + "." + str(self.deposit_amount_part)
            # type cast the value back to floating point value
            self.deposit_amount = round(float(new_amount), 2)
        else:
            print("Error! Cannot withdraw larger than what you have.")

    def display_amount(self):
        print(self.deposit_amount)

    def get_amount(self):
        return self.deposit_amount

        


# In[40]:


if __name__ == "__main__":
    # Create a CheckingAccount object with an initial deposit of $100.25
    checkin_acc = SavingsAccount("John", "Doe", "12345", 30, "01/01/1990", 5129.80)
    
    # Display the initial balance
    checkin_acc.display_amount()


# In[41]:


checkin_acc.withdraw(3000.78)


# In[42]:


checkin_acc.get_amount()


# In[43]:


class BusinessAccount(Account):
    def __init__(self, first_name, last_name, account_number, age, date_of_birth, deposit_amount):
        # Call the constructor of the parent class (Account) with the correct arguments
        super().__init__(first_name, last_name, account_number, age, date_of_birth)
        self.deposit_amount=deposit_amount
        self.withdraw_whole=0
        self.withdraw_part=0
        
        self.numstr = "%.2f" % deposit_amount
        self.deposit_amount_whole=int(self.numstr[:self.numstr.find('.')])
        self.deposit_amount_part=int(self.numstr[self.numstr.find('.')+1:])
    def deposit(self,deposit_amount):
        self.deposit_amount+=deposit_amount
    def withdraw(self, withdraw_amount):
        
        # separates the whole number from decimal number of the amount to withdraw
        withdraw_amount_str=str(withdraw_amount)
        self.withdraw_whole = int(withdraw_amount_str[:withdraw_amount_str.find('.')])
        self.withdraw_part = int( withdraw_amount_str[ withdraw_amount_str.find('.') + 1:])

        # if the amount in the account is greater than the requested amount,
        # then it is allowed to withdraw that amount
        if self.deposit_amount > float(withdraw_amount):
            #self.deposit_amount_whole -= self.withdraw_whole
            self.deposit_amount_whole-=self.withdraw_whole
            
            if self.withdraw_part > self.deposit_amount_part:
                self.deposit_amount_part = (100-self.withdraw_part)+self.deposit_amount_part
                self.deposit_amount_whole -= 1
            else:
                self.deposit_amount_part -= self.withdraw_part

            # puts back together the whole number and decimal value as one but as a string
            new_amount = str(self.deposit_amount_whole) + "." + str(self.deposit_amount_part)
            # type cast the value back to floating point value
            #self.deposit_amount = round(float(self.deposit_amount-withdraw_amount), 2)
            self.deposit_amount = round(float(new_amount), 2)
        else:
            print("Error! Cannot withdraw larger than what you have.")

    def display_amount(self):
        print(self.deposit_amount)

    def get_amount(self):
        return self.deposit_amount

        


# In[18]:


pip install ipywidgets


# In[44]:


import ipywidgets as widgets
from IPython.display import display


# In[54]:


l=widgets.ToggleButtons(
    options=['checking account', 'savings account', 'business account'],
    description='Account Type:',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltips=['Description of checking account', 'Description of savings account', 'Description of business account'],
    # icons=['check'] * 3
)


# In[56]:


l


# In[57]:


l.value


# In[ ]:


if __name__ == '__main__':
    isSessionOn = True
    isCustomer = False

    def initialise_objects():
        global Abc_checking, Abc_savings, Abc_business, master_list

        Abc_checking = CheckingAccount("John", "Doe", "123458989", 30, "01/01/1991", 12390.75)
        Abc_savings = SavingsAccount("Somali","Dasgupta","20123567",44,'8/3/1980', 125896.01)
        Abc_business = BusinessAccount("Somali","Dasgupta","20123567",44,'8/3/1980',60000.89)
        master_list = [[Abc_checking, "123458989", "checking account"], [Abc_savings, "20123567", "savings account"], [Abc_business, "20123567", "business account"]]

        return None

    initialise_objects()

    while isSessionOn is True:
        print("Welcome to 24-hour ATM service.")
        print("Insert your card.")

        # Card reading the customer info representation
        customerID = input("Enter your customer id number: ")
        print("\n")

        cust_accounts = []
        for i in master_list:
            if i[1] == customerID:
                cust_accounts.append(i[2])
                isCustomer = True

        if isCustomer is True:
            isAccountSelected = False

            while isAccountSelected is False:
                
                acc_type_widg=widgets.ToggleButtons(
                    options=['checking account', 'savings account', 'business account'],
                    description='Account Type:',
                    disabled=False,
                    button_style='', # 'success', 'info', 'warning', 'danger' or ''
                    tooltips=['Description of checking account', 'Description of savings account', 'Description of business account'])
    # icons=['check'] * 3
                display(acc_type_widg)
                
                #print("Enter 1 for checking account")
                #print("Enter 2 for savings account")
                #print("Enter 3 for business account")
                account_type = acc_type_widg.value

                if account_type in cust_accounts:
                    for x in master_list:
                        if account_type == x[2]:
                            objectName = x[0]

                    isAccountSelected = True
                    isAccountSessionOn = True

                    while isAccountSessionOn is True:
                        print("\nHow may I help you?")
                        print("Press 1 for balance view.")
                        print("Press 2 for withdrawals")
                        print("Press 3 to exit.")
                        action_value = input("Please enter your choice: ")

                        if action_value == "1":
                            objectName.display_amount()
                            print("\n")

                        if action_value == "2":
                            amnt_to_withdraw = float(input("Enter the amount to withdraw: "))
                            temp_str = str(amnt_to_withdraw)

                            adjusted_amount = "%.2f" % amnt_to_withdraw
                            # print "adjusted_amount:", adjusted_amount
                            objectName.withdraw(float(adjusted_amount))

                            print("current balance is", objectName.get_amount())
                            print("\n")

                        if action_value == "3":
                            isAccountSessionOn = False
                            print("Thank for using the 24-hour ATM service.")
                            print("Have a pleasant day.")
                            print("\n\n")
                            print("##########################################")
                else:
                    print("Error. You don't have that account.")
                    print("Please try again.\n")

        else:
            print("Cannot find your record.")
            print("Please get your card.")
            print("Exiting this session...")


# In[ ]:





# In[ ]:





# In[ ]:




