# 📧 Email Extractor

## Overview

The **Email Extractor** is a simple Python automation project that reads a text file, extracts all valid email addresses using **Regular Expressions (Regex)**, and saves the extracted emails into a separate text file. This project demonstrates how Python can automate repetitive tasks involving text processing.

## Objective

Read a text file, find all valid email addresses, and save them into another text file.

## Features

* Reads text from an input file.
* Extracts valid email addresses using Regular Expressions (`re` module).
* Saves all extracted email addresses to a new text file.
* Displays the total number of email addresses found.
* Prints the extracted email addresses in the console.

## Technologies Used

* Python 3
* Regular Expressions (`re`)
* File Handling

## Project Structure

```text
Email_Extractor/
│
├── input.txt           # Input file containing text and email addresses
├── emails.txt          # Output file with extracted email addresses
└── main.py  # Python script
```

## How It Works

1. Open and read the contents of `input.txt`.
2. Search for valid email addresses using a regular expression.
3. Store all matched email addresses in a list.
4. Write the extracted email addresses to `emails.txt`.
5. Display the total number of extracted emails in the terminal.

## How to Run

1. Make sure Python 3 is installed.
2. Place your text containing email addresses in `input.txt`.
3. Open a terminal in the project folder.
4. Run the script:

```bash
python email_extractor.py
```

## Example Input (`input.txt`)

```text
Hello!

Contact us at support@gmail.com

Business Email:
business@yahoo.com

Developer:
sayyam.shahid123@gmail.com

Another Email:
python_dev2026@hotmail.com
```

## Example Output (Console)

```text
✅ Email extraction completed!
4 email(s) found.

support@gmail.com
business@yahoo.com
sayyam.shahid123@gmail.com
python_dev2026@hotmail.com
```

## Output File (`emails.txt`)

```text
support@gmail.com
business@yahoo.com
sayyam.shahid123@gmail.com
python_dev2026@hotmail.com
```

## Python Concepts Used

* Regular Expressions (`re`)
* File Handling
* Reading and Writing Files
* Lists
* Loops

## Learning Outcomes

After completing this project, you will be able to:

* Read data from text files.
* Use Regular Expressions to search for patterns.
* Automate text-processing tasks.
* Save processed data into a new file.
* Apply Python file handling in real-world scenarios.

## Future Improvements

* Remove duplicate email addresses.
* Export results to a CSV file.
* Validate email domains.
* Allow users to specify input and output file names.
* Build a simple graphical user interface (GUI).

## License

This project is open-source and available for learning and educational purposes.
