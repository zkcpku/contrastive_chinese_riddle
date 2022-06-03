MODEL_NAME=./pinyin_and_chaizi_no_pretrain_config.json
MODEL_TYPE=roberta
MAX_Q_A_LEN=260
CUDA_VISIBLE_DEVICES=4,5 python run_with_nopretrain.py \
    --output_dir=./pinyin_and_chaizi_no_pretrain_no_qq \
    --model_type=$MODEL_TYPE \
    --config_name=$MODEL_NAME \
    --tokenizer_name=$MODEL_NAME \
    --do_train \
    --train_data_file=../../dataset/train.csv.for_seq.json \
    --eval_data_file=../../dataset/valid.csv.for_seq.json \
    --test_data_file=../../dataset/valid.csv.for_seq.json \
    --epoch 30 \
    --block_size $MAX_Q_A_LEN \
    --ans_size $MAX_Q_A_LEN \
    --train_batch_size 256 \
    --eval_batch_size 256 \
    --learning_rate 2e-5 \
    --max_grad_norm 1.0 \
    --evaluate_during_training \
    --PAD_ID 1 \
    --vocab_size 7500 \
    --MRR_num 100 \
    --seed 123456 2>&1| tee pinyin_and_chaizi_no_pretrain_no_qq.log