import subprocess

data_root = '/home/data'
# ckpt_root = 'my_output/my_pillar_logs/git_ori_160_5freq/checkpoints/'
# ckpt_root = 'my_output/my_pillar_logs/r_var_former_60ep/checkpoints/'
ckpt_root = 'my_output/my_pillar_logs/add_z_r_later_60ep/checkpoints/'
# saved_path_root = 'my_output/my_results/r_var_former_60ep/r_var_later_60ep_{}ep'
saved_path_root = 'my_output/my_results/add_z_r_later_60ep/add_z_r_later_60ep_{}ep'


# 20エポックごとに評価を行うループ
for epoch in range(60, 61, 10):  # range(sta,mid,end)は，mid未満のため161でよい
    ckpt_path = f'{ckpt_root}epoch_{epoch}.pth'
    saved_path = saved_path_root.format(epoch)

    # コマンドの作成
    command = [
        'python3',
        'evaluate_edi.py',
        '--data_root',
        data_root,
        '--ckpt',
        ckpt_path,
        '--saved_path',
        saved_path
    ]

    # コマンドの実行
    try:
        subprocess.run(command, check=True)
        print(f"Epoch {epoch} evaluation completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error encountered while evaluating epoch {epoch}: {e}")
