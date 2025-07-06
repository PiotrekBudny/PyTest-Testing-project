url = "http://notexistingapi.com/"


def get_winning_lotto_numbers_url(is_person_lucky):
    return f"{url}/winningLottoNumbers?isPersonLucky={is_person_lucky}"