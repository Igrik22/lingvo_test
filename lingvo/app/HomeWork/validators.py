from src.settings import MAX_UPLOAD_SIZE


def validate_file_size(temp_file):
    if temp_file.size > MAX_UPLOAD_SIZE:
        raise ValueError('File\'s size more then 2 mb')
    return True
