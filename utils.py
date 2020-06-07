class Utils:
    @staticmethod
    def xor(block1, block2):
        return bytes([a ^ b for a, b in zip(block1, block2)])
