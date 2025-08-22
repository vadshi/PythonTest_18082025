import pytest
from httpx import AsyncClient, ASGITransport


from app.database import Item
from app.main import app

@pytest.mark.asyncio
async def test_read_main():
    client = AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    )
    response = await client.get("/home")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}

    await client.aclose()


def test_read_main_client(test_client):
    response = test_client.get("/home")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}

def test_client_can_add_read_item(test_client, test_db_session):
    response = test_client.get("/item/1")
    assert response.status_code == 404

    response = test_client.post("/item", json={"name": "ball", "color": "red"})
    assert response.status_code == 201

    # Verify that item was added to the database
    item_id = response.json()
    item_db = (
        test_db_session.query(Item)
        .filter(Item.id == item_id)
        .first()
    )
    assert item_db is not None

    response = test_client.get("/item/1")
    assert response.status_code == 200
    assert response.json() == {"name": "ball", "color": "red"}