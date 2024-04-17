import redis
import os
import sys
# Connect to Redis
r = redis.StrictRedis(host= sys.argv[0], port=6379, db=0)

def upload_file(file_path, target_file):
    # Read the content of the file
    with open(file_path, 'rb') as f:
        content = f.read()

    # Get the directory and filename
    dirname = os.path.dirname(target_file)
    basename = os.path.basename(target_file)

    # Set the Redis configuration temporarily
    r.config_set('dir', dirname)
    r.config_set('dbfilename', basename)

    # Upload the file content to Redis
    r.set(basename, content)

    # Save the Redis database to disk
    r.save()
    print("successfully saved file: {}".format(target_file))

# Usage example
source_file = sys.argv[1]
target_file = sys.argv[2]

upload_file(source_file, target_file)
