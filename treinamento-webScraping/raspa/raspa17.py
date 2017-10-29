import wbdata
import matplotlib.pyplot as plt
#https://blogs.worldbank.org/opendata/accessing-world-bank-data-apis-python-r-ruby-stata 
countries = ["CL","UY","BR"]
indicators = {'NY.GNP.PCAP.CD':'GNI per Capita'}
 
df = wbdata.get_dataframe(indicators, country=countries, convert_date=False)

dfu = df.unstack(level=0)

dfu.plot()
plt.legend(loc='best')
plt.title("GNI Per Capita ($USD, Atlas Method)")
plt.xlabel('Date')
plt.ylabel('GNI Per Capita ($USD, Atlas Method')
plt.show()
