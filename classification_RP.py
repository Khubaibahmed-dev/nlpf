def Research_paper_classification(rp_title):
    import torch
    
    from transformers import BertTokenizer
    
    from transformers import BertForSequenceClassification
    
    model_name = "bert-base-uncased"
    
    # rp_title="A compact pico-second in-situ sensor using programmable ring oscillators for advanced on chip variation characterization in 28nm HKMG"
    save_directory = "/data_volume/finetuned_BERT_epoch_1.model"
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForSequenceClassification.from_pretrained("bert-base-uncased",
                                                          num_labels=5,
                                                          output_attentions=False,
                                                          output_hidden_states=False)

    predict_input_pt = tokenizer.encode(rp_title,
                                     truncation=True,
                                     padding=True,
                                     return_tensors="pt")
    # loaded_model_pt = BertForSequenceClassification.from_pretrained(save_directory, from_tf=True)
    model.load_state_dict(torch.load('data_volume/finetuned_BERT_epoch_1.model', map_location=torch.device('cpu')))
    model.eval()
    output_pt = model(predict_input_pt)[0]
    
    predictions_value_pt = torch.argmax(output_pt[0], dim=-1).item()
    print(predictions_value_pt)
    if predictions_value_pt == 0:
        predictions_value_pt = 'VLDB'
        print(predictions_value_pt)
    elif predictions_value_pt == 1:
        predictions_value_pt = 'ISCAS'
        print(predictions_value_pt)
    elif predictions_value_pt == 2:
        predictions_value_pt = 'SIGGRAPH'
        print(predictions_value_pt)
    elif predictions_value_pt == 3:
        predictions_value_pt = 'INFOCOM'
        print(predictions_value_pt)
    elif predictions_value_pt == 4:
        predictions_value_pt = 'WWW'
        print(predictions_value_pt)
    else:
        print("please enter correct title")
    return predictions_value_pt

rp_title="A compact pico-second in-situ sensor using programmable ring oscillators for advanced on chip variation characterization in 28nm HKMG"


Research_paper_classification(rp_title)