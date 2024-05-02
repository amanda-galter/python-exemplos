#Formatação de strings
from datetime import datetime
ano_atual = datetime.now().year
clube='SPFC'
ano_fundaçao=1930
campeonat_mundial= 3
print(f"{clube} possui {campeonat_mundial} titulos mundiais.")
print(f"são {ano_atual - ano_fundaçao} anos de axistência")

