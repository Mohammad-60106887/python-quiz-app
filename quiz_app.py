import tkinter as tk
from tkinter import messagebox

# --------------------------
# 1) Define All Questions
# --------------------------
all_questions = [
    # ---------- 3 Loops Questions ----------
    {
        "topic": "Loops",
        "question": "Q1: What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 0
    },
    {
        "topic": "Loops",
        "question": "Q2: How many times will 'Hello' be printed?",
        "code": "count = 0\nwhile count < 3:\n    print('Hello')\n    count += 1",
        "options": ["2", "3", "infinite", "0"],
        "answer": 1
    },
    {
        "topic": "Loops",
        "question": "Q3: Which of these for-loops iterates over a dict's keys?",
        "code": "my_dict = {'a':1, 'b':2}\nfor k in my_dict:\n    print(k)",
        "options": [
            "for k in my_dict:",
            "for k in my_dict.keys():",
            "for k, v in my_dict.items():",
            "Both 1 and 2 are correct."
        ],
        "answer": 3
    },

    # ---------- 3 Lists Questions ----------
    {
        "topic": "Lists",
        "question": "Q1: What will be the value of my_list after .insert(1,100)?",
        "code": "my_list = [1, 2, 3]\nmy_list.insert(1, 100)\nprint(my_list)",
        "options": [
            "[1, 100, 2, 3]",
            "[100, 1, 2, 3]",
            "[1, 2, 100, 3]",
            "Error"
        ],
        "answer": 0
    },
    {
        "topic": "Lists",
        "question": "Q2: What is printed by my_list[-1]?",
        "code": "my_list = ['a', 'b', 'c']\nprint(my_list[-1])",
        "options": ["a", "b", "c", "Error"],
        "answer": 2
    },
    {
        "topic": "Lists",
        "question": "Q3: Which method removes the last element of a list?",
        "code": "my_list = [1, 2, 3, 4]\n# ???\nprint(my_list)",
        "options": ["remove()", "pop()", "discard()", "push()"],
        "answer": 1
    },

    # ---------- 3 Strings Questions ----------
    {
        "topic": "Strings",
        "question": "Q1: What does this code print?",
        "code": 's = "Hello"\nprint(s[1:4])',
        "options": ["Hell", "ell", "llo", "He"],
        "answer": 1
    },
    {
        "topic": "Strings",
        "question": "Q2: Which function converts a string to lowercase in Python?",
        "code": 's = "HELLO"\n# ???\nprint(s)',
        "options": ["s.lower()", "s.capitalize()", "s.downcase()", "s.to_lower()"],
        "answer": 0
    },
    {
        "topic": "Strings",
        "question": "Q3: What is printed here?",
        "code": 's = "python"\nprint(s*2)',
        "options": ["python", "pythonpython", "error", "2"],
        "answer": 1
    }
]

# --------------------------
# 2) Create Main Window
# --------------------------
root = tk.Tk()
root.title("Python Quiz Generator")

# Make window a bit bigger and set a background color
root.geometry("640x480")
root.config(bg="#F3F4F6")  # a light grey/blue background

# Global variables that get set once a user chooses a topic
filtered_questions = []
current_index = 0
topic_score = 0
selected_option = tk.IntVar()

# --------------------------
# 3) Helper Functions
# --------------------------
def generate_topic_questions():
    """
    When the user clicks "Generate Python Question",
    filter all_questions by the topic in topic_entry,
    then display the first question of that topic.
    """
    global filtered_questions, current_index, topic_score
    
    user_topic = topic_entry.get().strip()
    if not user_topic:
        messagebox.showinfo("Info", "Please enter a Python topic.")
        return
    
    filtered_questions = [q for q in all_questions if q["topic"].lower() == user_topic.lower()]
    
    if not filtered_questions:
        messagebox.showinfo("Info", f"No questions found for topic '{user_topic}'.")
        return
    
    current_index = 0
    topic_score = 0
    display_question()

def display_question():
    """Show the question, code snippet, and answer choices for filtered_questions[current_index]."""
    if not filtered_questions:
        return
    
    q = filtered_questions[current_index]
    question_label.config(
        text=f"Topic: {q['topic']}\n\n{q['question']}",
        fg="#1F2937"  # dark gray text
    )
    code_label.config(text=q["code"])
    feedback_label.config(text="")

    selected_option.set(-1)  # reset radio selection
    for i, option_text in enumerate(q["options"]):
        radio_buttons[i].config(text=option_text, value=i)

