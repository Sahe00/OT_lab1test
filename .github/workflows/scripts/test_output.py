# This is the file that will be executed by the workflow to check the output of the main.py file.

import subprocess

def test_output():
    result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
    output = result.stdout

    assert "Hello from the main branch!" in output, "main() function did not run correctly"
    assert "Hello from the feature1 branch!" in output, "first_feature() function did not run correctly"
    assert "Hello from the feature2 branch!" in output, "second_feature() function did not run correctly"

if __name__ == "__main__":
    test_output()
