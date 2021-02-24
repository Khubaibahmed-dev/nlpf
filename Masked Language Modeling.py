from transformers import TFAutoModelWithLMHead, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased")
def masked_lang_fill(sequence,no_of_version):
    from transformers import TFAutoModelWithLMHead, AutoTokenizer
    import tensorflow as tf
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased")
    model = TFAutoModelWithLMHead.from_pretrained("distilbert-base-cased")

    input = tokenizer.encode(sequence, return_tensors="tf")
    mask_token_index = tf.where(input == tokenizer.mask_token_id)[0, 1]
    token_logits = model(input)[0]
    mask_token_logits = token_logits[0, mask_token_index, :]
    top_5_tokens = tf.math.top_k(mask_token_logits, no_of_version).indices.numpy()

    for token in top_5_tokens:
        print(sequence.replace(tokenizer.mask_token, tokenizer.decode([token])))
    return
sequence = f"Distilled models are smaller than the models they mimic. Using them instead of the large versions would help {tokenizer.mask_token} our carbon footprint."

masked_lang_fill(sequence,4)