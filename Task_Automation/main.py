# TASK 3: Task Automation with Python Scripts
# Goal: Automate a small, real-life repetitive task.
# Pick One of These Ideas:
# ● Move all .jpg files from a folder to a new folder.
# ● Extract all email addresses from a .txt file and save them to another file.
# ● Scrape the title of a fixed webpage and save it.
# Key Concepts Used: os, shutil, re, requests, file handling

import re

# read data from input file
with open("input.txt","r") as f:
    text = f.read()
    
# Regular Expression to find email addresses
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)

# save emails into emails.txt file
with open("emails.txt", "w") as f:
    f.write("These Emails are Founded! \n\n")
    for email in emails:
        f.write(email + "\n") 
        
print("✅ Email extraction completed!")
print(f"{len(emails)} email(s) found.")

print("\nExtracted Emails:")
for email in emails:
    print(email)