#!/usr/bin/python3
"""
Initialization module for the models package.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
