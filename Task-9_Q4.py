import re
def validate_input(pattern, input_string):
    regex = re.compile(pattern)
    return bool(regex.match(input_string))
# a) Email address
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# b) Mobile numbers of Bangladesh
bangladesh_mobile_pattern = r'^\+8801[3-9]\d{8}$'
# c) Telephone numbers of USA 
usa_telephone_pattern = r'^\+1\d{10}$'
# d) 16 character alpha-numeric password
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
#cases
email = "peace@gmail.com"
mobile_number = "+8801712345678"
telephone_number = "+11234567890"
password = "yolo4321@5678EFGH"
print("Email:", validate_input(email_pattern, email))
print("Mobile Number:", validate_input(bangladesh_mobile_pattern, mobile_number))
print("Telephone Number:", validate_input(usa_telephone_pattern, telephone_number))
print("Password:", validate_input(password_pattern, password))
