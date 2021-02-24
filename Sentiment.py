from transformers import pipeline
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
#
# tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-uncased-sentiment")
#
# model = AutoModelForSequenceClassification.from_pretrained("bert-base-multilingual-uncased-sentiment")
def Sentiment_classifer(text):
#     from transformers import pipeline
      classifier = pipeline('sentiment-analysis', model="bert-base-multilingual-uncased-sentiment")
      results=classifier(text)
      for result in results:
        print(f"label: {result['label']}, with score: {round(result['score'], 4)}")
      return results

print(Sentiment_classifer(["We are very happy to show you the 🤗 Transformers library.",
           "We hope you don't hate it."]))