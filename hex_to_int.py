#!/usr/bin/env python
"""
Hexadecimal to Integer 
"""

SPANNER_CREDENTIALS = 'credentials.json'
SPANNER_INSTANCE = 'darwins-bark-001'
DATABASE_NAME = 'example-db'

def hex_to_int():
    # [START spanner_quickstart]
    # Imports the Google Cloud Client Library.
    from google.cloud import spanner

    # Instantiate a client.
    #spanner_client = spanner.Client()

    spanner_client = spanner.Client.from_service_account_json(
    SPANNER_CREDENTIALS)
    instance_id = SPANNER_INSTANCE

    instance = spanner_client.instance(instance_id)
    database_id = DATABASE_NAME
    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            """
            SELECT '0x123' as hex_value, CAST('0x123' as INT64) as hex_to_int;
            """)

        for row in results:
            print(row)



if __name__ == '__main__':
    hex_to_int()
