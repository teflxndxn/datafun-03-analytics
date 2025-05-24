def write_project_notes(filename="project_notes.txt"):
    notes = """
    Ebola Data Analytics Project Notes

    - This project fetches Ebola data from an online source.
    - Processes data into long format using Python collections.
    - Saves processed data as CSV, Excel, JSON.
    - Generates plots for analysis.
    - Logs process information in log files.
    """
    with open(filename, "w") as f:
        f.write(notes)
    print(f"Project notes written to {filename}")
if __name__ == "__main__":
    write_project_notes()
