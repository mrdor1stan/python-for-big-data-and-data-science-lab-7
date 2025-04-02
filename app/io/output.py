def write_to_console(data):
    """Prints text to the console.

        Args:
            data (str): The text to write.

        Returns:
            None.
        """
    print(data)


def write_to_file_builtin(file_path, data):
    """Writes text to a file using Python's built-in functionality.

        Args:
            file_path (str): The path to the file.
            data (str): The text to write.

        Returns:
            None.
        """
    f = open(file_path, "a")
    f.write(data)
    f.close()

