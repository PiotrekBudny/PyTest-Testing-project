import requests
import pytest
from api import api_route_builder
from api.models.create_post_request import CreatePostRequest
from api.api_assertions import ApiAssertions

class TestJsonPlaceholderAPI:
    
    @pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
    def test_get_post_by_id_returns_200_and_correct_id(self, post_id):
        expected_http_status = 200
        url = api_route_builder.build_get_post_by_id_route(post_id)

        response = requests.get(url)

        ApiAssertions(response).assert_status_code(expected_http_status)
        ApiAssertions(response).assert_post_response(post_id)

    def test_get_post_by_id_returns_404_for_nonexistent_id(self):
        nonexistent_post_id = 10000
        expected_http_status = 404
        url = api_route_builder.build_get_post_by_id_route(nonexistent_post_id)

        response = requests.get(url)

        ApiAssertions(response).assert_status_code(expected_http_status)
        
    def test_get_post_by_id_returns_404_for_invalid_id(self):
        invalid_post_id = "invalid"
        expected_http_status = 404
        url = api_route_builder.build_get_post_by_id_route(invalid_post_id)

        response = requests.get(url)

        ApiAssertions(response).assert_status_code(expected_http_status)

    def test_get_all_posts_returns_200(self):
        expected_http_status = 200
        expected_number_of_posts = 100
        url = api_route_builder.build_get_all_posts_route()

        response = requests.get(url)

        ApiAssertions(response).assert_status_code(expected_http_status)
        ApiAssertions(response).assert_get_all_posts_response(expected_number_of_posts)

    def test_create_post_returns_201_for_valid_request(self):
        expected_http_status = 201
        url = api_route_builder.build_create_post_route()
        create_post_request = CreatePostRequest(userId=1, title="Test Title", body="Test Body")

        response = requests.post(url, json=create_post_request.__dict__, headers={"Content-Type": "application/json"})

        ApiAssertions(response).assert_status_code(expected_http_status)
        ApiAssertions(response).assert_create_post_response(create_post_request)
