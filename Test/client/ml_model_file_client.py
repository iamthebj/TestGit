"""
To train and test the model
"""
from ml_model import ml_filelevel_model
if __name__ == '__main__':
    MODEL = ml_filelevel_model.FileMLModel()
    DATA_FRAME = MODEL.model_init()
    T = MODEL.data_split(DATA_FRAME)
    MODEL.train_model(T[0], T[2])
    Y_PRED = MODEL.test_model(T[1])
    ACCURACY = MODEL.test_accuracy(T[3], Y_PRED)
