import sys
import csv


def main():
    cmd_arguments = sys.argv

    if len(cmd_arguments) != 3:
        sys.exit(
            "Invalid number of arguments. Provide: input.csv and the name of output.csv"
        )
    if not cmd_arguments[1].endswith(".csv") or not cmd_arguments[2].endswith(".csv"):
        sys.exit("Invalid data type. CSV required")

    with open(cmd_arguments[1], "r") as input_file, open(
        cmd_arguments[2], "w", newline=""
    ) as output_file:
        input_file_reader = csv.DictReader(input_file)

        fieldnames = ["first", "last", "house"]
        output_file_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        output_file_writer.writeheader()

        for row in input_file_reader:
            last, first = row["name"].split(",", maxsplit=1)
            output_file_writer.writerow(
                {"first": first.strip(), "last": last.strip(), "house": row["house"]}
            )


if __name__ == "__main__":
    main()
