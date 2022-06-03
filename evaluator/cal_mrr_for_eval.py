import pandas as pd
def cal_mrr(predicts, ans, MRR_NUM = 5):
    assert len(predicts) == len(ans)
    assert len(predicts[0]) >= MRR_NUM
    predicts = [e[:MRR_NUM] for e in predicts]
    mrr_index = []
    for i in range(len(predicts)):
        if ans[i] in predicts[i]:
            mrr_index.append(predicts[i].index(ans[i]))
        else:
            mrr_index.append(1000000)
    mrr_score = [1 / (e + 1) for e in mrr_index]
    return sum(mrr_score) / len(mrr_score)


def calculate_for_valid(output_path, valid_csv_path):
    df = pd.read_csv(valid_csv_path)
    ground_truth = df['A'].tolist()

    with open(output_path, 'r') as f:
        predicts = f.readlines()
    predicts = [e.strip().split() for e in predicts]

    mrr_nums = [1,3,5]
    for mrr_num in mrr_nums:
        mrr = cal_mrr(predicts, ground_truth, MRR_NUM = mrr_num)
        print('MRR@{} = {}'.format(mrr_num, mrr))

if __name__ == '__main__':
    calculate_for_valid('/home/zhangkechi/workspace/riddle/clone_detection/code/run_bert-base-chinese_chaizi_noqq/checkpoint-for-final/output.txt','/home/zhangkechi/workspace/riddle/dataset/valid.csv'
    )