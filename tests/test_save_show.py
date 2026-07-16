from unittest.mock import MagicMock, patch

import saveShow


def test_insert_user_executes_parameterized_sql():
    cursor = MagicMock()
    cursor.rowcount = 1

    rowcount = saveShow.insert_user(
        cursor, "Ada", "Lovelace", "555-0100", "000-00-0001"
    )

    assert rowcount == 1
    cursor.execute.assert_called_once()
    sql, values = cursor.execute.call_args[0]
    assert "INSERT INTO user_tb" in sql
    assert "%s" in sql
    assert values == ("Ada", "Lovelace", "555-0100", "000-00-0001")


def test_fetch_users_by_first_name():
    cursor = MagicMock()
    expected = [("Ada", "Lovelace", "555-0100", "000-00-0001")]
    cursor.fetchall.return_value = expected

    result = saveShow.fetch_users_by_first_name(cursor, "Ada")

    assert result == expected
    cursor.execute.assert_called_once()
    sql, params = cursor.execute.call_args[0]
    assert "first_name" in sql
    assert params == ("Ada",)


def test_connect_passes_kwargs():
    with patch("saveShow.mysql.connector.connect") as mock_connect:
        mock_connect.return_value = MagicMock()
        saveShow.connect("127.0.0.1", "root", "root", "myusers")

    mock_connect.assert_called_once_with(
        host="127.0.0.1",
        user="root",
        password="root",
        database="myusers",
    )


def test_main_happy_path():
    mock_cursor = MagicMock()
    mock_cursor.rowcount = 1
    mock_cursor.fetchall.return_value = [
        ("Ada", "Lovelace", "555-0100", "000-00-0001")
    ]
    mock_db = MagicMock()
    mock_db.cursor.return_value = mock_cursor

    inputs = iter(["Ada", "Lovelace", "555-0100", "000-00-0001"])

    with (
        patch("saveShow.input", side_effect=lambda _: next(inputs)),
        patch("saveShow.connect", return_value=mock_db) as mock_connect,
        patch("saveShow.pp.pprint") as mock_pprint,
        patch.dict(
            "os.environ",
            {
                "MYSQL_HOST": "db.example",
                "MYSQL_USER": "demo",
                "MYSQL_PASSWORD": "secret",
                "MYSQL_DATABASE": "myusers",
            },
            clear=False,
        ),
    ):
        saveShow.main()

    mock_connect.assert_called_once_with(
        "db.example", "demo", "secret", "myusers"
    )
    mock_db.commit.assert_called_once()
    mock_cursor.close.assert_called_once()
    mock_db.close.assert_called_once()
    mock_pprint.assert_called_once_with(
        [("Ada", "Lovelace", "555-0100", "000-00-0001")]
    )

    # insert then select
    assert mock_cursor.execute.call_count == 2
    insert_sql, insert_vals = mock_cursor.execute.call_args_list[0][0]
    assert "INSERT" in insert_sql
    assert insert_vals == ("Ada", "Lovelace", "555-0100", "000-00-0001")
    select_sql, select_params = mock_cursor.execute.call_args_list[1][0]
    assert "SELECT" in select_sql.upper()
    assert select_params == ("Ada",)
