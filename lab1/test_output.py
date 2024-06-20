from lab1.main import main_msg, first_feature, second_feature

def test_main():
    assert main_msg() == "Hello from the main branch!"

def test_first_feature():
    assert first_feature() == "Hello from the feature1 branch!"

def test_second_feature():
    assert second_feature() == "Hello from the feature2 branch!"




