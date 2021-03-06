import os
from django.core.exceptions import ValidationError
from rest_framework import serializers

MAX_FILE_SIZE = 1024000
ALLOWED_EXTENSIONS = ['.jpg', '.png', '.img']


def validate_file_size(value):
    if value.size > MAX_FILE_SIZE:
        raise ValidationError(f'Max file size is: {MAX_FILE_SIZE}')


def validate_extension(value):
    split_ext = os.path.splitext(value.name)
    if len(split_ext) > 1:
        ext = split_ext[1]
        if not ext.lower() in ALLOWED_EXTENSIONS:
            raise ValidationError(f'This is not allowed file, valid extensions: {ALLOWED_EXTENSIONS}')


def validate_name(self, value):
    if '/' in value:
        raise serializers.ValidationError('Invalid char in name field')
    return value
