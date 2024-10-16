import sys

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        return None

def parse_log_line(line: str) -> dict:
    parse = line.split()
    result_dict = {
        "date": parse[0],
        "time": parse[1],
        "level": parse[2],
        "message": " ".join(parse[3:])
    }
    return result_dict

def count_logs_by_level(logs: list) -> dict:
    count_log = {"INFO": 0, "DEBUG": 0, "ERROR": 0, "WARNING": 0}
    for log in logs:
        if log["level"] in count_log:
            count_log[log["level"]] += 1
    return count_log

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count:^10}")


def main():
    if len(sys.argv) < 2:
        print("Вкажіть шлях до файлу.")
        return

    file_path = sys.argv[1]
    if len(sys.argv) > 2:
        level = sys.argv[2]
    else:
        level = None

    lines = load_logs(file_path)

    logs = []
    try:
        for line in lines:
            logs.append(parse_log_line(line))
    except TypeError:
        return "Error"
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

if __name__ == "__main__":
    main()