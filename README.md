# Weather-ETL-Project
This is a weather data ETL pipeline and dashboard.

## Overview

This project is an entire end-to-end pipeline with ETL (Extract, Transform, Load) using real time weather data. It fetches real-time data from an external API, transforms it into a format that can be used by Python, saves the data in a PostgreSQL database and shares the information with an interactive Power BI dashboard.

The project is one example of the ways raw data can be turned into valuable information via a proper Business Intelligence workflow.


## Business Case

Transportation, tourism, logistics and event planning are among the many sectors that are affected by the weather and thus make decisions on a daily basis that affect them. When conditions change quickly or humidity levels are high, for instance, this can affect timetables, supply chain performance and the customer experience.

But this is just not enough: raw weather data. It is necessary for organizations to have a system that can gather, process and present this data continuously in a structured and interpretable format.

This project aims to do just that by establishing an automated pipeline that:

Gathers up-to-the-minute weather information from several cities.  
- Converts information from raw data into meaningful and organized format  
- Records the data for historical purposes  
- Offers visual clues for further analysis  
- Alerts for critical conditions when detected  

The aim is to replicate a ‘real world' BI solution with data to aid in monitoring and decision-making.



## Technologies Used

- **Requests** - Python library that sends HTTP requests.- **Pandas** - Python library for data manipulation and analysis.  
- **PostgreSQL** (Data Storage)  
Power BI (Data Visualization)  
The source of data is OpenWeather API.OpenWeather API is used as data source.  
- **SMTP** (Email Alerts)  
Task Scheduling (Automation) in Windows Task Scheduler.



## ETL Pipeline

### 1. Extract
The following cities' weather data is gathered from the OpenWeather API:
- Munich  
- Berlin  
- Paris  
- London  
- Rome  

The data consists of temperature, humidity, pressure, weather description and timestamps.



### 2. Transform
Data is extracted, cleaned and prepared with Python:

- Made sure that the time stamps are in standard format.  
- Removed inconsistencies  
When a new feature, "temperature category", is added to the table.When a new feature “temperature category” is added to the table.
  - Cold (< 10°C)  
  - Moderate (10–25°C)  
  - Hot (> 25°C)  

This is an important step to get the data ready for analysis.



### 3. Load
The cleaned data has been put into a PostgreSQL database:

- Database: `weather_db`  
- Table: `weather_data`  

The data is added on every run of the pipeline, which gives the ability to track data over time.



## Automation & Alerts

Automated via Windows Task Scheduler, the ETL pipeline is run automatically to update data continuously, rather than manually.

Moreover, an alert system based on data is put into use:

Alerts will be generated when:
  - Exceeding of the temperature levels.  
  - Unusually humid situations  

- Notifications are sent via email (smtp)  

This feature takes into account the actual monitoring and warning systems in the real world.



## Dashboard (Power BI)

The Power BI dashboard gives a dynamic visualization of the data:
<img width="754" height="428" alt="image" src="https://github.com/user-attachments/assets/038939b3-a2fe-4118-8a87-f08410e7b019" />

The dashboard allows users to easily gain insight into patterns, and compare conditions between locations.


## Key Insights

The temperature in Paris is the highest of the selected cities all the time.  
- Majority of observations are within the moderate temperature range.  
- Trends in temperatures are fairly constant with time  
- There is a wide range of humidity, depending on the area  

The insights show the power of processing data to aid informed decision-making.


## Conclusion

The aim of this project was to achieve a complete Business Intelligence pipeline from data collection to visualization, which has been accomplished.

It illustrates the value of real-time data being turned into actionable intelligence through automation, well-structured data storage, and easy visualization.

The solution is representative of real-life industrial use cases, in which continuous data processing and monitoring are key.


## Future Improvements

Integrating machine learning for temperature prediction has been implemented in a number of systems.  
Implementing system on cloud platforms.  
Incorporating real time streaming pipelines  
Improve alerting with advanced triggering and alert rules  

