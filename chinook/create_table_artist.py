SPANNER_CREDENTIALS = 'credentials.json'
SPANNER_INSTANCE = 'darwins-bark-001'
DATABASE_NAME = 'example-db'

def create_table(instance_id, database_id):
    """Creates tables."""
    from google.cloud import spanner
    spanner_client = spanner.Client.from_service_account_json(SPANNER_CREDENTIALS)
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    ddl_statements=[
        """
        CREATE TABLE Artist
        (
            ArtistId INTEGER  NOT NULL,
            Name NVARCHAR(120),
            CONSTRAINT PK_Artist PRIMARY KEY ArtistId
        )
        """
    ]
    operation_id = ""
    operation = database.update_ddl(ddl_statements)

    print('Waiting for operation to complete...')
    operation.result()

if __name__ == '__main__':
    create_table(SPANNER_INSTANCE, DATABASE_NAME)