from fastapi import Response

from postgres.connection import PostgresConnection

from router.models import data_models

SQL_SELECT_DATA = """
    select name
    from service.service_table
"""


def map_to_response(db_result):
    result = list()
    for row in db_result:
        result.append(
            data_models.Item(
                name=row[0]
            )
        )
    return result


async def data_get_impl():
    result = PostgresConnection.execute(SQL_SELECT_DATA)
    return map_to_response(result)
