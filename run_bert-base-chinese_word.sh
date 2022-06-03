MODEL_NAME=bert-base-chinese
MODEL_TYPE=chinese_bert
MAX_Q_A_LEN=65
CUDA_VISIBLE_DEVICES=4,5 python run_with_pretrain.py \
    --output_dir=./run_bert-base-chinese_word \
    --model_type=$MODEL_TYPE \
    --config_name=$MODEL_NAME \
    --tokenizer_name=$MODEL_NAME \
    --do_train \
    --train_data_file=../../dataset/train.csv.for_seq_only_word.json \
    --eval_data_file=../../dataset/valid.csv.for_seq_only_word.json \
    --test_data_file=../../dataset/valid.csv.for_seq_only_word.json \
    --epoch 300 \
    --block_size $MAX_Q_A_LEN \
    --ans_size $MAX_Q_A_LEN \
    --train_batch_size 128 \
    --eval_batch_size 128 \
    --learning_rate 2e-5 \
    --max_grad_norm 1.0 \
    --evaluate_during_training \
    --MRR_num 100 \
    --seed 123456 2>&1| tee run_bert-base-chinese_word.log