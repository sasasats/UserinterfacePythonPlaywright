import random



class RandomUtils:
    @staticmethod
    def get_random_int(number: int):
        return random.randint(0, number)