def check_answer_and_next():
    """
    Check if the selected answer is correct, update topic_score,
    then move to the next question (or show final score if done).
    """
    global current_index, topic_score
    
    if not filtered_questions:
        messagebox.showinfo("Info", "No questions loaded. Please enter a topic and click 'Generate'.")
        return
    
    if selected_option.get() == -1:
        messagebox.showinfo("Select an Option", "Please select an answer before submitting.")
        return
    
    q = filtered_questions[current_index]
    if selected_option.get() == q["answer"]:
        topic_score += 1
        feedback_label.config(text="Correct! Well done! 🎉", fg="#059669")  # green
    else:
        feedback_label.config(text="Incorrect.", fg="#DC2626")  # red
    
    root.after(1000, next_question)

def next_question():
    """Advance current_index or show the user their final score for this topic."""
    global current_index
    current_index += 1
    
    if current_index >= len(filtered_questions):
        # All done for this topic
        messagebox.showinfo(
            "Topic Complete",
            f"You finished all questions for {filtered_questions[0]['topic']}.\n"
            f"Score: {topic_score} / {len(filtered_questions)}"
        )
        # Clear question area so user can pick a new topic
        question_label.config(text="")
        code_label.config(text="")
        feedback_label.config(text="")
        for rb in radio_buttons:
            rb.config(text="", value=-1)
        return
    
    display_question()

# --------------------------
# 4) GUI Layout
# --------------------------

# -- 4A) A Title / Heading at the very top --
title_label = tk.Label(
    root,
    text="Welcome to the Python Quiz App",
    font=("Arial", 16, "bold"),
    bg="#A5B4FC",  # pastel purple
    fg="#1E3A8A"   # darker blue text
)
title_label.pack(fill="x", pady=5)

# -- 4B) Frame for topic entry and button --
top_frame = tk.Frame(root, bg="#E0F2FE")
top_frame.pack(fill="x", pady=10, padx=10)

tk.Label(
    top_frame,
    text="Enter Python Topic (e.g., Loops, Lists, Strings):",
    bg="#E0F2FE",
    font=("Arial", 10, "bold")
).pack(side=tk.LEFT, padx=(5, 2))

topic_entry = tk.Entry(top_frame, width=20, font=("Arial", 10))
topic_entry.pack(side=tk.LEFT, padx=5)

generate_button = tk.Button(
    top_frame,
    text="Generate Python Question",
    command=generate_topic_questions,
    bg="#93C5FD",
    fg="black",
    font=("Arial", 10, "bold")
)
generate_button.pack(side=tk.LEFT, padx=5)

# -- 4C) Frame for the question display --
question_frame = tk.Frame(root, bg="#F3F4F6")
question_frame.pack(fill="both", expand=True, padx=10, pady=5)

question_label = tk.Label(
    question_frame,
    text="",
    wraplength=500,
    justify="left",
    font=("Arial", 12, "bold"),
    bg="#F3F4F6",
    fg="#1F2937"
)
question_label.pack(pady=(10, 5))

# -- 4D) Frame for code snippet (styled differently) --
code_frame = tk.Frame(root, bg="#EDE9FE", bd=2, relief=tk.GROOVE)
code_frame.pack(fill="x", padx=10, pady=5)

code_label = tk.Label(
    code_frame,
    text="",
    font=("Courier", 10),
    fg="#4C1D95",      # deep purple
    bg="#EDE9FE",
    justify="left"
)
code_label.pack(pady=5, padx=5)

# -- 4E) Radio buttons for answer choices in a separate frame --
options_frame = tk.Frame(root, bg="#F3F4F6")
options_frame.pack(fill="x", padx=20, pady=5)

radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(
        options_frame,
        text="",
        variable=selected_option,
        value=i,
        font=("Arial", 10),
        wraplength=500,
        bg="#F3F4F6",
        fg="#1F2937",
        activebackground="#F3F4F6",
        anchor="w",
        justify="left"
    )
    rb.pack(anchor="w", pady=2)
    radio_buttons.append(rb)

# -- 4F) Feedback label and Submit button --
feedback_label = tk.Label(
    root,
    text="",
    font=("Arial", 10, "bold"),
    bg="#F3F4F6"
)
feedback_label.pack(pady=5)

submit_button = tk.Button(
    root,
    text="Submit / Next",
    command=check_answer_and_next,
    bg="#FCA5A5",
    fg="black",
    font=("Arial", 10, "bold")
)
submit_button.pack(pady=5)

# --------------------------
# 5) Start the Event Loop
# --------------------------
root.mainloop()
