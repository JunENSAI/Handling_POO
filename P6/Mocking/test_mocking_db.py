import pytest
from unittest.mock import MagicMock, patch

def get_user_name(db_connection, user_id):
    cursor = db_connection.cursor()
    query = "SELECT username FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone() 
    return result[0] if result else None

def test_get_user_name_success():

    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_conn.cursor.return_value = mock_cursor

    mock_cursor.fetchone.return_value = ("SuperAlice",)

    result = get_user_name(mock_conn, 99)

    assert result == "SuperAlice"

    mock_cursor.execute.assert_called_once()

def test_get_user_not_found():

    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_conn.cursor.return_value = mock_cursor

    mock_cursor.fetchone.return_value = None

    result = get_user_name(mock_conn, 999)

    assert result == None



