SPANNER_CREDENTIALS = 'credentials.json'
SPANNER_INSTANCE = 'darwins-bark-001'
DATABASE_NAME = 'example-db'

def drop_tables(instance_id, database_id):
    """Drop tables"""
    from google.cloud import spanner
    spanner_client = spanner.Client.from_service_account_json(SPANNER_CREDENTIALS)
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    ddl_statements=[
        """DROP TABLE Album""",
        """DROP TABLE Artist"""]
    operation_id = ""
    operation = database.update_ddl(ddl_statements)

    print('Waiting for operation to complete...')
    operation.result()

if __name__ == '__main__':
    drop_tables(SPANNER_INSTANCE, DATABASE_NAME)