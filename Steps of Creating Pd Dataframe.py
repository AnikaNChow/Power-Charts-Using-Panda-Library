----------- Step 1: Create the DataFrame

import pandas as pd
   
import pandas as pd
import matplotlib.pyplot as plt

data = {'Week': [1, 2, 3, 4],
        'DAU_Share %': [2.1, 2.4, 3.4, 3.4]
       }
  
df = pd.DataFrame(data, columns=['Week', 'DAU_Share %'])
print (df)


-------Step 2: Plot the DataFrame using Pandas
Finally, you can plot the DataFrame by adding the following syntax:

ax = df.plot(x='Week', y='DAU_Share %', kind='bar', align='edge', width=0.7)


--------3 Adding title and note/insights to your power charts (with x-axis and y-axis labels )


ax.set_title('Daily Active Users:\nE-Commerce Platform', fontsize=12, ha='center', va='bottom')
ax.set_xlabel('Week', fontsize=10)
ax.set_ylabel('DAU Share %', fontsize=10)

note_text = 'Note: The chart illustrates DAU share percentage for an E-Commerce platform over four weeks.'
ax.text(0.5, -0.20, note_text, ha='center', fontsize=10, transform=ax.transAxes,
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5)


----Final Step: Putting everything together:

import pandas as pd
import matplotlib.pyplot as plt


data = {'Week': [1, 2, 3, 4],
        'DAU_Share %': [2.1, 2.4, 3.4, 3.4]
       }
  

df = pd.DataFrame(data, columns=['Week', 'DAU_Share %'])
ax = df.plot(x='Week', y='DAU_Share %', kind='bar', align='edge', width=0.7)


ax.set_title('Daily Active Users:\nE-Commerce Platform', fontsize=12, ha='center', va='bottom')
ax.set_xlabel('Week', fontsize=10)
ax.set_ylabel('DAU Share %', fontsize=10)


note_text = 'Note: The chart illustrates DAU share percentage for an E-Commerce platform over four weeks.'
ax.text(0.5, -0.20, note_text, ha='center', fontsize=10, transform=ax.transAxes,
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))


plt.show()


