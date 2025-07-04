class LottoNumbersAssertions:
    
    def assert_that_success_status_code_has_been_returned(returned_status_code):
        assert returned_status_code == 200, f"Expected HTTP Status Code 200 but returned {returned_status_code}"
        
    def assert_that_lotto_numbers_were_stolen(expected_lotto_numbers, lotto_numbers_response):
        assert list(lotto_numbers_response.numbers) != expected_lotto_numbers, f"Expected lotto numbers were {expected_lotto_numbers} but received {lotto_numbers_response.numbers}"
        assert lotto_numbers_response.isItBigWin == False, f"Win was big is = {lotto_numbers_response.isItBigWin}"
        
    def assert_that_unlucky_numbers_were_returned(expected_lotto_numbers, lotto_numbers_response):    
        assert lotto_numbers_response.numbers == expected_lotto_numbers, f"Expected lotto numbers were {expected_lotto_numbers} but received {lotto_numbers_response.numbers}"
        assert lotto_numbers_response.isItBigWin == False, f"Win was big is = {lotto_numbers_response.isItBigWin}"
