from models.post_response import PostResponse

class ApiAssertions:
    def __init__(self, response):
        self.response = response
    
    def assert_status_code(self, expected_status_code):
        assert self.response.status_code == expected_status_code, (
            f"Expected status code {expected_status_code}, got {self.response.status_code}"
        )
    
    def assert_post_response(self, expected_post_id):
        json_response = self.response.json()
        get_post_response = PostResponse(**json_response)
        
        assert get_post_response.id == expected_post_id, f"Expected post ID {expected_post_id}, got {json_response.get('id')}"
        assert get_post_response.userId == 1, "Expected 'userId' to be present in the response and equal to 1"
        assert get_post_response.title is not None, "Expected 'title' to be present in the response"
        assert get_post_response.body is not None, "Expected 'body' to be present in the response"
        
    def assert_get_all_posts_response(self, expected_number_of_posts):
        json_response = self.response.json()
        actual_number_of_posts = len(json_response)
        
        assert isinstance(json_response, list), "Expected response to be a list of posts"
        assert actual_number_of_posts == expected_number_of_posts, (
            f"Expected {expected_number_of_posts} posts, got {actual_number_of_posts}"
        )
    
    def assert_create_post_response(self, create_post_request):
        response_json = self.response.json()
        create_post_response = PostResponse(**response_json)
        
        assert create_post_response.userId == create_post_request.userId, (
            "Expected 'userId' in response to match request"
        )
        assert create_post_response.title == create_post_request.title, (
            "Expected 'title' in response to match request"
        )
        assert create_post_response.body == create_post_request.body, (
            "Expected 'body' in response to match request"
        )
        assert create_post_response.id is not None, "Expected 'id' to be present in the response"
        
        