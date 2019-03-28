::这里设置SSD训练参数
::--checkpoint_path=${CHECKPOINT_PATH}^
::数据集的flag--max_number_of_steps=5000训练最大步数
set DATASET_DIR=C:\Users\lxr\Desktop\CCTSDB-TF
set TRAIN_DIR=../logs/ssd_300_vgg_3
set CHECKPOINT_PATH=./checkpoints/ssd_300_vgg.ckpt
python ../train_ssd_network.py^
    --train_dir=%TRAIN_DIR%^
    --dataset_dir=%DATASET_DIR%^
    --dataset_name=pascalvoc_2007^
    --dataset_split_name=train^
    --model_name=ssd_300_vgg^
    --save_summaries_secs=60^
    --save_interval_secs=600^
    --weight_decay=0.0005^
    --optimizer=adam^
    --learning_rate=0.001^
    --learning_rate_decay_factor=0.95^
    --batch_size=32^
    --max_number_of_steps=5000

