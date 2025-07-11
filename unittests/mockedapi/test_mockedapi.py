from unittests.mockedapi.utils.lotto_numbers_generator import LottoNumbersGenerator
from unittests.mockedapi.not_existing_api_handler import NotExistingApiHandler
from unittests.mockedapi.assertions.lotto_numbers_assertions import LottoNumbersAssertions


class TestNotExistingApi:

    def test_mocked_get_winning_lotto_numbers_if_person_is_lucky(self, mocker):
        list_of_lucky_numbers = LottoNumbersGenerator().get_lucky_lotto_numbers()
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"numbers": list_of_lucky_numbers, "is_it_big_win": True}

        mocker.patch("requests.get", return_value=mock_response)

        response_status_code, lotto_numbers_response = NotExistingApiHandler().get_winning_lotto_numbers(
            is_person_lucky=True)

        LottoNumbersAssertions(lotto_numbers_response, response_status_code)\
            .assert_that_success_status_code_has_been_returned()\
            .assert_that_lotto_numbers_were_stolen(list_of_lucky_numbers)

    def test_mocked_get_winning_lotto_numbers_if_person_is_not_lucky(self, mocker):
        list_of_numbers = LottoNumbersGenerator().get_lotto_numbers()
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"numbers": list_of_numbers, "is_it_big_win": False}

        mocker.patch("requests.get", return_value=mock_response)

        response_status_code, lotto_numbers_response = NotExistingApiHandler().get_winning_lotto_numbers(
            is_person_lucky=False)

        LottoNumbersAssertions(lotto_numbers_response, response_status_code)\
            .assert_that_success_status_code_has_been_returned()\
            .assert_that_unlucky_numbers_were_returned(list_of_numbers)
