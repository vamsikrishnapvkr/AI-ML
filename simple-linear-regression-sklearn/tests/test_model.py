from src.train import train_model
from src.predict import predict


def test_training_and_prediction():
    model = train_model()

    result = predict(5)

    assert result > 0
    assert isinstance(result, float)