
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY="AIzaSyBm6qXO2Br_0wnqd_UVNsN7NrdhTVhsBz4"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def run():
    context = """
    www.Droit-Afrique.com  OHADA 
      Plan comptable OHADA 1/31OHADA 
      Plan comptable 
      Suivant l’acte uniforme portant organisation et harmonisation  
      des comptabilités des entreprises le 22 février 2000 
      
      Classe  1       ‐       Comptes         de      ressources      durables 
      10      Capital
      101 Capital social 
      - 1011 Capital souscrit, non appelé 
      - 1012 Capital souscrit, appelé, non versé - 1013 Capital souscrit, appelé, versé, non amorti - 1014 Capital souscrit, appelé, versé, amorti - 1018 Capital souscrit soumis à des conditions particulières 
      102 Capital par dotation 
      - 1021 Dotation initiale 
      - 1022 Dotations complémentaires - 1028 Autres dotations 
      103 Capital personnel 
      104 Compte de l’exploitant 
      - 1041 Apports temporaires 
      - 1042 Opérations courantes - 1043 Rémunérations, impôts et autres charges personnelles - 1047 Prélèvements d’autoconsom-mation - 1048 Autres prélèvements 
      105 Primes liées aux capitaux propres 
      - 1051 Primes d’émission 
      - 1052 Primes d’apport - 1053 Primes de fusion - 1054 Primes de conversion - 1058 Autres primes 
      106 Écarts de réévaluation 
      - 1061 Écarts de réévaluation légale 
      - 1062 Écarts de réévaluation libre 
      109 Actionnaires, capital souscrit, non appelé 
    """
    # for m in genai.list_models():
    #     if 'generateContent' in m.supported_generation_methods:
    #         print(m.name)
    response = model.generate_content(
      ["Quelle est le numéro du compte Apports temporaires ", context], stream=False)
    print(response.text)
    