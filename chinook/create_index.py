SPANNER_CREDENTIALS = 'credentials.json'
SPANNER_INSTANCE = 'darwins-bark-001'
DATABASE_NAME = 'fohn'

def create_index(instance_id, database_id):
    """Creates index."""
    from google.cloud import spanner
    spanner_client = spanner.Client.from_service_account_json(SPANNER_CREDENTIALS)
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    ddl_statements=[
        """
        CREATE INDEX IFK_AlbumArtistId ON Album(ArtistId)
        """
    ]
    operation_id = ""
    operation = database.update_ddl(ddl_statements)

    print('Waiting for operation to complete...')
    operation.result()

if __name__ == '__main__':
    create_index(SPANNER_INSTANCE, DATABASE_NAME)