# テキストファイルからデータを読み込む
with open('test_val.txt', 'r') as file:
    data = file.read()

# 読み込んだデータをPythonオブジェクトに変換する
# parsed_data = parse_text_data(data)

# pickleを使用してpklファイルにデータを保存する
import pickle
with open('test_val.pkl', 'wb') as file: # write 書き込み binary バイナリモードからwb
    pickle.dump(data, file)


# import argparse
# import pickle


# def main(args):
#     # テキストファイルからデータを読み込む
#     with open(args.txt_data, 'r') as file:
#         data = file.read()
#     # 読み込んだデータをPythonオブジェクトに変換する
#     parsed_data = parse_text_data(data)
    

#     # pickleを使用してpklファイルにデータを保存する
#     with open(args.output, 'wb') as file:  # write 書き込み binary バイナリモードからwb
#         pickle.dump(parsed_data, file)

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Convert text data to pickle')
#     parser.add_argument('--txt_data', type=str, help='Path to the text data file')
#     parser.add_argument('--output', type=str, help='Path to save the output pickle file')
#     args = parser.parse_args()

#     main(args)