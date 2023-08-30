from Weather_api import get_weather,get_weather_details, Weather

def main():
    user_city: str = input('Enter A city: ')
    
    # Get the current weather details
    current_weather: dict = get_weather(user_city, mock=False)
    weather_details: list[Weather] = get_weather_details(current_weather)
    
    # Get the current days
    date_format: str = "%d/%m/%y"
    days:list[str] = sorted(list({f'{date.date:{date_format}}' for date in weather_details}))
   
    for day in days:
        print(day)
        print('---')
    
    grouped = [current for current in weather_details if f'{current.date:{date_format}}' == day]
    for element in grouped:
        print(element)
    
if __name__ == '__main__':
    main()