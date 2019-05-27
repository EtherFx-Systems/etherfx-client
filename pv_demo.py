import dep_ignore
import datetime
import pandas as pd
import time
import pvlib.forecast as forecast
import ether.pvlib.forecast as eforecast

coordinates = [
  (30, -110, 'Tucson', 700, 'Etc/GMT+7'),
  (35, -105, 'Albuquerque', 1500, 'Etc/GMT+7'),
  (40, -120, 'San Francisco', 10, 'Etc/GMT+8'),
  (50, 10, 'Berlin', 34, 'Etc/GMT-1'),
  (30, -110, 'Tucson', 700, 'Etc/GMT+7'),
  (35, -105, 'Albuquerque', 1500, 'Etc/GMT+7'),
  (40, -120, 'San Francisco', 10, 'Etc/GMT+8'),
  (50, 10, 'Berlin', 34, 'Etc/GMT-1')
]

fx_model = forecast.GFS()
fx_data = []

s = time.time()
for latitude, longitude, name, altitude, timezone in coordinates:
  start = pd.Timestamp(datetime.date.today(), tz=timezone)
  end = start + pd.Timedelta(days=30)
  fx_data.append(fx_model.get_processed_data(latitude, longitude, start, end))
print("Time taken (locally): ", time.time() - s)

ether_fx_model = eforecast.GFS()
ether_fx_data = []

s = time.time()
for latitude, longitude, name, altitude, timezone in coordinates:
  start = pd.Timestamp(datetime.date.today(), tz=timezone)
  end = start + pd.Timedelta(days=30)
  foo = ether_fx_model.get_processed_data(latitude, longitude, start, end)
  ether_fx_data.append(foo)

ether_fx_data = [i.exec() for i in ether_fx_data]
print("Time taken (ether fx): ", time.time() - s)

#from pvlib.modelchain import ModelChain
#from pvlib.tracking import SingleAxisTracker
#from pvlib.pvsystem import PVSystem, retrieve_sam
#sandia_modules = retrieve_sam('sandiamod')
#cec_inverters = retrieve_sam('cecinverter')
#module = sandia_modules['Canadian_Solar_CS5P_220M___2009_']
#inverter = cec_inverters['SMA_America__SC630CP_US_315V__CEC_2012_']
#system = SingleAxisTracker(module_parameters=module,inverter_parameters=inverter,modules_per_string=15,strings_per_inverter=300)
#mc = ModelChain(system, ether.location)
#mc.run_model(ether_fx_data.index, weather=ether_fx_data)
#mc.total_irrad.plot()

#print(ether_fx_data)
#start = pd.Timestamp(datetime.date.today())
#end = start + pd.Timedelta(days=30)
