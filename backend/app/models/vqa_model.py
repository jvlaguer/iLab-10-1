import tensorflow as tf
from transformers import RobertaTokenizer
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.regularizers import l2

# Define the VQAModel class with Keras model
class VQAModel(tf.keras.Model):
    def __init__(self, **kwargs):  # Accept **kwargs to handle additional arguments like 'trainable'
        super(VQAModel, self).__init__(**kwargs)
        self.dense1 = Dense(512, activation='relu', kernel_regularizer=l2(0.01))
        self.dropout = Dropout(0.5)
        self.flatten = Flatten()
        self.dense2 = Dense(2, activation='softmax')

    def call(self, inputs):
        x = self.dense1(inputs)
        x = self.dropout(x)
        x = self.flatten(x)
        return self.dense2(x)

    # Optional: Implement get_config if you plan to save the model config
    def get_config(self):
        config = super(VQAModel, self).get_config()
        return config

# Function to load the Keras model
def get_model(model_path=None):
    if model_path:
        # Use custom_objects to map the VQAModel class
        model = tf.keras.models.load_model(model_path, custom_objects={'VQAModel': VQAModel})
        return model
    else:
        # Create a new instance if model_path is not provided
        model = VQAModel()
        return model

# Function to load the tokenizer
def get_tokenizer(tokenizer_path='roberta-base'):
    tokenizer = RobertaTokenizer.from_pretrained(tokenizer_path)
    return tokenizer
