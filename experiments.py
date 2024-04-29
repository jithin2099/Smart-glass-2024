from subprocess import call

def call_python_file():
    call(["python", "recognizer_attempt1.py"])

print("Calling Python File")

call_python_file()

print("Python file has been called")