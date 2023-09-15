import numpy as np
import matplotlib
import base64
from io import BytesIO
from matplotlib.figure import Figure
import math

class CalcPopulation:

    def __init__(self, growth_rate_per_year, init_population, time_in_years):

        matplotlib.use('Agg')

        self.growth_rate_per_year = growth_rate_per_year
        self.init_population = init_population
        self.time_in_years = np.arange(0, time_in_years+1)
        self.population_values_across_years =  [ self.__calculate_population(year) for year in self.time_in_years ]

    def __calculate_population(self, year):
        return self.init_population * math.exp(self.growth_rate_per_year * year)
        # return math.ceil(self.init_population * (1 + self.growth_rate_per_year) ** year)
    
    def generate_graph_in_hex(self):

        figure = Figure()
        ax = figure.subplots()

        ax.plot(self.time_in_years, self.population_values_across_years, marker='o', linestyle='-')
        ax.grid()

        image_data = self.convert_to_hexadecimal(figure)
        
        return f"data:image/png;base64,{image_data}"
    
    def convert_to_hexadecimal(self, figure):

        buffer = BytesIO()
        figure.savefig(buffer, format='png')
        buffer.seek(0)

        data = base64.b64encode(buffer.getbuffer()).decode()
        buffer.close()

        return data

    def get_population_values_across_years(self):
        return self.population_values_across_years
    
        # plt.xlabel('Años')
        # plt.ylabel('Población')
        # plt.title('Crecimiento de Población con Tasa de Crecimiento de 0.1 por')