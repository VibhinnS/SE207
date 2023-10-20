def count_lines_of_code(file_path):
    code_lines = 0

    with open(file_path, 'r') as file:
        inside_comment = False

        for line in file:
            line = line.strip()

            if not inside_comment:
                if line.startswith("/*"):
                    inside_comment = True
                    if line.endswith("*/"):
                        inside_comment = False
                elif line.startswith("//"):
                    continue
                elif not line:
                    continue
                else:
                    code_lines += 1
            elif inside_comment and line.endswith("*/"):
                inside_comment = False

    return code_lines

if __name__ == "__main__":
    file_path = "C:/Users/Vibhinn Singhal/SE207/exp6.py"
    lines_of_code = count_lines_of_code(file_path)
    print()
    print(f"Lines of code (excluding comments and blanks): {lines_of_code}")
    print()
