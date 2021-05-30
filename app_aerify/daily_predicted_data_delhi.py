import pandas as pd


# def get_daily_delhi_pred(BASE_DIR):    
    
#          print("Inside get_daily_delhi_pred")
#          # data_df = pd.read_csv(BASE_DIR + "/app_aerify/daily_predicted_data_delhi/predicted_delhi.csv")
#          data_df = pd.read_csv(BASE_DIR + "/app_aerify/daily_predicted/predicted_trivandrum.csv")
#          data = list(data_df["AQI"])
#          date = list(data_df["Date"])
#          print("Exiting get_daily_delhi_pred")
#          return {"aqi": data, "date":date}
      



def get_daily_data_pred(city, BASE_DIR):
    print("Inside get_daily_data_pred")       

    data = []
    
    if city == "Thiruvananthapuram":
        data_df = pd.read_csv(
            BASE_DIR+"/app_aerify/daily_predicted_data/predicted_trivandrum.csv")
   # elif city == "Delhi":
#    data_df = pd.read_csv(
 #           BASE_DIR+"/app_aerify/daily_predicted_data/predicted_delhi.csv")
  #  elif city == "Ahmedabad":
   #     data_df = pd.read_csv(
    #        BASE_DIR+"/app_aerify/yearly_predicted_data/pred_Ahmedabad.csv")
    else:
        data_df = pd.read_csv(
            BASE_DIR+"/app_aerify/daily_predicted_data/predicted_delhi.csv")


    data = list(data_df["AQI"])
    date = list(data_df["date"])
    # print(data)
    # print(date)
    return {"aqi": data, "date": date}







