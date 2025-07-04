import requests
from unittests.mockedapi import not_existing_api_url_builder
from unittests.mockedapi.models.lotto_numbers_response import LottoNumbersResponse
from unittests.mockedapi.utils.lotto_numbers_generator import LottoNumbersGenerator

class NotExistingApiHandler:
    
    def get_winning_lotto_numbers(self, isPersonLucky):
        url = not_existing_api_url_builder.get_winning_lotto_numbers_url(isPersonLucky)
        
        http_response =  requests.get(url)
        
        json_response = http_response.json()
        lotto_numbers_response = LottoNumbersResponse(**json_response)
        
        if lotto_numbers_response.isItBigWin == True:
            stolen_numbers = lotto_numbers_response.numbers
            print(f"Stolen numbers are: {stolen_numbers}")
            
            lotto_numbers_response.numbers = LottoNumbersGenerator().get_lotto_numbers()
            lotto_numbers_response.isItBigWin = False
            return http_response.status_code, lotto_numbers_response
        else:
            return http_response.status_code, lotto_numbers_response
