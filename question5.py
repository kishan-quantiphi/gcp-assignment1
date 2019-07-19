from google.cloud import storage
import logging
# setting logging config
logging.basicConfig(filename="question5.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
logger=logging.getLogger()
logger.setLevel(logging.ERROR) 

# Instantiates a client
storage_client = storage.Client()

# uploads the object
def upload_object(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    try:
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print('File {} uploaded to {}.'.format(
            source_file_name,
            destination_blob_name))
    except Exception as e:
        logger.error(e)
        print("Error occured! please check your code")


def create_bucket(bucket_name):
    # Creates the new bucket
    try:
        bucket = storage_client.create_bucket(bucket_name)
        print('Bucket {} created.'.format(bucket.name))
    except Exception as e:
        logger.error(e)
        print("Error occured! please debug your code")


def copy_blob(bucket_name, blob_name, new_bucket_name, new_blob_name):
    """Copies a blob from one bucket to another with a new name."""
    try:
        source_bucket = storage_client.get_bucket(bucket_name)
        source_blob = source_bucket.blob(blob_name)
        destination_bucket = storage_client.get_bucket(new_bucket_name)

        new_blob = source_bucket.copy_blob(
            source_blob, destination_bucket, new_blob_name)

        print('Blob {} in bucket {} copied to blob {} in bucket {}.'.format(
            source_blob.name, source_bucket.name, new_blob.name,
            destination_bucket.name))
    except Exception as e:
        logger.error(e)
        print("Error occured! please debug your code")


def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.delete()

        print('Blob {} deleted.'.format(blob_name))
    except Exception as e:
        logger.error(e)
        print("Error occured! please debug your code")


def move_object(bucket1,bucket2,object_name):

    copy_blob(bucket1,object_name,bucket2,object_name)
    delete_blob(bucket1,object_name)
    print('object moved ')

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(source_blob_name)

        blob.download_to_filename(destination_file_name)

        print('Blob {} downloaded to {}.'.format(
            source_blob_name,
            destination_file_name))
    except Exception as e:
        logger.error(e)
        print("Error occured! please debug your code")


bucket_name1='kishan-bucket1'
# bucket_name2='kishan-bucket2'
# create_bucket(bucket_name1)
# create_bucket(bucket_name2)
# upload_object(bucket_name1,'asd.png','asd.png')
# move_object(bucket_name1,bucket_name2,'asd.png')
# copy_blob(bucket_name2,'asd.png',bucket_name1,'asd.png')
download_blob(bucket_name1,'asd.png','/home/kishan/Desktop/asd1.png')