#!/usr/bin/env python

SPANNER_CREDENTIALS = 'credentials.json'
SPANNER_INSTANCE = 'darwins-bark-001'
DATABASE_NAME = 'example-db'

def run_quickstart():
    # [START spanner_quickstart]
    # Imports the Google Cloud Client Library.
    from google.cloud import spanner

    # Instantiate a client.
    #spanner_client = spanner.Client()

    spanner_client = spanner.Client.from_service_account_json(
    SPANNER_CREDENTIALS)

    # Your Cloud Spanner instance ID.
    instance_id = SPANNER_INSTANCE

    # Get a Cloud Spanner instance by ID.
    instance = spanner_client.instance(instance_id)

    # Your Cloud Spanner database ID.
    database_id = DATABASE_NAME

    # Get a Cloud Spanner database by ID.
    database = instance.database(database_id)

    # Execute a simple SQL statement.
    with database.snapshot() as snapshot:
        # results = snapshot.execute_sql('SELECT * FROM Singers')
        results = snapshot.execute_sql(
            """
            SELECT '0x123' as hex_value, CAST('0x123' as INT64) as hex_to_int;
            """)

        for row in results:
            print(row)
    # [END spanner_quickstart]


if __name__ == '__main__':
    run_quickstart()
