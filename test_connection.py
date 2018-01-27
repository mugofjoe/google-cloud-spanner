from google.cloud import storage

# Explicitly use service account credentials by specifying the private key
# file.
storage_client = storage.Client.from_service_account_json(
    'credentials.json')

# Make an authenticated API request
buckets = list(storage_client.list_buckets())
print(buckets)