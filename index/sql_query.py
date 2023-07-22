
def answer_to_return_gsheet():
    import sqlite3
    conn = sqlite3.connect('db.sqlite3')

    ''''c = conn.cursor()
    d = conn.cursor()
    d.execute("SELECT id FROM index_questions")
    f = d.fetchall()
    print(len(f))
    x = int(f[0][0])
    print(x)
    sql_query = f"SELECT index_answer.answer FROM index_answer WHERE index_answer.answer_to_id = {x}"
    #c.execute("SELECT index_answer.answer FROM index_answer WHERE  index_answer.answer_to_id == {x}")
    c.execute(sql_query)
    res =c.fetchall()
    for i in range(0,5):
        print(res[i][0])'''
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
    print(final_res)
    conn.commit()
    conn.close()
    return final_res

