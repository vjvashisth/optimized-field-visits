# forecast_kpi.py
import pandas as pd
from fbprophet import Prophet

# Function to forecast KPI values
def forecast_kpi(data, forecast_period=5):
    # Convert the 'date' column to datetime format
    data['ds'] = pd.to_datetime(data['ds'])
    
    # Prophet requires columns 'ds' and 'y'
    df = data.rename(columns={'date': 'ds', 'value': 'y'})
    
    # Initialize the Prophet model
    model = Prophet()

    # Fit the model with the data
    model.fit(df)

    # Create future dates for predictions
    future = model.make_future_dataframe(df, periods=forecast_period)

    # Make the forecast
    forecast = model.predict(future)
    
    return forecast

# Example usage
if __name__ == "__main__":
    # Load your actual KPI data (ensure it has 'date' and 'value' columns)
    data = pd.read_csv('data/sample_kpi_data.csv')

    # Forecast the next 5 days
    forecast = forecast_kpi(data, forecast_period=5)
    
    # Show the forecasted values for the next 5 days
    print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(5))
