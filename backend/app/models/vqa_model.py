import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.regularizers import l2

# Define the VQAModel class with Keras model
class VQAModel(tf.keras.Model):
    def __init__(self, trainable=True, **kwargs):  # Accept 'trainable' and other kwargs
        super(VQAModel, self).__init__(**kwargs)
        self.trainable = trainable  # You can choose to use or ignore this
        self.dense1 = Dense(512, activation='relu', kernel_regularizer=l2(0.01))
        self.dropout = Dropout(0.5)
        self.flatten = Flatten()
        self.dense2 = Dense(2, activation='softmax')

    def call(self, inputs):
        x = self.dense1(inputs)
        x = self.dropout(x)
        x = self.flatten(x)
        return self.dense2(x)

    def get_config(self):
        config = super(VQAModel, self).get_config()
        config.update({"trainable": self.trainable})
        return config

# Function to load the Keras model
def get_model(model_path):
    model = tf.keras.models.load_model(model_path, custom_objects={'VQAModel': VQAModel})
    return model

# Function to load the tokenizer
def get_tokenizer(tokenizer_path='roberta-base'):
    tokenizer = RobertaTokenizer.from_pretrained(tokenizer_path)
    return tokenizer
