import datetime

def format_date(date_string):
    date_array = date_string.split()[-2:]   # Ex: Apr 16, March 10
    month_abbreviated = date_array[0]
    day_unformatted = date_array[1]

    month = format_month(month_abbreviated)
    day = ''.join(c for c in day_unformatted if c != ')')
    year = 2020
    
    date_string = str(month) + "-" + str(day) + "-" + str(year)
    date = datetime.datetime.strptime(date_string, "%m-%d-%Y")
    
    return date.date()

def format_month(month_abbreviated):
    if month_abbreviated == "Mar":
        return 3
    elif month_abbreviated == "Apr":
        return 4

def get_days_from_now(shipping_date):
    current_date = datetime.datetime.now().date()
    shipping_date = format_date(shipping_date)
    days_diff = (shipping_date - current_date)  # date object
    
    return days_diff.days
