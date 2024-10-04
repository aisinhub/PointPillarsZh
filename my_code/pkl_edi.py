import pickle

# input_file = '/home/data/kitti_infos_val.pkl'  # 入力ファイル名
# output_file = '/home/data/kitti_infos_edi_00_val.pkl'  # 出力ファイル名

input_file = '/home/data_v2/KITTI/kitti_data_PointPillarsZh/kitti_infos_val.pkl'  # 入力ファイル名
output_file = '/home/data_v2/KITTI/kitti_data_PointPillarsZh/pkl_folder/kitti_infos_edi_50_val.pkl'  # 出力ファイル名


# pklファイルの読み込み
with open(input_file, 'rb') as f:
    data = pickle.load(f)

# 1行から80行までのデータを取得
# data_subset = data[:50]
# 辞書から最初の50個のキーを取得(50のシーン)
keys_subset = list(data.keys())[0:50]

# 最初の80個のキーに対応する値を取得
values_subset = [data[key] for key in keys_subset]

# 新しい辞書を作成し、キーと値をセットする
data_subset = {key: value for key, value in zip(keys_subset, values_subset)}



# 新しい名前を付けてデータを保存
with open(output_file, 'wb') as f:
    pickle.dump(data_subset, f) 