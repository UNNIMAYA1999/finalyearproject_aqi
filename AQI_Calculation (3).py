## importing packages
import numpy as np
import pandas as pd


fileName = 'ekm_data_extracted_2_preProcessed'
df = pd.read_csv(fileName+'.csv')


#df.columns = ['City','Date','PM2.5', 'NO2', 'NH3', 'CO', 'Benzene', 'Toluene', 'Xylene']

#df.columns = ['Date','PM2.5', 'PM10', 'O3', 'NO2', 'SO2', 'CO']



# print(df["PM10_24hr_avg"])

## PM2.5 Sub-Index calculation
def get_PM25_subindex(x):
    if x <= 30:
        return x * 50 / 30
    elif x <= 60:
        return 50 + (x - 30) * 50 / 30
    elif x <= 90:
        return 100 + (x - 60) * 100 / 30
    elif x <= 120:
        return 200 + (x - 90) * 100 / 30
    elif x <= 250:
        return 300 + (x - 120) * 100 / 130
    elif x > 250:
        return 400 + (x - 250) * 100 / 130
    else:
        return 0


    
    
# df["PM2.5_SubIndex"] = df["PM2.5_24hr_avg"].apply(lambda x: get_PM25_subindex(x))
df["PM2.5_SubIndex"] = df["PM2.5"].apply(lambda x: get_PM25_subindex(x))

## PM10 Sub-Index calculation
def get_PM10_subindex(x):
    if x <= 50:
        return x
    elif x <= 100:
        return x
    elif x <= 250:
        return 100 + (x - 100) * 100 / 150
    elif x <= 350:
        return 200 + (x - 250)
    elif x <= 430:
        return 300 + (x - 350) * 100 / 80
    elif x > 430:
        return 400 + (x - 430) * 100 / 80
    else:
        return 0

# df["PM10_SubIndex"] = df["PM10_24hr_avg"].apply(lambda x: get_PM10_subindex(x))
df["PM10_SubIndex"] = df["PM10"].apply(lambda x: get_PM10_subindex(x))

## SO2 Sub-Index calculation
def get_SO2_subindex(x):
    if x <= 40:
        return x * 50 / 40
    elif x <= 80:
        return 50 + (x - 40) * 50 / 40
    elif x <= 380:
        return 100 + (x - 80) * 100 / 300
    elif x <= 800:
        return 200 + (x - 380) * 100 / 420
    elif x <= 1600:
        return 300 + (x - 800) * 100 / 800
    elif x > 1600:
        return 400 + (x - 1600) * 100 / 800
    else:
        return 0

# df["SO2_SubIndex"] = df["SO2_24hr_avg"].apply(lambda x: get_SO2_subindex(x))
df["SO2_SubIndex"] = df["SO2"].apply(lambda x: get_SO2_subindex(x))

## NOx Sub-Index calculation
def get_NOx_subindex(x):
    if x <= 40:
        return x * 50 / 40
    elif x <= 80:
        return 50 + (x - 40) * 50 / 40
    elif x <= 180:
        return 100 + (x - 80) * 100 / 100
    elif x <= 280:
        return 200 + (x - 180) * 100 / 100
    elif x <= 400:
        return 300 + (x - 280) * 100 / 120
    elif x > 400:
        return 400 + (x - 400) * 100 / 120
    else:
        return 0

# df["NOx_SubIndex"] = df["NOx_24hr_avg"].apply(lambda x: get_NOx_subindex(x))
df["NO2_SubIndex"] = df["NO2"].apply(lambda x: get_NOx_subindex(x))

# ## NH3 Sub-Index calculation
# def get_NH3_subindex(x):
#     if x <= 200:
#         return x * 50 / 200
#     elif x <= 400:
#         return 50 + (x - 200) * 50 / 200
#     elif x <= 800:
#         return 100 + (x - 400) * 100 / 400
#     elif x <= 1200:
#         return 200 + (x - 800) * 100 / 400
#     elif x <= 1800:
#         return 300 + (x - 1200) * 100 / 600
#     elif x > 1800:
#         return 400 + (x - 1800) * 100 / 600
#     else:
#         return 0

# # df["NH3_SubIndex"] = df["NH3_24hr_avg"].apply(lambda x: get_NH3_subindex(x))
# df["NH3_SubIndex"] = df["NH3"].apply(lambda x: get_NH3_subindex(x))


