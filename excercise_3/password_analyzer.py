# Analyze password strength and suggest improvements using multiple criteria.

# ### 📋 Requirements
# 1. Check passwords against these criteria:
#    - Length (minimum 8 characters)
#    - Contains uppercase letters
#    - Contains lowercase letters
#    - Contains numbers
#    - Contains special characters (!@#$%^&*)
#    - Not a common password (maintain list of 20+ common passwords)
# 2. Scoring system: Each criterion = 20 points (max 120 points)
# 3. Strength levels: Weak(0-40), Fair(41-60), Good(61-80), Strong(81-100), Excellent(101-120)
# 4. Generate specific improvement suggestions

# ### 💡 Key Concepts Tested
# - String methods, character validation
# - List membership, scoring algorithms
# - Complex conditional logic


# def check_password_strength(password):
#     has_upper = False
#     has_lower = False
#     has_digit = False
#     has_special = False
#     for char in password:
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower= True
#         elif char.isdigit():
#             has_digit = True
#         elif char in "!@#$%^&*()":
#             has_special = True
#     if len(password)>= 8 and has_upper and has_lower and has_special and has_digit:
#         return "strong"
#     elif len(password)>=6 and has_upper and has_lower and has_digit:
#         return "medium"
#     else:
#         return "weak"
def password_strength(password):
    score=0
    suggestions=[]
    common_passwords=[
        "123456","password", "qwerty", "12345678","1234567", "dragon", "baseball" "letmen", "helo123", "master", "abc123", "football"
    ]
    if len(password)>=8:
        score +=20
    else:
        suggestions.append("Make it at least 8 characters long")
has_upper=False
for ch in password:
    if 'A'<=ch<='Z':
        has_upper=True
        break
if has_upper:
    score +=20
else:
    suggestions.append("Add atleast one uppercase letter")
has_lower = False
for ch in password:
    if 'a'<=ch<='z':
        has_lower=True
        break
if has_lower:
    score +=20
else:
    suggestions.append("add atleast one lower case")
has_digit = False
for ch in password:
    if '0'<=ch<='9':
        has_digit=True
        break
if has_digit:
    score +=20
else:
    suggestions.append("add atleast one digit number")
special_chars = "!@#$%^&*()_-+=[]{};:',.<>?/"
has_special = False
for ch in password:
    if ch in special_chars:
        has_special=True
        break
if has_special:
    score +=20
else:
    suggestions.append("add a special chracter")
if password.lower() not in common_passwords:
    score +=20
else:
    suggestions.append("Avoid common passwords")
    return score,suggestions
Password= input("enter password")
score, suggestions= password_strength(password)
print("\n password score:", score,"/120")
if score ==120:
    print("strong password")
else:
    print("Suggestions to improve your password:")
    for tip in suggestions:
        print("-",tip)
    