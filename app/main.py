def copy_file(command: str) -> None:
    parts = command.split()
    file_name = parts[1]
    new_file_name = parts[2]

    if file_name == new_file_name:
        return

    with open(file_name, "r") as file_in, open(new_file_name, "w") as file_out:
        file_out.write(file_in.read())
# write your code here
