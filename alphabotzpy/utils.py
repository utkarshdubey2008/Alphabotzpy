def chunked_file_reader(file_path, chunk_size=1024 * 1024 * 5):  # 5 MB chunks
    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            yield chunk
