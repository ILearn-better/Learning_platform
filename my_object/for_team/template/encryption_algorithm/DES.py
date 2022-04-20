from pyDes import des, PAD_PKCS5, ECB


class DES:
    def __init__(self, DES_KEY):
        self.des_obj = des(DES_KEY, ECB, DES_KEY, padmode=PAD_PKCS5)

    def encrypt(self, s):
        s = s.encode()  # 这里中文要转成字节
        secret_bytes = self.des_obj.encrypt(s)  # 用对象的encrypt方法加密
        return secret_bytes.hex()
    def decrypt(self, secret_bytes):
        secret_bytes = bytes.fromhex(secret_bytes)  # 这里中文要转成字节
        s = self.des_obj.decrypt(secret_bytes)  # 用对象的decrypt方法解密
        return s.decode()


if __name__ == '__main__':
    DES_KEY = "12345623"
    while (len(DES_KEY) != 8):
        print("秘钥位数不对，请重新输入！！")
        DES_KEY = input("请输入您的秘钥8位数秘钥:")
    p = DES(DES_KEY)
    s = input("请输入待加密文本:")  # 这里中文要转成字节， 英文好像不用
    test = p.encrypt(s)
    print("加密结果:", test)