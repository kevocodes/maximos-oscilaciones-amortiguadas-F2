import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Leer el archivo CSV
df = pd.read_csv('Oscilacion.csv')

# Obtener los valores de tiempo y ángulo
tiempo = df['tiempo']
angulo = df['ángulo']

# Encontrar los máximos de amplitud utilizando la función find_peaks
peaks, _ = find_peaks(angulo, prominence=0.1)  # Ajusta la prominencia según tu caso

# Filtrar picos repetidos con el mismo ángulo
filtered_peaks = [peaks[0]]
for peak in peaks[1:]:
    if angulo[peak] != angulo[filtered_peaks[-1]]:
        filtered_peaks.append(peak)

# Obtener los tiempos y ángulos correspondientes a los máximos de amplitud
maximos_amplitud = [(tiempo[p], angulo[p]) for p in filtered_peaks]

# Guardar los máximos de amplitud en un archivo CSV
df_maximos = pd.DataFrame(maximos_amplitud, columns=['tiempo', 'angulo'])
df_maximos.to_csv('maximos_amplitud.csv', index=False)

# Graficar la oscilación y marcar los máximos de amplitud
plt.plot(tiempo, angulo, label='Oscilación')
plt.plot(tiempo[filtered_peaks], angulo[filtered_peaks], "ro")  # Marcar los máximos con puntos rojos

plt.xlabel('Tiempo')
plt.ylabel('Ángulo')
plt.title('Oscilación con máximos de amplitud')
plt.xticks(tiempo[::1000])  # Marcas de tiempo cada 1000 puntos (ajusta según tus necesidades)
plt.legend()
plt.grid(True)

# Guardar la gráfica como imagen
plt.savefig('grafica_oscilacion.png')

# Mostrar la gráfica
plt.show()
