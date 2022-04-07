#!/usr/bin/env python3

# Created by Devin Jhu
# Created on April 2022
# Is it a leap year


def main():
    # this function tells you if its a leap year.

    print("Is it a leap year")

    # input
    year_string = input("Enter your year: ")

    # process
    try:
        year_number = int(year_string)

        if year_number % 4 == 0:
            if year_number % 100 == 0:
                if year_number % 400 == 0:
                    print("Year {0} is a leap year.".format(year_number))
                else:
                    print("Year {0} is not a leap year.".format(year_number))
            else:
                print("Year {0} is a leap year.".format(year_number))
        else:
            print("Year {0} is not a leap year.".format(year_number))
    except Exception:
        print("Not a year")
    print("\nDone.")


if __name__ == "__main__":
    main()
