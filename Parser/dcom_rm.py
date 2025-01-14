import argparse
from pathlib import Path


def single_line_comment_start(line):
    if "//" in line:
        return True

def multi_line_comment_start(line):
    if "/*" in line:
        return True

def multi_line_comment_end(line):
    if "*/" in line:
        return True

def is_dated_comment(line):
    def contain_full_date(subline):
        """Test if a subline contains a full date"""
        # Subline is too short to contain a full date
        if len(subline) < 10:
            return False

        # Pattern match DD/MM/YYYY
        if subline[0].isdigit() and subline[1].isdigit() and subline[2] == "/" and \
            subline[3].isdigit() and subline[4].isdigit() and subline[5] == "/" and \
            subline[6].isdigit() and subline[7].isdigit() and subline[8].isdigit() and subline[9].isdigit():
           return True

        return False

    # Multi line comment can contain single line comment, must process multi line comment first.
    i = line.find("/*")
    if i < 0:
        i = line.find("//")

    i += 2  # Skip the comment characters

    # Find full date by looking for the first number in full date
    while i < len(line):
        if line[i].isdigit() and contain_full_date(line[i:]):
            return True
        i += 1

    return False

def parse_lines(lines):
    processed_lines = []

    in_multi_line_comment = False  # Flag to track if we are inside a multi line comment
    should_remove = False  # Flag to track if this multi line comment shall be removed
    for line in lines:
        # A line cannot be multi line and single line comment
        # Multi line comment has higher priority
        if not in_multi_line_comment and multi_line_comment_start(line):
            in_multi_line_comment = True
            if is_dated_comment(line):
                should_remove = True
        elif not in_multi_line_comment and single_line_comment_start(line):
            if is_dated_comment(line):
                continue

        # Keep regular lines and regular comments
        if not in_multi_line_comment or (in_multi_line_comment and not should_remove):
            # print(line)
            processed_lines.append(line)

        if multi_line_comment_end(line):
            in_multi_line_comment = False
            should_remove = False

    return processed_lines

def read_lines_from_file(file_path):
    """Read lines from a given file and return them as a list."""
    try:
        with file_path.open("r") as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def save_lines_to_file(lines, file_path):
    with open(file_path, "w") as output_file:
        output_file.writelines(lines)  # Write Hello, World! to the file

def main(args):
    lines = read_lines_from_file(args.input_file)
    processed_lines = parse_lines(lines)
    save_lines_to_file(processed_lines, args.output_file)

if __name__ == "__main__":
    # Usage:
    # `python dcom_rm.py inputC.cpp inputC_rm.cpp`
    #
    # Does NOT support the following special cases:
    # - Comment characters in string literals
    #   E.g. `"// not a valid comment"`
    # - Comments inline with code
    #   E.g. `return 0; // 01/01/2024`

    parser = argparse.ArgumentParser(description="Remove dated comments in a C++ source file.")
    parser.add_argument("input_file", type=Path, help="The input C++ file to read from (e.g., inputC.cpp)")
    parser.add_argument("output_file", type=Path, help="The output file to save to (e.g., inputC_rm.cpp)")

    args = parser.parse_args()
    main(args)
