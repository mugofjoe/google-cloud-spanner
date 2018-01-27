SPANNER_CREDENTIALS = 'credentials.json'
SPANNER_INSTANCE = 'darwins-bark-001'
DATABASE_NAME = 'example-db'

def create_database(instance_id, database_id):
    """Creates a database and tables for sample data."""
    from google.cloud import spanner

    # spanner_client = spanner.Client()
    spanner_client = spanner.Client.from_service_account_json(SPANNER_CREDENTIALS)
    instance = spanner_client.instance(instance_id)

    # database = instance.database(database_id)
    
    # database = instance.database(database_id, ddl_statements=[
    #     """CREATE TABLE Singers (
    #         SingerId     INT64 NOT NULL,
    #         FirstName    STRING(1024),
    #         LastName     STRING(1024),
    #         SingerInfo   BYTES(MAX)
    #     ) PRIMARY KEY (SingerId)""",
    #     """CREATE TABLE Albums (
    #         SingerId     INT64 NOT NULL,
    #         AlbumId      INT64 NOT NULL,
    #         AlbumTitle   STRING(MAX)
    #     ) PRIMARY KEY (SingerId, AlbumId),
    #     INTERLEAVE IN PARENT Singers ON DELETE CASCADE"""
    # ])
    ddl_statements=[
        """CREATE TABLE Singers (
            SingerId     INT64 NOT NULL,
            FirstName    STRING(1024),
            LastName     STRING(1024),
            SingerInfo   BYTES(MAX)
        ) PRIMARY KEY (SingerId)""",
        """CREATE TABLE Albums (
            SingerId     INT64 NOT NULL,
            AlbumId      INT64 NOT NULL,
            AlbumTitle   STRING(MAX)
        ) PRIMARY KEY (SingerId, AlbumId),
        INTERLEAVE IN PARENT Singers ON DELETE CASCADE"""
    ]
    operation_id = ""
    operation = instance.update_ddl(ddl_statements, operation_id)

    print('Waiting for operation to complete...')
    operation.result()

    # print('Created database {} on instance {}'.format(
    #     database_id, instance_id))

if __name__ == '__main__':
    create_database(SPANNER_INSTANCE, DATABASE_NAME)