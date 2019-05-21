import datetime
import pandas as pd
import time
from pvlib.forecast import GFS as local_GFS
from ether.pvlib.forecast import GFS as ether_GFS

coordinates = [
  (30, -110, 'Tucson', 700, 'Etc/GMT+7'),
  (35, -105, 'Albuquerque', 1500, 'Etc/GMT+7'),
  (40, -120, 'San Francisco', 10, 'Etc/GMT+8'),
  (50, 10, 'Berlin', 34, 'Etc/GMT-1')
]

fx_model = local_GFS()
fx_data = []

s = time.time()
for latitude, longitude, name, altitude, timezone in coordinates:
  start = pd.Timestamp(datetime.date.today(), tz=timezone)
  end = start + pd.Timedelta(days=30)
  fx_data.append(fx_model.get_processed_data(latitude, longitude, start, end))
print("Time taken (locally): ", time.time() - s)

ether_fx_model = ether_GFS()
ether_fx_data = []

s = time.time()
for latitude, longitude, name, altitude, timezone in coordinates:
  start = pd.Timestamp(datetime.date.today(), tz=timezone)
  end = start + pd.Timedelta(days=30)
  ether_fx_data.append(ether_fx_model.get_processed_data(latitude, longitude, start, end))
print("Time taken (ether fx): ", time.time() - s)