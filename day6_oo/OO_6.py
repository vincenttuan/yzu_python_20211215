class Account:
    def __init__(self, name, balance) -> None:
        self.name = name
        self.__balance = balance

    def __str__(self) -> str:
        return "%s 的帳戶餘額 $%d" % (self.name, self.__balance)

    def deposit(self, amount):  # 存款
        if amount > 0:
            self.__balance = self.__balance + amount
            return True, '存款成功'
        else:
            return False, '存款失敗。存款金額不正確 $%d' % amount

    def withdrawal(self, amount):  # 提款
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
            return True, '提款成功'
        else:
            return False, '提款失敗。提款金額過大 $%d' % amount

if __name__ == '__main__':
    a = Account('Vincent', 10000)
    b = Account('Anita', 6000)
    print(a, b)
    # 存款(deposit) 提款 (withdrawal)
    state, message = a.deposit(3000)
    print(state, message, a)
    state, message = b.withdrawal(2000)
    print(state, message, b)