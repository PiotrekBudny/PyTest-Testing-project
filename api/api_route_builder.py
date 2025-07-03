import api_variables

def build_get_post_by_id_route(post_id):    
    return f"{api_variables.API_BASE_URL}/posts/{post_id}"

def build_get_all_posts_route():
    return f"{api_variables.API_BASE_URL}/posts"

def build_create_post_route():
    return f"{api_variables.API_BASE_URL}/posts"

def build_update_post_route(post_id):
    return f"{api_variables.API_BASE_URL}/posts/{post_id}"