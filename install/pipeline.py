from ingest import fetch_weather_data

API_KEY = "65277f3d6378a665cad2d380f7ea47f4"

if __name__ == "__main__":
    data = fetch_weather_data("Delhi", API_KEY)
    weather = data["weather"][0]
    print(data)