import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

input_path = 'ghcnd_daily.csv'
columns_to_keep = ['id', 'year', 'month', 'element'] + [f'value{i}' for i in range(1, 32)]
value_cols = [f'value{i}' for i in range(1, 32)]

# Especificar dtype para evitar warnings
dtype_spec = {
    'id': 'object', 'year': 'int32', 'month': 'int32', 'element': 'object',
    **{f'value{i}': 'float32' for i in range(1, 32)}
}

# Ler e limpar chunk
chunk = pd.read_csv(input_path, nrows=100000, dtype=dtype_spec, na_values=-9999)
chunk = chunk[columns_to_keep]

# Uso de memória original
mem_before = chunk.memory_usage(deep=True) / 1024  # KB

# Processar
chunk['year'] = chunk['year'].astype('int16')
chunk['month'] = chunk['month'].astype('int8')
chunk['element'] = chunk['element'].astype('category')
chunk['id'] = chunk['id'].astype('category')
for col in value_cols:
    chunk[col] = chunk[col].astype('float32')

# Uso de memória após
mem_after = chunk.memory_usage(deep=True) / 1024

# Comparação
mem_comparison = pd.DataFrame({'Antes (KB)': mem_before, 'Depois (KB)': mem_after})
mem_comparison = mem_comparison.loc[columns_to_keep]

# Plot
mem_comparison.plot(kind='bar', figsize=(14, 6), color=['red', 'green'])
plt.title('Uso de Memória por Coluna Antes vs Depois da Conversão de Tipos')
plt.ylabel('Memória (KB)')
plt.xlabel('Colunas')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend(loc='upper right')
plt.show()
