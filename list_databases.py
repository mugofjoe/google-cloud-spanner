#!/usr/bin/env python

SPANNER_CREDENTIALS = 'credentials.json'
SPANNER_INSTANCE = 'darwins-bark-001'
DATABASE_NAME = 'example-db'

def list_databases():
    # [START list_databases]
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

    # Execute a simple SQL statement.
    for database in instance.list_databases():
        # `database` is a `Database` object.
        print(database.name)


    # [END list_databases]


if __name__ == '__main__':
    list_databases()
