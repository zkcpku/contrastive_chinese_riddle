MODEL_NAME=ShannonAI/ChineseBERT-base
MODEL_TYPE=chinese_bert
MAX_Q_A_LEN=67
CUDA_VISIBLE_DEVICES=2,3 python run.py \
    --output_dir=./saved_models_chinesebertbase_no_qq \
    --model_type=$MODEL_TYPE \
    --config_name=$MODEL_NAME \
    --model_name_or_path=$MODEL_NAME \
    --tokenizer_name=$MODEL_NAME \
    --do_train \
    --train_data_file=../../dataset/train.csv \
    --eval_data_file=../../dataset/train.csv \
    --test_data_file=../../dataset/train.csv \
    --epoch 30 \
    --block_size $MAX_Q_A_LEN \
    --ans_size $MAX_Q_A_LEN \
    --train_batch_size 256 \
    --eval_batch_size 256 \
    --learning_rate 2e-5 \
    --max_grad_norm 1.0 \
    --evaluate_during_training \
    --PAD_ID 0 \
    --seed 123456 2>&1| tee train_base.log