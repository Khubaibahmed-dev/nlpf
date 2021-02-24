def Sentiment(text):
    from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
    from transformers import pipeline
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    tf_model = TFAutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    classifier = pipeline('sentiment-analysis', model=tf_model, tokenizer=tokenizer)
    results = classifier(text)
    for result in results:
        print(f"label: {result['label']}, with score: {round(result['score'], 4)}")
    return results

print(Sentiment(["We are very happy to show you the 🤗 Transformers library.",
               "We hope you don't hate it."]))
