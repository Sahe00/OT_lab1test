def main():
    print("Hello from the main branch!")
    first_feature()
    second_feature()


if __name__ == "__main__":
    main()


# Pytest cannot find the correct file to run,
# because there is not "test_" prefix in the file name.