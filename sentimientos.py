import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

datos = pd.read_csv("./amazon.csv")
df = pd.DataFrame(datos)
all_reviews = datos ['Sentence']
all_sent_values , all_sentimentes = [], []

def sentiment_values(sentencia):
    analizador = SentimentIntensityAnalyzer()
    resultado analizador.polarity_scores(sentencia)
    socre = resultado['compound']
    return round(score, 1)

datos_tem = datos.copy()
for intem in range(0, 1000):
    all_sent_values.append(sentiment_values(all_reviews[intem]))

sentimiento, valor_sent = [], []

for i in range (0, 1000):
    sent =  all_sent_values[i]
    if sent <= 1 and sent > 0 :
        valor_sent.append('Positivo')
    elif 0 == sent:
        valor_sent.append('Neutral')
    else:
        valor_sent.append('Negativo')
