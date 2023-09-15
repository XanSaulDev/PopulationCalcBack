from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .CalcPopulation import CalcPopulation




class CalculatePopulation(APIView):

    def post(self, request, *args, **kwargs):
        
        growth_rate = float(request.data.get('rate', 0.1)) 
        initial_population = int(request.data.get('population', 10)) 
        years = int(request.data.get('years', 20))
        
        popolation = CalcPopulation(growth_rate, initial_population, years)
        figure = popolation.generate_graph_in_hex()       
        number_of_population_across_years = popolation.get_population_values_across_years()

        return Response({
            "figure": figure,
            "number_of_population_across_years": number_of_population_across_years
        },
        status.HTTP_200_OK)