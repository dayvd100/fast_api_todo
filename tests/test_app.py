from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testemeuuser',
            'email': 'teste@teste.com',
            'password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        'username': 'testemeuuser',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'testemeuuser',
                'email': 'teste@teste.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': '123',
            'id': 1,
            'username': 'Dayvao',
            'email': 'Dayvao@gmail.com',
        },
    )

    assert response.json() == {
        'id': 1,
        'username': 'Dayvao',
        'email': 'Dayvao@gmail.com',
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'user deleted'}


def test_error_delete_user(client):
    response = client.delete('/users/10')
    assert response.json() == {'detail': 'USER NOT FOUND'}
