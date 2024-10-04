
if [ -z $1 ] || [ -z $2 ] || [ -z $3 ] || [ -z $4 ];then
    echo "useage:bash kitti2ply.sh [bin_path] [save_name] [start_No] [end_No]"
    exit
fi

save_path="./ply/$2"

if [ ! -e $save_path ]; then
    mkdir -p $save_path
    echo "make_dir: $save_path"
fi

for i in $(seq $3 $4); do
    data_no=`printf %06d $i`
    echo $1/$data_no.bin
    python kitti2ply.py $1/$data_no.bin $save_path
done
