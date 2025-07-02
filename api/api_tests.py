import requests
import pytest
import api_route_builder
from models.get_post_response import GetPostResponse

@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_get_post_by_id_returns_200_and_correct_id(post_id):
    expected_http_status = 200
    url = api_route_builder.build_get_post_by_id_route(post_id)
    
    response = requests.get(url)
    json_response = response.json()
    get_post_response = GetPostResponse(**json_response)
    
    assert response.status_code == expected_http_status, f"Expected status code {expected_http_status}, got {response.status_code}"
    assert get_post_response.id == post_id, f"Expected post ID {post_id}, got {json_response.get('id')}"
    assert get_post_response.userId is 1, "Expected 'userId' to be present in the response and equal to 1"
    assert get_post_response.title is not None, "Expected 'title' to be present in the response"
    assert get_post_response.body is not None, "Expected 'body' to be present in the response"
    
def test_get_post_by_id_returns_404_for_nonexistent_id():
    nonexistent_post_id = 10000
    expected_http_status = 404
    url = api_route_builder.build_get_post_by_id_route(nonexistent_post_id)
    
    response = requests.get(url)
    
    assert response.status_code == expected_http_status, f"Expected status code {expected_http_status}, got {response.status_code}"
    
def test_get_post_by_id_returns_404_for_invalid_id():
    invalid_post_id = "invalid"
    expected_http_status = 404
    url = api_route_builder.build_get_post_by_id_route(invalid_post_id)
    
    response = requests.get(url)
    
    assert response.status_code == expected_http_status, f"Expected status code {expected_http_status}, got {response.status_code}"
