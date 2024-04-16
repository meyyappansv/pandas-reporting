import pandas as pd
dtype_dict = {
    'DATE':  str,
    'TIMESTAMP':  str,
    'PRODUCTNAME': str,
    'MBSERIAL': str,
    'BIOSINFO': str,
    'TOTALMEM/Kb': float,
    'CPUNUM': int,
    'CPU FREQUENCY': float,
    'CPU1Temp/°C': float,
    'RESULT': str,
    'CPU2Temp/°C': float,
    'PCHTemp/°C': float,
    'CPU UTIL/%': float,
    'MEMORY UTIL/%': float,
    'P[0-9]-DIMM[A-Z][0-9]Temp/°C': float,
     'FAN[0-9]/RPM':float,
     'FAN[A-Z]/RPM': float,
     'SD[A-Z] Read': float,
     'SD[A-Z] Write': float,
     'SD[A-Z] Temp/°C': float,
     '^en[0-9]': int
}