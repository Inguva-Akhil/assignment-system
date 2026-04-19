from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_submit():
    client = app.test_client()
    response = client.post('/submit', json={
        "name": "Akhil",
        "assignment": "DBMS"
    })
    assert response.status_code == 200