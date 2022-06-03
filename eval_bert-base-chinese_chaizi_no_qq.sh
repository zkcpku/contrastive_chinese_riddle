MODEL_NAME=bert-base-chinese
MODEL_TYPE=chinese_bert
MAX_Q_A_LEN=185
CUDA_VISIBLE_DEVICES=1,2 python run_with_pretrain.py \
    --output_dir=./run_bert-base-chinese_chaizi_noqq \
    --model_type=$MODEL_TYPE \
    --config_name=$MODEL_NAME \
    --tokenizer_name=$MODEL_NAME \
    --do_test \
    --train_data_file=None \
    --eval_data_file=None \
    --test_data_file=../../dataset/valid.csv.fake.csv.for_seq_only_chaizi.json \
    --epoch 300 \
    --block_size $MAX_Q_A_LEN \
    --ans_size $MAX_Q_A_LEN \
    --train_batch_size 64 \
    --eval_batch_size 64 \
    --learning_rate 2e-5 \
    --max_grad_norm 1.0 \
    --evaluate_during_training \
    --MRR_num 5 \
    --with_qq false \
    --seed 123456 2>&1| tee eval_bert-base-chinese_chaizi_no_qq.log