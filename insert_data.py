SPANNER_CREDENTIALS = 'credentials.json'
SPANNER_INSTANCE = 'darwins-bark-001'
DATABASE_NAME = 'example-db'

    def insert_data(instance_id, database_id):
        """Inserts sample data into the given database.

        The database and table must already exist and can be created using
        `create_database`.
        """
        from google.cloud import spanner
        
        # spanner_client = spanner.Client()
        spanner_client = spanner.Client.from_service_account_json(SPANNER_CREDENTIALS)
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)

        with database.batch() as batch:
            batch.insert(
                table='Singers',
                columns=('SingerId', 'FirstName', 'LastName',),
                values=[
                    (1, u'Marc', u'Richards'),
                    (2, u'Catalina', u'Smith'),
                    (3, u'Alice', u'Trentor'),
                    (4, u'Lea', u'Martin'),
                    (5, u'David', u'Lomond')])

            batch.insert(
                table='Albums',
                columns=('SingerId', 'AlbumId', 'AlbumTitle',),
                values=[
                    (1, 1, u'Total Junk'),
                    (1, 2, u'Go, Go, Go'),
                    (2, 1, u'Green'),
                    (2, 2, u'Forever Hold Your Peace'),
                    (2, 3, u'Terrified')])

        print('Inserted data.')

if __name__ == '__main__':
    insert_data(SPANNER_INSTANCE, DATABASE_NAME)