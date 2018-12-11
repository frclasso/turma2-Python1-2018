class NetWorkError(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise NetWorkError('Bad hostname')
except NetWorkError as e:
    print(e.args)

c = NetWorkError('Google')
print(c)