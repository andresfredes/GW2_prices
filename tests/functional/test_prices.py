def test_index(test_client):
    with test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        # inherited from base.html
        assert b'Guild Wars 2 - Recipes & Pricing' in response.data
        # content from index.html
        assert b'Content placeholder - searchbar etc' in response.data