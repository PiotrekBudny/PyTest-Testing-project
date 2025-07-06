class LottoNumbersAssertions:
    def __init__(self, lotto_numbers_response, returned_status_code):
        self.lotto_numbers_response = lotto_numbers_response
        self.returned_status_code = returned_status_code

    def assert_that_success_status_code_has_been_returned(self):
        assert self.returned_status_code == 200, f"Expected HTTP Status Code 200 but returned {self.returned_status_code}"
        return self

    def assert_that_lotto_numbers_were_stolen(self, expected_lotto_numbers):
        assert list(self.lotto_numbers_response.numbers) != expected_lotto_numbers, \
            f"Expected lotto numbers were {expected_lotto_numbers} but received {self.lotto_numbers_response.numbers}"
        assert self.lotto_numbers_response.is_it_big_win == False, \
            f"Win was big is = {self.lotto_numbers_response.is_it_big_win}"
        return self

    def assert_that_unlucky_numbers_were_returned(self, expected_lotto_numbers):
        assert self.lotto_numbers_response.numbers == expected_lotto_numbers, \
            f"Expected lotto numbers were {expected_lotto_numbers} but received {self.lotto_numbers_response.numbers}"
        assert self.lotto_numbers_response.is_it_big_win == False, \
            f'Win was big is = {self.lotto_numbers_response.is_it_big_win}'
        return self
