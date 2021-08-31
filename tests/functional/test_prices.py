def test_response(test_client):
    with test_client:
        response = test_client.get('/')
        assert response.status_code == 200

def test_inheritence(test_client):
        response = test_client.get('/')
        # inherited from base.html
        assert b'Guild Wars 2 - Recipes & Pricing' in response.data
        # content from index.html
        assert b'Content placeholder - searchbar etc' in response.data