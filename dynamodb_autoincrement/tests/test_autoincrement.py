from .. import DynamoDBAutoIncrement


N = 20


def test_dangerously_handles_many_serial_puts(dynamodb, create_tables):
    autoincrement = DynamoDBAutoIncrement(
        counter_table_name="autoincrement",
        counter_table_key={"tableName": "widgets"},
        table_name="widgets",
        attribute_name="widgetID",
        initial_value=1,
        dynamodb=dynamodb,
    )
    ids = list(range(1, N + 1))
    results = [autoincrement.put({"widgetName": id}) for id in ids]
    assert sorted(results) == ids
