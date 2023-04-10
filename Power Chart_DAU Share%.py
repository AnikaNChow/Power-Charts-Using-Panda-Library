

DAU Share>>>>>>>>>>> Plot the DataFrame using Pandas:

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