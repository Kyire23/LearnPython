from itertools import cycle
def crypt(text, key):
    result = []
    keys = cycle(key)
    for ch in text:
        result.append(chr(ord(ch)^ord(next(keys))))
    return ''.join(result)
#测试代码
if __name__=='__main__':
    plain = 'The quick brown fox jumps over the lazy dog'
    key = 'Python_1'
    print('加密前明文：{}'.format(plain))
    encrypted = crypt(plain, key)
    print('加密后密文：{}'.format(encrypted))
    decrypted = crypt(encrypted, key)
    print('解密后明文：{}'.format(decrypted))
