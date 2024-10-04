import sys

# 標準出力を一時的にファイルにリダイレクト
with open('output.txt', 'w') as f:
    sys.stdout = f

# ここからのprint文はoutput.txtに保存されます
print('これはファイルに保存されるテキストです。')

# リダイレクトを元に戻す
sys.stdout = sys.__stdout__