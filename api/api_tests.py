import requests
import pytest
import api_route_builder
from models.post_response import PostResponse
from models.create_post_request import CreatePostRequest

class TestJsonPlaceholderAPI:
    
    @pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
    def test_get_post_by_id_returns_200_and_correct_id(self, post_id):
        expected_http_status = 200
        url = api_route_builder.build_get_post_by_id_route(post_id)

        response = requests.get(url)
        json_response = response.json()
        get_post_response = PostResponse(**json_response)

        assert response.status_code == expected_http_status, f"Expected status code {expected_http_status}, got {response.status_code}"
        assert get_post_response.id == post_id, f"Expected post ID {post_id}, got {json_response.get('id')}"
        assert get_post_response.userId is 1, "Expected 'userId' to be present in the response and equal to 1"
        assert get_post_response.title is not None, "Expected 'title' to be present in the response"
        assert get_post_response.body is not None, "Expected 'body' to be present in the response"

    def test_get_post_by_id_returns_404_for_nonexistent_id(self):
        nonexistent_post_id = 10000
        expected_http_status = 404
        url = api_route_builder.build_get_post_by_id_route(nonexistent_post_id)

        response = requests.get(url)

        assert response.status_code == expected_http_status, f"Expected status code {expected_http_status}, got {response.status_code}"

    def test_get_post_by_id_returns_404_for_invalid_id(self):
        invalid_post_id = "invalid"
        expected_http_status = 404
        url = api_route_builder.build_get_post_by_id_route(invalid_post_id)

        response = requests.get(url)

        assert response.status_code == expected_http_status, f"Expected status code {expected_http_status}, got {response.status_code}"

    def test_get_all_posts_returns_200(self):
        expected_http_status = 200
        expected_number_of_posts = 100
        url = api_route_builder.build_get_all_posts_route()

        response = requests.get(url)

        assert response.status_code == expected_http_status, f"Expected status code {expected_http_status}, got {response.status_code}"

        json_response = response.json()
        actual_number_of_posts = len(json_response)
        assert isinstance(json_response, list), "Expected response to be a list of posts"
        assert actual_number_of_posts == expected_number_of_posts, f"Expected 100 posts, got {actual_number_of_posts}"

    def test_create_post_returns_201_for_valid_request(self):
        expected_http_status = 201
        url = api_route_builder.build_create_post_route()
        create_post_request = CreatePostRequest(userId=1, title="Test Title", body="Test Body")

        response = requests.post(url, json=create_post_request.__dict__, headers={"Content-Type": "application/json"})
        response_json = response.json()
        create_post_response = PostResponse(**response_json)

        assert response.status_code == expected_http_status, f"Expected status code {expected_http_status}, got {response.status_code}"
        assert create_post_response.userId == create_post_request.userId, "Expected 'userId' in response to match request"
        assert create_post_response.title == create_post_request.title, "Expected 'title' in response to match request"
        assert create_post_response.body == create_post_request.body, "Expected 'body' in response to match request"
        assert create_post_response.id is not None, "Expected 'id' to be present in the response"