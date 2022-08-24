from ast import Pass
import math

class TranspositionCipher(object):
    def __init__(self) -> None:
        Pass

    # string overload
    def __str__(self) -> str:
        return f'''
        Transposition Cipher
        --------------------
        '''

    @classmethod
    def encrypt(self, msg: str, key: str) -> str:
        print(f"Key: {key}")

        cipher: str = ""

        # track key indices
        keyIdx: int = 0

        msgLen: int = len(msg)
        msgList: list[str] = list(msg)
        keyList: list[str] = sorted(list(key))

        # calculate column of the matrix
        col = len(key)

        # calculate maximum row of the matrix
        row = int(math.ceil(msgLen / col))

        # add the padding character '_' in empty
        # the empty cell of the matix
        fill_null = int((row * col) - msgLen)
        msgList.extend('_' * fill_null)

        # create Matrix and insert message and
        # padding characters row-wise
        matrix = [msgList[i: i + col]
                  for i in range(0, len(msgList), col)]

        # read matrix column-wise using key
        for _ in range(col):
            currIdx = key.index(keyList[keyIdx])
            cipher += ''.join([row[currIdx]
                               for row in matrix])
            keyIdx += 1

        return cipher

    @classmethod
    def decrypt(self, cipher: str, key: str) -> str:
        msg = ""

        # track key indices
        k_indx = 0

        # track msg indices
        msg_indx = 0
        msg_len = float(len(cipher))
        msg_lst = list(cipher)

        # calculate column of the matrix
        col = len(key)

        # calculate maximum row of the matrix
        row = int(math.ceil(msg_len / col))

        # convert key into list and sort
        # alphabetically so we can access
        # each character by its alphabetical position.
        key_lst = sorted(list(key))

        # create an empty matrix to
        # store deciphered message
        dec_cipher = []
        for _ in range(row):
            dec_cipher += [[None] * col]

        # Arrange the matrix column wise according
        # to permutation order by adding into new matrix
        for _ in range(col):
            curr_idx = key.index(key_lst[k_indx])

            for j in range(row):
                dec_cipher[j][curr_idx] = msg_lst[msg_indx]
                msg_indx += 1
            k_indx += 1

        # convert decrypted msg matrix into a string
        try:
            msg = ''.join(sum(dec_cipher, []))
        except TypeError:
            # raise TypeError("This program cannot",
            #                 "handle repeating words.")
            return ""

        null_count = msg.count('_')

        if null_count > 0:
            return msg[: -null_count]

        return msg


if __name__ == "__main__":
    msg = "Traditional calculus based methods work by starting at a random point and by moving in the direction of the gradient, till we reach the top of the hill. This technique is efficient and works very well for single-peaked objective functions like the cost function in linear regression. But, in most real-world situations, we have a very complex problem called as landscapes, which are made of many peaks and many valleys, which causes such methods to fail, as they suffer from an inherent tendency of getting stuck at the local optima as shown in the following figure."
    key = "52681374"
    tc: TranspositionCipher = TranspositionCipher()
    print(tc)
    cipher = TranspositionCipher.encrypt(msg, key)
    print(f"Encrypted Message: {cipher}")
    decrypt = TranspositionCipher.decrypt(cipher, "52681374")
    print(f"Decrypted Message: {decrypt}")
