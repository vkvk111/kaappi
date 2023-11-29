def main():
    filename = input("Enter a filename:\n")
    limit = int(input("How many minutes is the bus route supposed to take?\n"))
    a = 0.0
    d = 0.0
    e = 0.0
    c = 0

    try:
        file = open(filename, 'r')
        total = 0
        count = 0

        for line in file:
            line = line.rstrip()
            minutes = int(line)
            total += minutes
            count += 1
            ero = minutes - limit

            if ero > 10:
                a += 1
            elif ero < 3:
                d += 1
            else:
                e += 1

        if count > 0:  # Check if there are valid records in the file.
            x = round((e / count) * 100)
            y = round((a / count) * 100)
            print(f"{e} were max 10 minutes late, which is {x:.1f}%.")
            print(f"{a} were more than 10 minutes late, which is {y:.1f}%.")
            print(f"The file contained {count} times")
        else:
            print("No valid records in the file.")

    except OSError:
        print(f"Error in reading file {filename}. Closing program.")

if __name__ == "__main__":
    main()