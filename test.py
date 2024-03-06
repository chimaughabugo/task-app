from app import app

def test1():
    response = app.test_client().get('/')
    assert response.status_code == 200, f"code not found"
    
def test2():
    response = app.test_client().get('/edit')
    assert response.status_code == 200
    
def test3():
    response = app.test_client().get('/edit')
    assert b"To Do App" in response.data