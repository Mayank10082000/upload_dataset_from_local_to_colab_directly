from google.colab import files
uploaded = files.upload()

for filename in uploaded.keys():
    print(f'User uploaded file "{filename}" with size {uploaded[filename].size} bytes')