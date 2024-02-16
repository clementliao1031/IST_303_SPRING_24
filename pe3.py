from datetime import date, timedelta

def encode(input_text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_list = list(alphabet)

    def encode_letter(letter):
        if letter.isalpha(): 
            is_upper = letter.isupper()
            letter = letter.lower()
            index = (alphabet_list.index(letter) + shift) % 26
            encoded_letter = alphabet_list[index]
            if is_upper:
                encoded_letter = encoded_letter.upper()
            return encoded_letter
        else:
            return letter
    
    encoded_text = ''.join(encode_letter(char) for char in input_text)
    return alphabet_list, encoded_text



def decode(input_text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    def decode_letter(letter):
        if letter.isalpha():
            is_upper = letter.isupper()
            letter = letter.lower()
            index = (alphabet.index(letter) - shift) % 26
            decoded_letter = alphabet[index]
            if is_upper:
                decoded_letter = decoded_letter.upper()
            return decoded_letter
        else:
            return letter
    
    decoded_text = ''.join(decode_letter(char) for char in input_text)
    return decoded_text



class BankAccount:
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        self.name = name
        self.ID = ID
        self.creation_date = creation_date if (creation_date and creation_date <= date.today()) else date.today()
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            pass
        else:
            self.balance += amount
            print(f"Deposit of ${amount} successful. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount < 0:
            pass
        if self.balance < amount:
            print("Insufficient funds. Withdrawal unsuccessful.")
        else:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")

    def view_balance(self):
        print(f"Current balance: ${self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        super().__init__(name, ID, creation_date, balance)

    def withdraw(self, amount):
        if (date.today() - self.creation_date).days < 180:
            pass
        else:
            super().withdraw(amount)

class CheckingAccount(BankAccount):
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0, overdraft_fee=30):
        super().__init__(name, ID, creation_date, balance)
        self.overdraft_fee = overdraft_fee

    def withdraw(self, amount):
        if self.balance - amount < 0:
            pass
            super().withdraw(amount + self.overdraft_fee)
        else:
            super().withdraw(amount)