import logging

import subprocess


def run_pgmigrate(pg_credentials):
    result = subprocess.run(
        [
            "pgmigrate",
            "-t",
            "1",
            "migrate",
            "-c",
            f"dbname={pg_credentials['database']} "
            + f"user={pg_credentials['user']} "
            + f"password={pg_credentials['password']} "
            + f"host={pg_credentials['host']} "
            + f"port={pg_credentials['port']}"
        ],
        capture_output=True,
    )
    logging.info(result.stdout)
    if result.returncode:
        logging.error(result.stderr.decode('utf-8'))

    return result.returncode
