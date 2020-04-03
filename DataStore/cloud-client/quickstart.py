def run_quickstart():
    # [START datastore_quickstart]
    # Imports the Google Cloud client library
    from google.cloud import ndb

    # Instantiates a client
    datastore_client = ndb.Client()

    # The kind for the new entity
    kind = 'Task'
    # The name/ID for the new entity
    name = 'sampletask2'
    # The Cloud Datastore key for the new entity
    task_key = datastore_client.key(kind, name)

    # Prepares the new entity
    task = ndb.Entity(key=task_key)
    task['description'] = 'NGuyen Van Dat'

    # Saves the entity
    datastore_client.put(task)

    print('Saved {}: {}'.format(task.key.name, task['description']))
    # [END datastore_quickstart]


if __name__ == '__main__':
    run_quickstart()