## CO Sub-Index calculation
def get_CO_subindex(x):
    if x <= 1:
        return x * 50 / 1
    elif x <= 2:
        return 50 + (x - 1) * 50 / 1
    elif x <= 10:
        return 100 + (x - 2) * 100 / 8
    elif x <= 17:
        return 200 + (x - 10) * 100 / 7
    elif x <= 34:
        return 300 + (x - 17) * 100 / 17
    elif x > 34:
        return 400 + (x - 34) * 100 / 17
    else:
        return 0

# df["CO_SubIndex"] = df["CO_8hr_max"].apply(lambda x: get_CO_subindex(x))
df["CO_SubIndex"] = df["CO"].apply(lambda x: get_CO_subindex(x))

## O3 Sub-Index calculation
def get_O3_subindex(x):
    if x <= 50:
        return x * 50 / 50
    elif x <= 100:
        return 50 + (x - 50) * 50 / 50
    elif x <= 168:
        return 100 + (x - 100) * 100 / 68
    elif x <= 208:
        return 200 + (x - 168) * 100 / 40
    elif x <= 748:
        return 300 + (x - 208) * 100 / 539
    elif x > 748:
        return 400 + (x - 400) * 100 / 539
    else:
        return 0

# df["O3_SubIndex"] = df["O3_8hr_max"].apply(lambda x: get_O3_subindex(x))
df["O3_SubIndex"] = df["O3"].apply(lambda x: get_O3_subindex(x))

## AQI bucketing
def get_AQI_bucket(x):
    if x <= 50:
        return "Good"
    elif x <= 100:
        return "Satisfactory"
    elif x <= 200:
        return "Moderate"
    elif x <= 300:
        return "Poor"
    elif x <= 400:
        return "Very Poor"
    elif x > 400:
        return "Severe"
    else:
        return np.NaN

# df["Checks"] = (df["PM2.5_SubIndex"] > 0).astype(int) + \
#                 (df["PM10_SubIndex"] > 0).astype(int) + \
#                 (df["NO2_SubIndex"] > 0).astype(int) + \
#                 (df["NH3_SubIndex"] > 0).astype(int) + \
#                 (df["CO_SubIndex"] > 0).astype(int) 
              


# df["Checks"] = (df["PM2.5_SubIndex"] > 0).astype(int) + \
#                 (df["NO2_SubIndex"] > 0).astype(int) + \
#                 (df["NH3_SubIndex"] > 0).astype(int) + \
#                 (df["CO_SubIndex"] > 0).astype(int) 


df["Checks"] = (df["PM2.5_SubIndex"] > 0).astype(int) + \
                (df["PM10_SubIndex"] > 0).astype(int) + \
                (df["SO2_SubIndex"] > 0).astype(int) + \
                (df["NO2_SubIndex"] > 0).astype(int) + \
                (df["CO_SubIndex"] > 0).astype(int) + \
                (df["O3_SubIndex"] > 0).astype(int)
               

# df["AQI_calculated"] = round(df[["PM2.5_SubIndex", "PM10_SubIndex", "SO2_SubIndex", "NOx_SubIndex",
#                                   "NH3_SubIndex", "CO_SubIndex", "O3_SubIndex"]].max(axis = 1))
# df.loc[df["PM2.5_SubIndex"] + df["PM10_SubIndex"] <= 0, "AQI_calculated"] = np.NaN



# df["AQI_calculated"] = round(df[["PM2.5_SubIndex", "NO2_SubIndex",
#                                   "NH3_SubIndex", "CO_SubIndex"]].max(axis = 1))






df["AQI_calculated"] = round(df[["PM2.5_SubIndex", "PM10_SubIndex", "NO2_SubIndex","O3_SubIndex", "SO2_SubIndex",
                                  "CO_SubIndex"]].max(axis = 1))
df.loc[df["PM2.5_SubIndex"] + df["PM10_SubIndex"] <= 0, "AQI_calculated"] = np.NaN
df.loc[df.Checks < 3, "AQI_calculated"] = np.NaN

df["AQI_bucket_calculated"] = df["AQI_calculated"].apply(lambda x: get_AQI_bucket(x))
df[~df.AQI_calculated.isna()].head(13)


df[~df.AQI_calculated.isna()].AQI_bucket_calculated.value_counts()


outputFileName = fileName +'_AQICalculated.csv'
df.to_csv(outputFileName, index=False)


