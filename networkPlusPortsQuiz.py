import random

# List of port questions
questions = [
    {"port": 20, "protocol": "FTP (Data)", "description": "File Transfer Protocol - Data Channel"},
    {"port": 21, "protocol": "FTP (Control)", "description": "File Transfer Protocol - Control Channel"},
    {"port": 22, "protocol": "SSH", "description": "Secure Shell for remote access"},
    {"port": 23, "protocol": "Telnet", "description": "Unsecured remote login"},
    {"port": 25, "protocol": "SMTP", "description": "Simple Mail Transfer Protocol"},
    {"port": 53, "protocol": "DNS", "description": "Domain Name System"},
    {"port": 67, "protocol": "DHCP (Server)", "description": "Dynamic Host Configuration Protocol - Server"},
    {"port": 68, "protocol": "DHCP (Client)", "description": "Dynamic Host Configuration Protocol - Client"},
    {"port": 69, "protocol": "TFTP", "description": "Trivial File Transfer Protocol"},
    {"port": 80, "protocol": "HTTP", "description": "HyperText Transfer Protocol"},
    {"port": 110, "protocol": "POP3", "description": "Post Office Protocol v3"},
    {"port": 143, "protocol": "IMAP", "description": "Internet Message Access Protocol"},
    {"port": 161, "protocol": "SNMP", "description": "Simple Network Management Protocol"},
    {"port": 162, "protocol": "SNMP Trap", "description": "SNMP Trap messages"},
    {"port": 443, "protocol": "HTTPS", "description": "Secure HTTP"},
    {"port": 445, "protocol": "SMB", "description": "Server Message Block"},
    {"port": 3389, "protocol": "RDP", "description": "Remote Desktop Protocol"},
]

# Shuffle and ask 5 random questions
score = 0
for i in range(5):
    q = random.choice(questions)
    answer = input(f"Q{i+1}: What protocol uses port {q['port']}? ").strip()

    if answer.lower() == q["protocol"].lower():
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Incorrect. The correct answer is {q['protocol']} — {q['description']}")

print(f"\nYour score: {score}/5")

# Each question is stored as a dictionary with three parts:
# "port"       → the port number being asked about (e.g., 22)
# "protocol"   → the correct answer (e.g., "SSH")
# "description"→ a short explanation of what the protocol does

# This format makes it easy to:
# - Access specific parts of the question using q["port"], q["protocol"], etc.
# - Keep the data organized and readable
# - Expand the quiz later with more features like multiple choice or scoring

# score = 0
# → Starts the score at 0 before the quiz begins

# for i in range(5):
# → Runs the quiz loop 5 times to ask 5 questions

# q = random.choice(questions)
# → Picks one random question from the list of dictionaries

# f"Q{i+1}: ..." is an f-string
# → It lets you insert variables into a string
# → {i+1} means the question number (starts at 1 instead of 0)

# input(...) asks the user to type their answer
# .strip() removes any extra spaces before or after the answer
# .lower() converts the answer to lowercase so it's easier to compare
# → This way, "SSH", "ssh", or "sSh" will all be treated the same

# if answer.lower() == q["protocol"].lower():
# → Checks if the user's answer matches the correct protocol (case-insensitive)

# If correct:
# → Print "✅ Correct!" and add 1 to the score

# If incorrect:
# → Print "❌ Incorrect" and show the correct answer and explanation

# After the loop ends:
# → Print the final score out of 5
