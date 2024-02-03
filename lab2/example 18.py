# Python program to convert the month name to a number of days.

# Function to convert month name to number of days
def month_to_days(month_name):
    # Dictionary mapping month names to their respective days
    days_in_month = {
        "January": 31,
        "Feburary": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "November": 31,
        "October": 30,
        "December": 31
    }
    
    # Convert month name to title case for case-insensitivity
    month_name = month_name.title()
    
    # Check if the month name is valid
    if month_name in days_in_month:
        return days_in_month[month_name]
    else:
        return "Invalid month name"
    
# Input
month_name = input("Enter the month name: ")
# Call
result = month_to_days(month_name)
# Print
print(result)
