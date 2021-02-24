def paraphrase(sequence_0,sequence_1):
    from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
    import tensorflow as tf
    tokenizer = AutoTokenizer.from_pretrained("bert-base-cased-finetuned-mrpc")
    model = TFAutoModelForSequenceClassification.from_pretrained("bert-base-cased-finetuned-mrpc")
    classes = ["not paraphrase", "is paraphrase"]
    # sequence_0 = "The company HuggingFace is based in New York City"
    # sequence_1 = "Apples are especially bad for your health"
    sequence_2 = "HuggingFace's headquarters are situated in Manhattan"
    paraphrase = tokenizer(sequence_0, sequence_1, return_tensors="tf")
    not_paraphrase = tokenizer(sequence_0, sequence_1, return_tensors="tf")
    paraphrase_classification_logits = model(paraphrase)[0]
    not_paraphrase_classification_logits = model(not_paraphrase)[0]
    paraphrase_results = tf.nn.softmax(paraphrase_classification_logits, axis=1).numpy()[0]
    # not_paraphrase_results = tf.nn.softmax(not_paraphrase_classification_logits, axis=1).numpy()[0]
    # Should be paraphrase
    for i in range(len(classes)):
        print(f"{classes[i]}: {int(round(paraphrase_results[i] * 100))}%")
    # Should not be paraphrase
    # for i in range(len(classes)):
    #     print(f"{classes[i]}: {int(round(not_paraphrase_results[i] * 100))}%")
    return

sequence_0 = "The company HuggingFace is based in New York City"
sequence_1 = "Apples are especially bad for your health"

paraphrase(sequence_0,sequence_1)