#!/usr/bin/env python
from google.cloud import spanner

SPANNER_CREDENTIALS = 'credentials.json'
SPANNER_INSTANCE = 'darwins-bark-001'
DATABASE_NAME = 'fohn'

def create_database(instance_id, database_id):
    spanner_client = spanner.Client.from_service_account_json(SPANNER_CREDENTIALS)
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id, ddl_statements=[
        """
        CREATE TABLE Artist (
            ArtistId INT64 NOT NULL,
            Name     STRING(120),
        ) PRIMARY KEY (ArtistId)
        """,
        """
        CREATE TABLE Album (
            ArtistId INT64 NOT NULL,
            AlbumId  INT64 NOT NULL,
            Title    STRING(MAX)
        ) PRIMARY KEY (ArtistId, AlbumId),
        INTERLEAVE IN PARENT Artist ON DELETE CASCADE
        """
    ])

    operation = database.create()
    print('Waiting for operation to complete...')
    operation.result()

    print('Created database {} on instance {}'.format(
        database_id, instance_id))


if __name__ == '__main__':
    create_database(SPANNER_INSTANCE, DATABASE_NAME)