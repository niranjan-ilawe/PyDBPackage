from datetime import datetime, timedelta
import time, os


def return_new_files(file_list, day_interval=1):
    """OBSOLETED
    Return files that have been updated in the last specified days

    Parameters:
        file_list (list): List of files with full path
        day_interval (int): day interval in which files are needed

    Returns:
        file_list (list): List of filtered files
    """

    files_sent = len(file_list)
    print(f"Total number of files recieved by function {files_sent}")

    # Skip files older than specified days
    now_minus_one_day = datetime.today() - timedelta(days=day_interval)
    now_minus_one_day = now_minus_one_day.strftime("%Y-%m-%d %H:%M:%S")
    new_files = []

    for file in file_list:
        modification_time = os.path.getmtime(file)
        modification_time = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(modification_time)
        )
        if modification_time > now_minus_one_day:
            new_files.append(file)

    total_no_files = len(new_files)
    print(f"Files modified in the last {day_interval} day(s) .. {total_no_files}")
    return new_files
