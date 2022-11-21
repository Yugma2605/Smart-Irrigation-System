import requests
class weather:
    
    def get_weather_params():

        # url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/3038401?apikey=e6c0Bqg3AOXd9NHkSxcz5ICLiOdATLdg&language=en-us&details=true&metric=true"

        # response = requests.get(url)
        
        # a = response.json()
        # x = a["DailyForecasts"]
        # x = x[0]
        # x = x["Day"]
        # Precipitation_Probability = x["PrecipitationProbability"]
        # Rain = x["Rain"]
        # Rain = Rain["Value"]
        # Evapotranspiration = x["Evapotranspiration"]
        # Evapotranspiration = Evapotranspiration["Value"]

        url = "https://bestweather.p.rapidapi.com/weather/SG%20Highway%20Ahmedabad%20India/today"
        querystring = {"unitGroup":"us"}
        headers = {
            'x-rapidapi-host': "bestweather.p.rapidapi.com",
            'x-rapidapi-key': "c872a32e10msh186c1dbbae670f8p18eb20jsne2912312048f"
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()
        a = response["days"]
        a = a[0]
        a = a["precipprob"]

        b = response["currentConditions"]
        b = b["precip"]
        # print(response["precip"])
        # print(response["precipprob"])



        return {
            "Precipitation_Probability":a, 
            "Rain":b
            # "Evapotranspiration":Evapotranspiration
            }
        