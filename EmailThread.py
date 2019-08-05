def main():
    givenString = "Feedback hello this is feedback"
    resultStr = givenString.split('Feedback', 1)[1]
    print(resultStr)

if __name__ == "__main__":
    main()