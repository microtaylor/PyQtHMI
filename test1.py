# coding :utf-8

class Card:
    def __init__(self, card_no):
        '''初始化方法'''
        self.card_no = card_no
        self.__money = 0

    def set_money(self, money):
        if money % 100 == 0:
            self.__money += money
            print("存钱成功！")
        else:
            print("不是一百的倍数")

    def get_money(self):
        return self.__money

    def __str__(self):
        return "卡号%s,余额%d" % (self.card_no, self.__money)

    # 删除money属性
    def del_money(self):
        print("----->要删除money")
        # 删除类属性
        del Card.money

    money = property(get_money, set_money)


c = Card("4559238024925290")
print(c)

c.money = 500
print(c.money)

print(Card.money.__doc__)

from motor.common.basic import ss, FactoryTest

print(ss)
FactoryTest.Query()

# 删除
