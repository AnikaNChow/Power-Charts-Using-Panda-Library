

DAU Share>>>>>>>>>>>Plot the DataFrame using Pandas:

import pandas as pd
import matplotlib.pyplot as plt

data = {'Week': [1,2,3,4],
        'DAU_Share %': [2.5,2.5,2.5,3.4]
       }
  
df = pd.DataFrame(data,columns=['Week','DAU_Share %'])
df.plot(x ='Week', y='DAU_Share %', kind = 'bar')
plt.show()