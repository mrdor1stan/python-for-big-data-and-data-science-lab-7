from app.io import input
from app.io import output


def main():
    output.write_to_console(input.read_from_console())
    output.write_to_console(input.read_from_file_builtin("data/lorem.txt"))
    output.write_to_file_builtin("data/data_output.txt", input.read_from_csv_file_pandas("data/example.csv"))


if __name__ == "__main__":
    main()
