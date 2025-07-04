import random
class LottoNumbersGenerator:
    
    def get_lotto_numbers(self):
        return random.sample(range(1, 50), 6)
    
    def get_lucky_lotto_numbers(self):
        lucky_number = random.randint(1,44)
        return [lucky_number + i for i in range(6)]