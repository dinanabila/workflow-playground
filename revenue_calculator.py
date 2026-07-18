import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/dinanabila/workflow-playground/refs/heads/main/source_data.csv')
df_result = pd.DataFrame({'revenue_total': [df['revenue'].sum()]})

df_result.to_csv('result_data.csv', index=False)
