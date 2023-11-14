<<<<<<< HEAD
from os import path, remove


class Events:
    def __init__(self, date, name, time, location, importance=0):
        self.date = date
        self.name = name
        self.time = time
        self.location = location
        self.importance = importance
        self.file = "events.txt"
        if not path.exists(self.file):
            with open(self.file, "w") as file:
                file.write("")

    importance_dict = {
        0: {"description": "low", "icon": "."},
        1: {"description": "medium", "icon": "*"},
        2: {"description": "high", "icon": "!"},
        3: {"description": "critical", "icon": "!!"},
    }

    def __str__(self):
        return f'- {self.name}: {self.date} at {self.time} in {self.location} ({self.importance_dict[self.importance]["description"]})'

    def store(self):
        with open(self.file, "a") as file:
            file.write(
                f"{self.date} {self.name} {self.time} {self.location} {self.importance}\n"
            )

    @staticmethod
    def erase(filename, line_number):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return

        try:
            del lines[line_number - 1]
        except IndexError:
            print(f"Line {line_number} not found.")
            return

        with open(filename, "w") as file:
            file.writelines(lines)

    @classmethod
    def from_file(cls, file):
        events = []
        try:
            with open(file, "r") as file:
                lines = file.readlines()
            for line in lines:
                line = line.split()
                # print(line)
                events.append(cls(line[0], line[1], line[2], line[3], int(line[4])))
        except FileNotFoundError:
            print("File not found. Creating a new one...")
            with open(file, "w") as file:
                file.write("")
        finally:
            return events

    def del_file(self):
        with open(self.file, "r") as file_test:
            if file_test.read() == "":
                file_test.close()
                remove(self.file)


def test():
    test = Events("2020-12-25", "Christmas", "12:00", "home", 2)
    test.store()
    print(test)

    # input('Press enter to erase the event')

    reading_test = Events.from_file(test.file)
    for event in reading_test:
        print(event)

    # test.erase(test.file, 1)
    # test.del_file()


if __name__ == "__main__":
    test()
=======
from os import path, remove


class Events:
    def __init__(self, date, name, time, location, importance=0):
        self.date = date
        self.name = name
        self.time = time
        self.location = location
        self.importance = importance
        self.file = "events.txt"
        if not path.exists(self.file):
            with open(self.file, "w") as file:
                file.write("")

    importance_dict = {
        0: {"description": "low", "icon": "."},
        1: {"description": "medium", "icon": "*"},
        2: {"description": "high", "icon": "!"},
        3: {"description": "critical", "icon": "!!"},
    }

    def __str__(self):
        return f'- {self.name}: {self.date} at {self.time} in {self.location} ({self.importance_dict[self.importance]["description"]})'

    def store(self):
        with open(self.file, "a") as file:
            file.write(
                f"{self.date} {self.name} {self.time} {self.location} {self.importance}\n"
            )

    @staticmethod
    def erase(filename, line_number):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return

        try:
            del lines[line_number - 1]
        except IndexError:
            print(f"Line {line_number} not found.")
            return

        with open(filename, "w") as file:
            file.writelines(lines)

    @classmethod
    def from_file(cls, file):
        events = []
        try:
            with open(file, "r") as file:
                lines = file.readlines()
            for line in lines:
                line = line.split()
                # print(line)
                events.append(cls(line[0], line[1], line[2], line[3], int(line[4])))
        except FileNotFoundError:
            print("File not found. Creating a new one...")
            with open(file, "w") as file:
                file.write("")
        finally:
            return events

    def del_file(self):
        with open(self.file, "r") as file_test:
            if file_test.read() == "":
                file_test.close()
                remove(self.file)


def test():
    test = Events("2020-12-25", "Christmas", "12:00", "home", 2)
    test.store()
    print(test)

    # input('Press enter to erase the event')

    reading_test = Events.from_file(test.file)
    for event in reading_test:
        print(event)

    # test.erase(test.file, 1)
    # test.del_file()


if __name__ == "__main__":
    test()
>>>>>>> 7b0acce (adding readme, removing sensitive information and adding arduino sketch)
