from run import *
valid_pd = pd.read_csv('/home/zhangkechi/workspace/riddle/dataset/valid.csv')
# valid_pd.head()
def mrr_calculate(vecs, ans_vecs, ground_truth,MRR_num = 5):
        scores= np.matmul(vecs,ans_vecs.T)
        sort_ids=np.argsort(scores, axis=-1, kind='quicksort', order=None)[:,::-1]
        index2ans = ground_truth
        index2ans = {i:index2ans[i] for i in range(len(index2ans))}
        predict_words = []
        for i in range(sort_ids.shape[0]):
            this_predict = []
            this_pred_num = 0
            this_ids = sort_ids[i]
            for each_id in this_ids:
                each_label = index2ans[each_id]
                if each_label not in this_predict:
                    this_predict.append(each_label)
                    this_pred_num += 1
                    if this_pred_num > MRR_num:
                        break
            predict_words.append(this_predict)
        mrr_index = []
        for i in range(len(ground_truth)):
            if ground_truth[i] in predict_words[i]:
                mrr_index.append(predict_words[i].index(ground_truth[i]))
            else:
                mrr_index.append(100000000)
            # mrr_index.append(predict_words[i].index(ground_truth[i]))
        mrr_score = [1/(e + 1) for e in mrr_index]
        mrr_score = sum(mrr_score) / len(mrr_score)
        return mrr_score
# mrr_calculate(tmp['vecs'], tmp['ans_vecs'], list(valid_pd['A']))
def calculate_mrr_in_dir(dir_path):
    file2score = {}
    # root_path = '/home/zhangkechi/workspace/riddle/clone_detection/code/run_bert-base-chinese_chaizi_noqq'
    root_path = dir_path
    print(root_path)
    for each_path in tqdm(os.listdir(root_path)):
        if each_path.endswith('vecs.pkl'):
            this_path = os.path.join(root_path, each_path)
            with open(this_path,'rb') as f:
                tmp = pickle.load(f)
            if tmp['vecs'].shape[0] > 10000:
                continue
            mrr_score = mrr_calculate(tmp['vecs'], tmp['ans_vecs'], list(valid_pd['A']))
            file2score[each_path] = mrr_score
    # for k in file2score:
    #     print(k, file2score[k])


    file2score_pair = list(file2score.items())

    file2score_pair.sort(key=lambda x:-x[1])

    print(file2score_pair[:10])
    for i in range(2):
        best_file = file2score_pair[i][0]
        with open(os.path.join(root_path, best_file),'rb') as f:
            tmp = pickle.load(f)
        mrr_1 = mrr_calculate(tmp['vecs'], tmp['ans_vecs'], list(valid_pd['A']),MRR_num=1)
        mrr_3 = mrr_calculate(tmp['vecs'], tmp['ans_vecs'], list(valid_pd['A']),MRR_num=3)
        mrr_5 = mrr_calculate(tmp['vecs'], tmp['ans_vecs'], list(valid_pd['A']),MRR_num=5)
        mrr_10 = mrr_calculate(tmp['vecs'], tmp['ans_vecs'], list(valid_pd['A']),MRR_num=10)
        print("MRR_1:",mrr_1)
        print("MRR_3:",mrr_3)
        print("MRR_5:",mrr_5)
        print("MRR_10:",mrr_10)


# calculate_mrr_in_dir('/home/zhangkechi/workspace/riddle/clone_detection/code/run_bert-base-chinese_chaizi')
# calculate_mrr_in_dir('/home/zhangkechi/workspace/riddle/clone_detection/code/run_bert-base-chinese_chaizi_noqq')
# calculate_mrr_in_dir('/home/zhangkechi/workspace/riddle/clone_detection/code/run_bert-base-chinese_word')
calculate_mrr_in_dir('/home/zhangkechi/workspace/riddle/clone_detection/code/pinyin_and_chaizi_no_pretrain')

# /home/zhangkechi/workspace/riddle/clone_detection/code/run_bert-base-chinese_chaizi
# 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 306/306 [07:39<00:00,  1.50s/it]
# [('1654097326.2874563eval_vecs.pkl', 0.16373784202981048), ('1654100191.789121eval_vecs.pkl', 0.1635188639057229), ('1654102771.6894958eval_vecs.pkl', 0.16329076172506596), ('1654103058.9153852eval_vecs.pkl', 0.16308699041728003), ('1654102485.1360438eval_vecs.pkl', 0.16302920454380085), ('1654102198.2795322eval_vecs.pkl', 0.1629775013698348), ('1654103632.4565012eval_vecs.pkl', 0.16284672278467668), ('1654104490.8069236eval_vecs.pkl', 0.16277677143370342), ('1654100765.1787968eval_vecs.pkl', 0.16264295148783978), ('1654104205.0904415eval_vecs.pkl', 0.16252737970620948)]
# MRR_1: 0.14178832950547968
# MRR_3: 0.15767944819769375
# MRR_5: 0.16373784202981048
# MRR_10: 0.17077412580423315
# /home/zhangkechi/workspace/riddle/clone_detection/code/run_bert-base-chinese_chaizi_noqq
# 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 301/301 [07:12<00:00,  1.44s/it]
# [('1654117330.5990183eval_vecs.pkl', 0.16162105368127028), ('1654134856.2672012eval_vecs.pkl', 0.16143248920803438), ('1654134280.8567832eval_vecs.pkl', 0.16130171062835072), ('1654117042.0420847eval_vecs.pkl', 0.16125000747810736), ('1654119342.8814616eval_vecs.pkl', 0.16121655249392228), ('1654134569.0329876eval_vecs.pkl', 0.16118613884854538), ('1654133993.6867378eval_vecs.pkl', 0.16089720941728022), ('1654118480.7789478eval_vecs.pkl', 0.16079684446107564), ('1654133419.2468162eval_vecs.pkl', 0.16017944785645297), ('1654133131.731564eval_vecs.pkl', 0.1601399101362583)]
# MRR_1: 0.13886862149635557
# MRR_3: 0.15503346279623392
# MRR_5: 0.16162105368127028
# MRR_10: 0.16780795475229565
# /home/zhangkechi/workspace/riddle/clone_detection/code/run_bert-base-chinese_word
# 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 298/298 [06:13<00:00,  1.25s/it]
# [('1654045313.4588826eval_vecs.pkl', 0.008020082846715737), ('1654046558.9198244eval_vecs.pkl', 0.007308404016423765), ('1654040644.4931803eval_vecs.pkl', 0.007183708159975925), ('1654030887.1275816eval_vecs.pkl', 0.0071320049841851274), ('1654037740.015379eval_vecs.pkl', 0.007119839548662116), ('1654046455.1544385eval_vecs.pkl', 0.007110715459245989), ('1654035663.6366918eval_vecs.pkl', 0.0070863845590027124), ('1654046247.7084732eval_vecs.pkl', 0.007080301832117192), ('1654045625.8110464eval_vecs.pkl', 0.007046846851581914), ('1654046662.5889287eval_vecs.pkl', 0.007016433218978391)]
# MRR_1: 0.006569352985401819
# MRR_3: 0.0072536595310223086
# MRR_5: 0.008020082846715737
# MRR_10: 0.008781206793058728