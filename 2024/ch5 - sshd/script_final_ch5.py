from typing import Union
import struct

class ChaCha20:
    def __init__(self, key: Union[str, bytes], nonce: Union[str, bytes]):
        # Modified constant for this specific implementation
        # Using "expand 32-byte K" instead of "expand 32-byte k"
        self.constant = b'expand 32-byte K'
        
        self.key = bytes.fromhex(key) if isinstance(key, str) else key
        self.nonce = bytes.fromhex(nonce) if isinstance(nonce, str) else nonce

    @staticmethod
    def rotl(a: int, b: int) -> int:
        return ((a << b) | (a >> (32 - b))) & 0xffffffff

    def quarter_round(self, state: list, a: int, b: int, c: int, d: int) -> None:
        state[a] = (state[a] + state[b]) & 0xffffffff
        state[d] ^= state[a]
        state[d] = self.rotl(state[d], 16)

        state[c] = (state[c] + state[d]) & 0xffffffff
        state[b] ^= state[c]
        state[b] = self.rotl(state[b], 12)

        state[a] = (state[a] + state[b]) & 0xffffffff
        state[d] ^= state[a]
        state[d] = self.rotl(state[d], 8)

        state[c] = (state[c] + state[d]) & 0xffffffff
        state[b] ^= state[c]
        state[b] = self.rotl(state[b], 7)

    def block_function(self, counter: int) -> bytes:
        state = list(struct.unpack('<IIII', self.constant))
        
        state.extend(struct.unpack('<IIIIIIII', self.key))
        
        state.append(counter)
        state.extend(struct.unpack('<III', self.nonce))
        
        working = state.copy()
        
        for _ in range(10):
            self.quarter_round(working, 0, 4, 8, 12)
            self.quarter_round(working, 1, 5, 9, 13)
            self.quarter_round(working, 2, 6, 10, 14)
            self.quarter_round(working, 3, 7, 11, 15)
            
            self.quarter_round(working, 0, 5, 10, 15)
            self.quarter_round(working, 1, 6, 11, 12)
            self.quarter_round(working, 2, 7, 8, 13)
            self.quarter_round(working, 3, 4, 9, 14)

        working = [(working[i] + state[i]) & 0xffffffff for i in range(16)]
        
        return b''.join(struct.pack('<I', x) for x in working)

    def decrypt(self, ciphertext: Union[str, bytes]) -> bytes:

        if isinstance(ciphertext, str):
            ciphertext = bytes.fromhex(''.join(ciphertext.split()))
        
        plaintext = bytearray(len(ciphertext))
        counter = 0
        
        for i in range(0, len(ciphertext), 64):
            keystream = self.block_function(counter)
            chunk = ciphertext[i:i+64]
            
            for j in range(len(chunk)):
                plaintext[i + j] = chunk[j] ^ keystream[j]
            
            counter += 1
        
        return bytes(plaintext)


def main():
    key = "8dec9112eb760eda7c7d87a443271c35d9e0cb878993b4d904aef934fa2166d7"
    nonce = "111111111111111111111111"
    ciphertext = """
    A9 F6 34 08 42 2A 9E 1C 0C 03 A8 08 94 70 BB 8D 
    AA DC 6D 7B 24 FF 7F 24 7C DA 83 9E 92 F7 07 1D 
    02 63 90 2E C1 58
    """

    chacha = ChaCha20(key, nonce)
    decrypted = chacha.decrypt(ciphertext)
    
    print(f"Key: {key}")
    print(f"Nonce: {nonce}")
    print(f"Ciphertext (hex): {ciphertext.strip()}")
    print(f"Decrypted (hex): {decrypted.hex()}")
    print(f"Decrypted (ascii): {decrypted.decode('ascii', errors='ignore')}")


if __name__ == "__main__":
    main()