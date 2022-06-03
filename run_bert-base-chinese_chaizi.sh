MODEL_NAME=bert-base-chinese
MODEL_TYPE=chinese_bert
MAX_Q_A_LEN=185
CUDA_VISIBLE_DEVICES=2,3 python run_with_pretrain.py \
    --output_dir=./run_bert-base-chinese_chaizi \
    --model_type=$MODEL_TYPE \
    --config_name=$MODEL_NAME \
    --tokenizer_name=$MODEL_NAME \
    --do_train \
    --train_data_file=../../dataset/train.csv.for_seq_only_chaizi.json \
    --eval_data_file=../../dataset/valid.csv.for_seq_only_chaizi.json \
    --test_data_file=../../dataset/valid.csv.for_seq_only_chaizi.json \
    --epoch 300 \
    --block_size $MAX_Q_A_LEN \
    --ans_size $MAX_Q_A_LEN \
    --train_batch_size 64 \
    --eval_batch_size 64 \
    --learning_rate 2e-5 \
    --max_grad_norm 1.0 \
    --evaluate_during_training \
    --MRR_num 100 \
    --seed 123456 2>&1| tee run_bert-base-chinese_chaizi.log