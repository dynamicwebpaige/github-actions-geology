import pandas as pd

# Utility function to scrape space weather data.
def scrape_space_weather(url):
  df =  pd.read_json(url)
  return re.sub(r"\[?\s*(\d+)(?=(?:, \d+)|\])(?=[^\[]*\]).", "", df.to_csv(index=False))


if __name__ == '__main__':
    with open('data.csv', 'w+') as f:
        f.write(scrape_space_weather('https://services.swpc.noaa.gov/products/solar-wind/mag-7-day.json'))
