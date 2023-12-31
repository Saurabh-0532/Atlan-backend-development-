
def answer_to_return_gsheet():
    import sqlite3
    conn = sqlite3.connect('db.sqlite3')

    question_obj = conn.cursor()
    answer_obj = conn.cursor()

    question_obj.execute("SELECT id FROM index_questions")
    ques_id = question_obj.fetchall()
    no_of_ques = len(ques_id)
    answer_for_gsheet = []
    for i in range(0, no_of_ques):
        ques_id_value = ques_id[i][0]
        ans_sql_query = f"SELECT index_answer.answer FROM index_answer WHERE index_answer.answer_to_id = {ques_id_value}"
        answer_obj.execute(ans_sql_query)
        ans_value = answer_obj.fetchall()
        ans_in_tuple = [item[0] for item in ans_value]
        answer_for_gsheet.append(ans_in_tuple)
    final_res = [list(row) for row in zip(*answer_for_gsheet)]
    #print(final_res)
    conn.commit()
    conn.close()
    return final_res

def return_value_sms():
    import sqlite3
    conn = sqlite3.connect('db.sqlite3')

    quest_obj = conn.cursor()
    quest_obj.execute("SELECT id FROM index_questions WHERE question = 'Phone number' or question = 'Phone' or question = 'phone' or question = 'phone no' ")
    ques_ids = quest_obj.fetchall()
    if(len(ques_ids) != 0 ):
        idvalue = ques_ids[0][0]
        
        #print(idvalue)
        answ_obj = conn.cursor()
        ans_query = f"SELECT answer FROM index_answer WHERE answer_to_id = {idvalue}"
        answ_obj.execute(ans_query)
        res = [item[0] for item in answ_obj.fetchall()]
        conn.commit()
        conn.close()
        #print(res[len(res)-1])
        return res[len(res)-1]
    else: 
        return 0


