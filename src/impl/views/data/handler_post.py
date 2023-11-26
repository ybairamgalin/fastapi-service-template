from fastapi import Response

from postgres.connection import PostgresConnection


SQL_INSERT_NAME = """
    insert into service.service_table (name)
    values
        (%s)
    on conflict (id) do nothing
"""


async def data_post_impl(name):
    PostgresConnection.execute_no_return(SQL_INSERT_NAME, (name,))
    return Response(status_code=201)
