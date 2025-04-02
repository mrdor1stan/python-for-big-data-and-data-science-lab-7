import pandas


def read_from_console():
    """Reads text from the console.

       Returns:
           str: The user-entered text.
       """
    return input()


def read_from_file_builtin(file_path):
    """Reads a text file using Python's built-in functionality.

       Args:
           file_path (str): The path to the file.

       Returns:
           str: The content of the file as a string.
       """
    result = ""
    with open(file_path) as file:
        for line in file:
            result += line
    return result


def read_from_csv_file_pandas(file_path):
    """Reads a file using the pandas library.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            str: The file content as a string.
        """
    return pandas.read_csv(file_path).to_string()
