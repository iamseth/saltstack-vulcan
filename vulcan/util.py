import os
import hashlib

def hashfile(path):
    '''Get the SHA1 digest for a file.
    '''
    hasher = hashlib.sha1()
    with open(path, 'rb') as fp:
        while True:
            blocksize = 64 * 1024
            data = fp.read(blocksize)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def hashdir(path, file_excludes=None):
    '''Determine a SHA1 digest for an entire directory tree.
    '''

    if not file_excludes:
        file_excludes = []
    file_list = []
    for root, _, files in os.walk(path):
        for f in files:
            if not f in file_excludes:
                file_list.append(os.path.join(root, f))

    file_hashes = [hashfile(f) for f in sorted(file_list)]
    hasher = hashlib.sha1()
    for file_hash in file_hashes:
        hasher.update(file_hash.encode('utf-8'))
    return hasher.hexdigest()
