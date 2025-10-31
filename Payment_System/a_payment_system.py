class PaymentSystem:
    def __init__(self):
        self.admin_store = {}
        self.user_info = {}

    def user_reg(self, user_name, user_ph_no, user_bank_acc_no):
        self.user_name = user_name
        self.user_ph_no = user_ph_no
        self.user_bank_acc_no = user_bank_acc_no
        self.mps_id = 'mps_' + user_bank_acc_no[-3:]
        self.user_info['user_name'] = self.user_name
        self.user_info['user_ph_no'] = self.user_ph_no
        self.user_info['user_bank_acc_no'] = self.user_bank_acc_no
        self.admin_store[self.mps_id] = self.user_info

    def get_mpsid(self):
        return self.mps_id

    def admin(self):
        return self.admin_store


p = PaymentSystem()

user_name = input("Enter your name: ")
user_ph_no = input("Enter your ph_no: ")
user_bank_acc_no = input("Enter your bank_acc_no: ")

p.user_reg(user_name, user_ph_no, user_bank_acc_no)
print(p.admin())
