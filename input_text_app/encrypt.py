import random

def encrypt_text(text):
    # 文字を2進数に変換
    afterBin = [f'{ord(i):b}'.zfill(8) for i in text]
    cryptList = [bin(random.randint(33, 126)) for _ in range(len(afterBin))]
    cryptSentence = [bin(int(a, 2) ^ int(b, 2)) for a, b in zip(afterBin, cryptList)]

    # 有効なASCII範囲のチェックと修正
    for k, c in enumerate(cryptSentence):
        while not (32 < int(c, 2) < 127):
            randomNumber = bin(random.randint(33, 126))
            retake = bin(int(afterBin[k], 2) ^ int(randomNumber, 2))
            if 32 < int(retake, 2) < 127:
                cryptSentence[k] = retake
                cryptList[k] = randomNumber

    # 暗号化された文と鍵を文字に変換
    encrypted_text = "".join(chr(int(b, 2)) for b in cryptSentence)
    key_text = "".join(chr(int(b, 2)) for b in cryptList)
    return encrypted_text, key_text
