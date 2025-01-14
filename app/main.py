from datetime import datetime  # DO NOT CHANGE THIS IMPORT\
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        file_name = f"app-{time.hour}_{time.minute}_{time.second}.log"
        with open(file_name, "w") as f:
            f.write(str(datetime.now()))
            print(f"{time} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
