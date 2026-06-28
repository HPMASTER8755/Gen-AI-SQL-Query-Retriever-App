from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.genai as genai

# genai.configure(api_key=os.getenv("G_API_KEY"))
client = genai.Client(api_key=os.getenv("API_KEY"))

# ## Define Your Prompt
# prompt="""
#     You are an expert in converting English questions to SQL query!
#     The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
#     SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
#     the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
#     \nExample 2 - Tell me all the students studying in Data Science class?, 
#     the SQL command will be something like this SELECT * FROM STUDENT 
#     where CLASS="Data Science"; 
#     also the sql code should not have ``` in beginning or end and sql word in output

#     """

# def get_gemini_response(question,prompt):
#     model=genai.GenerativeModel('gemini-1.5-flash')
#     # response=model.generate_content([prompt,question])
#     response = model.generate_content(
#     f"{prompt}\n\n{question}"
# )
    # return response.text

def get_gemini_response(question, prompt):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
{prompt}

User Question:
{question}

Only return SQL query.
Do not return markdown.
Do not return explanation.
"""
    )

    return response.text.strip()

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt = """
You are an expert in converting English questions into SQL queries.

Database Name: STUDENT

Columns:
- NAME
- CLASS
- SECTION

Example:

Question:
How many entries are present?

SQL:
SELECT COUNT(*) FROM STUDENT;

Question:
Tell me all students studying in Data Science class.

SQL:
SELECT * FROM STUDENT WHERE CLASS='Data Science';

Return ONLY SQL.
"""


## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)
