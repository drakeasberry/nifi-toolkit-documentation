import os

def read_help_files(help_files_dir):
    """
    Reads all the help files in the specified directory and returns a sorted list of filenames.
    """
    help_files = [f for f in os.listdir(help_files_dir) if f.endswith('.txt')]
    help_files.sort()  # Sort files alphabetically
    return help_files
