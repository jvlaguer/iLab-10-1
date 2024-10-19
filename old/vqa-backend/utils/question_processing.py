from transformers import RobertaTokenizer

tokenizer = RobertaTokenizer.from_pretrained('roberta-base')

def preprocess_question(question):
    """
    Tokenizes and preprocesses the question using RoBERTa tokenizer.
    :param question: Input question as a string
    :return: Tokenized question
    """
    tokens = tokenizer(question, return_tensors='pt', padding=True, truncation=True)
    return tokens
