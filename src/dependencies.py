import postgres


def init_dependencies():
    postgres.PostgresConnection.open_connection()
