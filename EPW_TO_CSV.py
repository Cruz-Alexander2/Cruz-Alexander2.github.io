import pandas as pd

file_path = r'C:\Users\muham\OneDrive\Desktop\PA_PHILADELPHIA-IAP_724080_18.epw'

# The columns based on EPW file structure
columns = [
    "Year", "Month", "Day", "Hour", "Minute", "Data Source and Uncertainty Flags", 
    "Dry Bulb Temperature", "Dew Point Temperature", "Relative Humidity", 
    "Atmospheric Station Pressure", "Extraterrestrial Horizontal Radiation", 
    "Extraterrestrial Direct Normal Radiation", "Horizontal Infrared Radiation Intensity", 
    "Global Horizontal Radiation", "Direct Normal Radiation", "Diffuse Horizontal Radiation", 
    "Global Horizontal Illuminance", "Direct Normal Illuminance", 
    "Diffuse Horizontal Illuminance", "Zenith Luminance", "Wind Direction", "Wind Speed", 
    "Total Sky Cover", "Opaque Sky Cover", "Visibility", "Ceiling Height", 
    "Present Weather Observation", "Present Weather Codes", "Precipitable Water", 
    "Aerosol Optical Depth", "Snow Depth", "Days Since Last Snowfall", "Albedo", 
    "Liquid Precipitation Depth", "Liquid Precipitation Quantity"
]

# Reading the file , skipping the first 8 lines
df = pd.read_csv(file_path, sep=',', skiprows=8, header=None, names=columns)

# Droping the column with corrupted data
df = df.drop(columns=["Data Source and Uncertainty Flags"])

# Converting to CSV
csv_file_path = r'C:\Users\muham\OneDrive\Desktop\PA_PHILADELPHIA_2018.csv'
df.to_csv(csv_file_path, index=False)


'''
More information on EPW's here:
https://designbuilder.co.uk/cahelp/Content/EnergyPlusWeatherFileFormat.htm#:~:text=The%20EnergyPlus%20data%20dictionary%20format,for%20alphanumeric%3B%20N%20for%20numeric

EPW File Structure: The EPW file structure is well-documented. It includes a header section and a data section. 
The header contains metadata about the weather station and data source, and the data section contains the actual weather data.

Standard Columns: The columns for the weather data section are standardized across all EPW files. 
These typically include year, month, day, hour, minute, and various parameters like temperature, humidity, wind speed, and radiation.
'''

