# coding: utf-8

# In[1]:


def get_stat_data(BASE_DIR):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    # import seaborn as sns
    from sklearn.impute import SimpleImputer
    import warnings

    warnings.filterwarnings("ignore")

    # In[2]:

    df = pd.read_csv(BASE_DIR+"/app_aerify/stats_data.csv")
    df = df.drop(['stn_code', 'agency'], axis=1)

    #imputer = SimpleImputer(missing_values='NaN', strategy='mean', axis=0)
    imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputer = imputer.fit(df.iloc[:, 3:8].values)
    df.iloc[:, 3:8] = imputer.transform(df.iloc[:, 3:8].values)

    commonArea = 'Residential, Rural and other Areas'
    df['type'] = df['type'].fillna(commonArea)
    statewise_emission = df.groupby('state').mean()[['so2', 'no2', 'pm10', 'co', 'pm2_5']]

    dik = {}
    list1 = list(statewise_emission.index.values)
    list2 = list(statewise_emission['so2'])
    list3 = list(statewise_emission['no2'])
    list4 = list(statewise_emission['pm10'])
    list5 = list(statewise_emission['co'])
    l = [list1, list2, list3, list4, list5]
    dik['allstate_so2_no2_pm10_co'] = l

    # In[20]:

    states_highest_no2 = statewise_emission.sort_values('no2', ascending=False).head(10)
    states_highest_no2 = states_highest_no2.loc[:, ['no2']]
    dik['state_high_no2'] = [list(states_highest_no2.index.values), list(states_highest_no2.no2)]

    # In[23]:

    states_highest_so2 = statewise_emission.sort_values('so2', ascending=False).head(10)
    states_highest_so2 = states_highest_so2.loc[:, ['so2']]
    dik['state_high_so2'] = [list(states_highest_so2.index.values), list(states_highest_so2.so2)]


    # In[24]:

    states_highest_pm10 = statewise_emission.sort_values('pm10', ascending=False).head(10)
    states_highest_pm10 = states_highest_pm10.loc[:, ['pm10']]
    dik['state_high_pm10'] = [list(states_highest_pm10.index.values), list(states_highest_pm10.pm10)]

    # In[25]:

    states_highest_co = statewise_emission.sort_values('co', ascending=False).head(10)
    states_highest_co = states_highest_co.loc[:, ['co']]
    dik['state_high_co'] = [list(states_highest_co.index.values), list(states_highest_co.co)]

    # In[26]:

    locationwise_emission = df.groupby('location').mean()[['so2', 'no2', 'pm10', 'co', 'pm2_5']]

    # In[27]:

    loc_highest_pm10 = locationwise_emission.sort_values('pm10', ascending=False).head(10)
    loc_highest_pm10 = loc_highest_pm10.loc[:, ['pm10']]
    dik['loc_high_pm10'] = [list(loc_highest_pm10.index.values), list(loc_highest_pm10.pm10)]

    # In[28]:

    loc_highest_co = locationwise_emission.sort_values('co', ascending=False).head(10)
    loc_highest_co = loc_highest_co.loc[:, ['co']]
    dik['loc_high_co'] = [list(loc_highest_co.index.values), list(loc_highest_co.co)]

    # In[29]:

    loc_highest_so2 = locationwise_emission.sort_values('so2', ascending=False).head(10)
    loc_highest_so2 = loc_highest_so2.loc[:, ['so2']]
    dik['loc_high_so2'] = [list(loc_highest_so2.index.values), list(loc_highest_so2.so2)]

    # In[30]:

    loc_highest_no2 = locationwise_emission.sort_values('no2', ascending=False).head(10)
    loc_highest_no2 = loc_highest_no2.loc[:, ['no2']]
    dik['loc_high_no2'] = [list(loc_highest_no2.index.values), list(loc_highest_no2.no2)]
    # print(dik.keys())
    return dik

