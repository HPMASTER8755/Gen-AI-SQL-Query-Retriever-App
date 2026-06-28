# 🚀 SQL Query Generator using Gemini AI

An AI-powered SQL Query Generator built with **Streamlit**, **Google Gemini API**, and **SQLite**. This application converts natural language questions into SQL queries using Google's Gemini Large Language Model and executes them on a SQLite database.

---

## 📌 Features

* 🤖 Convert English questions into SQL queries using Gemini AI
* 💾 Execute generated SQL queries on a SQLite database
* 📊 Display query results instantly
* ⚡ Interactive Streamlit web interface
* 🔒 Secure API key management using `.env`
* 🧠 Prompt engineering for accurate SQL generation

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Google Gemini API
* SQLite
* python-dotenv

---

## 📂 Project Structure

```text
sql-query-generator/
│
├── app.py
├── student.db
├── requirements.txt
├── .env
├── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sql-query-generator.git
cd sql-query-generator
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```text
API_KEY=YOUR_GEMINI_API_KEY
```

Generate your API key from Google AI Studio.

### 5. Run the application

```bash
python -m streamlit run app.py
```

---

## 💡 Example Queries

* Show all students.
* Count the total number of students.
* Show students from Data Science class.
* List all students in Section A.
* Show students whose names start with R.
* Count students in each class.
* Display students ordered by name.

---

## 🗃️ Database Schema

**Table Name:** STUDENT

| Column  | Description     |
| ------- | --------------- |
| NAME    | Student Name    |
| CLASS   | Student Class   |
| SECTION | Student Section |

---

## 🔄 Application Workflow

1. User enters a question in plain English.
2. Gemini AI converts the question into an SQL query.
3. The generated SQL query is executed on the SQLite database.
4. The query result is displayed in the Streamlit application.

---

## 📸 Screenshots

Add screenshots of:

* Home Screen
* Generated SQL Query
* Query Results

---

## 📈 Future Enhancements

* Upload custom SQLite databases
* Support multiple database engines (MySQL, PostgreSQL)
* Query explanation using AI
* SQL syntax validation
* Query history
* Export results to CSV or Excel
* Authentication and user management

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork this repository and submit a pull request.

---


## 🌐 Live Demo

https://gen-ai-sql-query-retriever-app-rcxspddepwwdszsecvbhw5.streamlit.app/
