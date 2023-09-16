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
        #  math.e ** (self.growth_rate_per_year * year) == math.exp(self.growth_rate_per_year * year )
        # return float(format( self.init_population * math.e ** (self.growth_rate_per_year * year), ".2f")) 
        return float(format( self.init_population * math.exp(self.growth_rate_per_year * year ), ".2f"))
    
    def generate_graph_in_hex(self):

        figure = Figure()
        ax = figure.subplots()

        ax.plot(self.time_in_years, self.population_values_across_years, marker='o', linestyle='-')
        ax.grid()
        ax.set_xlabel("Años")
        ax.set_ylabel('Población')
        ax.set_title(f'Crecimiento de Población con Tasa de Crecimiento de {self.growth_rate_per_year} por Año')
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
    