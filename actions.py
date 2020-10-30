from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, UserUtteranceReverted, ConversationPaused
import api
from answer_search import AnswerSearcher
import pandas as pd

class Action_a(Action):
    def name(self):
        return "action_diseases"
    def get_data(self,dispatcher,tracker,domain):
        slot_dict = tracker.current_slot_values()
        print('slotdict================>>', slot_dict, '=====================')
        # slot_list =list(slot_dict.keys())
        # print('slotdict================>>', slot_list, '=====================')
        df = pd.DataFrame(list(slot_dict.values())) #获取所有插槽对应的值
        value = df.dropna(axis=0).values[0][0] #去掉None 获取实体
        Node_label = list(slot_dict.keys())[list(slot_dict.values()).index(f"{value}")] #获取label
        print('Node_label=============>>',Node_label,'=================')
        res_sql = []
        sql = {}
        sentence = tracker.latest_message['intent']
        print('sentence================>>', sentence, '=====================')
        # 获取意图
        intent = tracker.latest_message['intent'].get('name')
        print('intent==================>>', intent, '=========================')
        a = ''.join(tracker.get_slot(f'{Node_label}')).replace(' ', '')
        if not a:
            dispatcher.utter_message('蒽..你说得这个,等我回去查查资料明天再告诉你吧~')
        print('entity==================>>', a, '=========================')
        sql['question_type'] = intent
        print('sql列表=================>>', sql, '=======================')
        res = api.sql_transfer(intent, [a])
        print('res=====================>>', res, '=======================')
        if res:
            sql['sql'] = res
            res_sql.append(sql)
        return res_sql

    def run(self,dispatcher,tracker,domain):
        res_sql = self.get_data(dispatcher,tracker,domain)
        searcher = AnswerSearcher()
        final_answers = searcher.search_main(res_sql)
        print('final_answers===========>>',final_answers,'===========')
        if not final_answers:
            dispatcher.utter_message('蒽..你说得这个,等我回去查查资料明天再告诉你吧~')
        else:
            dispatcher.utter_message(final_answers)
        return []