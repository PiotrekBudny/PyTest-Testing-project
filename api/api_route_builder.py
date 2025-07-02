import variables

def build_get_post_by_id_route(post_id):    
    return f"{variables.API_BASE_URL}/posts/{post_id}"