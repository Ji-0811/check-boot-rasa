import os
import re
import random

#构建语料写入txt
def get_value(intent):
    keys = random.choice(list(intent))  # 从一个字典中随机获取key
    # print('keys:', keys)
    value_list = intent[f'{keys}']  # 获取key对应的值-->列表形式
    # print('values_list:', value_list)
    value_sentence = random.choice(value_list) #从列表中随机获取一个字符串
    # print('value_sentense:', value_sentence)
    with open('dict_sentence_entity'+'\\'+keys+'_sentence.txt','a',encoding='utf-8') as rewrite: #单种实体类别分别存放txt
        rewrite.write('- 'f'{value_sentence}'+'\n')
    with open('all_dict_sentence_entity.txt', 'a', encoding='utf-8') as alwrite: #所有实体类别
        alwrite.write('- 'f'{value_sentence}'+'\n')

#构建语料模板
def nlu_sentence(data,entity):
    data = data.replace('\n','')
    if entity=='Disease':
        Disease_intent = {'disease_desc':[f'{data}是什么',f'{data}解释',f'介绍{data}',f'{data}是什么病',f'{data}相关说明'],
                  'disease_cause':[f'{data}病因',f'{data}由什么引起的',f'{data}怎么引起的',f'{data}怎么回事',f'什么导致的{data}',f'为什么会得{data}'],
                  'disease_prevent':[f'{data}预防措施',f'怎样预防{data}',f'预防{data}',f'怎样才能不得{data}'],
                  'disease_lasttime':[f'{data}持续时间',f'{data}多久才能好',f'{data}治疗时间',f'{data}需要多久'],
                  'disease_cureprob':[f'{data}治愈率是多少',f'{data}治愈率',f'{data}活的机率',f'{data}能治好吗',f'{data}能不能治好'],
                  'disease_cureway':[f'{data}治疗方式',f'{data}治疗方法',f'{data}怎样治疗',f'治疗{data}'],
                  'disease_easyget':[f'{data}易发人群',f'{data}什么人容易得'],
                  'disease_symptom':[f'{data}症状',f'{data}有哪些症状',f'{data}表现'],
                  'disease_acompany':[f'{data}并发症',f'{data}能引发什么病',f'{data}有哪些并发症'],
                  'disease_not_food':[f'{data}不能吃什么',f'{data}需要对什么忌口',f'{data}忌口',f'{data}什么不能吃',f'{data}最好不要吃些什么'],
                  'disease_do_food':[f'{data}能吃什么',f'{data}推荐吃什么',f'{data}多吃些什么'],
                  'disease_drug':[f'{data}吃什么药',f'什么药治{data}这个病',f'什么药解决{data}'],
                  'disease_check':[f'{data}做什么检查',f'{data}检查什么',f'{data}怎么检查'],
        }
        get_value(Disease_intent)

    elif entity=='Food':
        Food_initent = {
            'food_not_disease': [f'哪些人不能吃{data}',f'什么人最好不要吃{data}',f'什么人不能吃{data}'],
            'food_do_disease': [f'吃{data}有什么好处',f'吃{data}对什么人好',f'{data}哪些人适合多吃'],
        }
        get_value(Food_initent)
    elif entity == 'Drug':
        Drug_initent = {'drug_disease': [f'{data}能治什么病',f'{data}治什么病']}
        get_value(Drug_initent)
    elif entity == 'Symptom':
        Symptom_initent = {'symptom_disease':[f'{data}怎么了',f'{data}怎么回事',f'{data}得了什么病',f'为什么{data}']}
        get_value(Symptom_initent)
    elif entity == 'Check':
        Check_initent = {'check_disease':[f'{data}能查什么病',f'什么病需要检查{data}',f'检查{data}',f'查{data}',f'{data}能查出啥来']}
        get_value(Check_initent)


if __name__ == '__main__':
    patch = os.listdir('dict') #获取目录下所有的文件名有后缀
    print('Getting all folder names ...')
    # print(patch) #['Check.txt', 'Deny.txt', 'Department.txt', 'Disease.txt', 'Drug.txt', 'Food.txt', 'Producer.txt', 'Symptom.txt']
    entity_list = []
    print('Writing to file ...')
    for i in range(len(patch)): #循环每个文件
        # print(patch[i]) #带后缀的每个文件夹名称
        filename = re.findall(r'(.+?)\.txt',patch[i].strip())[0] #获取文件名称不带后缀（实体类型）
        # print(filename)
        entity_list.append(filename) #将所有实体名称存入列表
        with open('dict'+'\\' + patch[i],'r',encoding='utf-8') as f:
            for data in f.readlines():#按行读取数据
                line = data.strip('\n')  # 除去每行的换行符
                # print(line)
                with open('dict_entity'+'\\'+filename+'_entity.txt','a',encoding='utf-8') as rewrite: #单种实体类别分别存放txt
                    rewrite.write('- ['+line+']'+'('+filename+')'+'\n')
                with open('all_dict_entity.txt', 'a', encoding='utf-8') as alwrite: #所有实体类别
                    alwrite.write('['+line+']'+'('+filename+')'+'\n')

                sentence = f'['+line+']'+'('+filename+')'
                nlu_sentence(sentence,filename)

    print('Perform the end')