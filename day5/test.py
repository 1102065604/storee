class Account:
    account = 1
    username = '1'
    password = '2'

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        info = '''
                ------------个人信息------------
                        用户名:%s
                        账号:%s
                        密码:%s
                '''
        return info % (self.account, self.username, self.password)

account1 = Account()
account1.account = 110
account1.username = 'username01'

account2 = Account()
account2.account = 220
account2.username = 'username02'

accountList = []
accountList.append(account1)
accountList.append(account2)


def get(selectKey: str, selectVal: str) -> Account:
    for item in accountList:
        if selectKey == 'account':
            if str(item.account) == selectVal:
                return item
            else:
                continue
        elif selectKey == 'username':
            if item.username == selectVal:
                return item
            else:
                continue
        elif selectKey == 'password':
            if item.password == selectVal:
                return item
            else:
                continue
        else:
            print('wrong search key')
        return None
    print('can not find account')
    return None

print(get('account','110'))

print(get('as','asdf') == None)