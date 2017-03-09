import datetime

class chap_Money:

	"""docstring for mobile_Money"""
	def __init__(self,name,phone_number,balance,deposits,withdrawals):
		self.name=input("Please Enter Your Name")
		self.phone_number=input("[Please Enter Your Phone Number")
		self.balance=0
		self.deposits=[]
		self.withdrawals=[]

		print("Dear {} Welcome To CHAP".format(self.name))
		print("Start By Depositing Some Money")

	def deposit_cash(self, amount):
		if amount < 50:
			print("Dear Customer, Sorry You Cannot Deposit less than 50")
		else:
			self.balance+=amount
		print("Thank you {} for using CHAP. Your current balance is {}".format(self.name,self.balance))

		Time=datetime.datetime.now()

		deposit_details={"Time":datetime.datetime.now(), "Amount":amount}
		self.deposits.append(deposit_details)
		

	def show_balance(self):
		print("Thank you {} for using CHAP.Your current balance is {}".format(self.name,self.balance))

	def withdraw_cash(self, amount):
		if amount < 500:
			print("Dear Customer, You Cannot withdraw less than 500")

		elif amount > self.balance:
			print("Dear Customer, you have insufficient funds to complete transaction")
		else:
			self.balance-=amount
			print("Thank you {} for using CHAP. Your current balance is {}".format(self.name, self.balance))

		Time=datetime.datetime.now()

		withdrawal_details={"Time":datetime.datetime.now(), "Amount":amount}
		self.withdrawals.append(withdrawal_details)

	def show_deposits(self):
		for deposit in self.deposits: 
			print("Dear {} Thank You For Using CHAP,On {} You deposited {}".format(self.name, deposit["Time"].strftime("%c"), deposit["Amount"]))
			
	







	

		
