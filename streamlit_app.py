import streamlit as st
import pandas as pd
import os
from prophet import Prophet
from prophet.plot import plot_plotly
import plotly.graph_objects as go

st.set_page_config(
    layout="wide",
    page_title="Smart Energy Forecaster",
    page_icon="⚡"
)

st.title("⚡ Smart Energy Forecaster")

LOCAL_DATA_PATH = 'household_power_consumption.csv'
DATA_URL = "https://storage.googleapis.com/kagglesdsdata/datasets/8331998/13150534/household_power_consumption.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20250923%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20250923T180227Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=1dddca7d05b47e879422a09b551729a1c6f3e55d6781aaa5b307f92600c3ed0989ef791645380cdaa6502dc3f9f881487b5c3d6c3abbb3d8a8b95756a2078b555a7578948bdd8e75c80cf27910c707a09a2c7f537d54b0c7271c0af0d1dca3c445173f01cd5d79c74cec1d434d3624fad0fe76316cb6760fac9b0773ba0cb9664725856a6f05ccbad70b128bf5076883b73f9cb715d077e765b4955fbfceb5ccd964612b415c20f3c8b9066411666ac05243b7d6a88054c96d945aa08ff030c129672739810163862f106e22b621096cf835429b0c2aae747a98d46e460d6d378eb652c455052c94466d5e6ba19efe6ffa44b36a9d917b288993f5f931fe5f24"

@st.cache_data
def load_data():
    if os.path.exists(LOCAL_DATA_PATH):
        source = LOCAL_DATA_PATH
    elif "IS_DEPLOYED" in st.secrets:
        source = DATA_URL
    else:
        source = DATA_URL
    
    read_params = {
        'sep': ';',
        'parse_dates': {'dt': ['Date', 'Time']},
        'infer_datetime_format': True,
        'low_memory': False,
        'na_values': ['nan', '?']
    }
    if 'kaggle.com' in source or 'googleapis.com' in source:
        read_params['compression'] = 'zip'

    df = pd.read_csv(source, **read_params)
    df = df.set_index('dt')
    df_daily = df['Global_active_power'].resample('D').sum().reset_index()
    df_daily.rename(columns={'dt': 'ds', 'Global_active_power': 'y'}, inplace=True)
    df_daily.dropna(inplace=True)
    return df_daily

@st.cache_data
def create_forecast(_df):
    model = Prophet()
    model.fit(_df)
    future = model.make_future_dataframe(periods=365)
    forecast = model.predict(future)
    return forecast, model

try:
    daily_data = load_data()
    st.success("Data loaded successfully!")
    
    st.subheader("Forecasted Energy Consumption")
    forecast_df, model = create_forecast(daily_data)
    
    fig = plot_plotly(model, forecast_df)
    fig.update_layout(
        title="Forecasted Daily Energy Consumption for the Next Year",
        xaxis_title="Date",
        yaxis_title="Total Watt-hours"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Forecast Components")
    fig2 = model.plot_components(forecast_df)
    st.write(fig2)

except Exception as e:
    st.error(f"An error occurred: {e}")