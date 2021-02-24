def sentence_gramticaly(test_text):
    import torch
    from transformers import BertTokenizer
    from transformers import BertForSequenceClassification
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


    output_dir = './model_save/'
    # Load a trained model and vocabulary that you have fine-tuned
    model = BertForSequenceClassification.from_pretrained(output_dir,)
    tokenizer = BertTokenizer.from_pretrained(output_dir)

    # Copy the model to the GPU/cpu.
    model.to(device)
    model.eval()

    predict_input_pt = tokenizer.encode(test_text,
                                     truncation=True,
                                     padding=True,
                                     return_tensors="pt")
    output_pt = model(predict_input_pt)[0]

    predictions_value_pt = torch.argmax(output_pt[0], dim=-1).item()
    print(predictions_value_pt)

    if predictions_value_pt == 0:
        predictions_value_pt = 'Sentence is Grammatically correct'
        print(predictions_value_pt)

    elif predictions_value_pt == 1:
        predictions_value_pt = 'Sentence is Grammatically correct'
        print(predictions_value_pt)
    return predictions_value_pt

test_text="A compact pico-second in-situ sensor using programmable ring oscillators for advanced on chip variation characterization in 28nm HKMG"

sentence_gramticaly(test_text)