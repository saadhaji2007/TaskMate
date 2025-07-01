import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QListWidget, QPushButton, QLineEdit, QMessageBox, QInputDialog
)

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.conn = sqlite3.connect("todo.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 400, 500)

        self.layout = QVBoxLayout()

        # Search field
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Search task...")
        self.search_input.textChanged.connect(self.search_task)
        self.layout.addWidget(self.search_input)

        # Task input field
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter a new task...")
        self.layout.addWidget(self.task_input)

        # Task list
        self.task_list = QListWidget(self)
        self.layout.addWidget(self.task_list)

        # Buttons Layout
        btn_layout = QHBoxLayout()
        self.add_btn = QPushButton("Add Task")
        self.edit_btn = QPushButton("Edit Task")
        self.remove_btn = QPushButton("Remove Task")
        self.complete_btn = QPushButton("Mark as Done")

        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.edit_btn)
        btn_layout.addWidget(self.remove_btn)
        btn_layout.addWidget(self.complete_btn)

        self.layout.addLayout(btn_layout)
        self.setLayout(self.layout)

        # Button Actions
        self.add_btn.clicked.connect(self.add_task)
        self.edit_btn.clicked.connect(self.edit_task)
        self.remove_btn.clicked.connect(self.remove_task)
        self.complete_btn.clicked.connect(self.mark_done)

        self.load_tasks()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def load_tasks(self):
        self.task_list.clear()
        self.cursor.execute("SELECT description FROM tasks")
        for row in self.cursor.fetchall():
            self.task_list.addItem(row[0])

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            self.cursor.execute("INSERT INTO tasks (description) VALUES (?)", (task,))
            self.conn.commit()
            self.task_input.clear()
            self.load_tasks()
        else:
            QMessageBox.warning(self, "Warning", "Task cannot be empty!")

    def edit_task(self):
        current_item = self.task_list.currentItem()
        if current_item:
            old_text = current_item.text()
            new_text, ok = QInputDialog.getText(self, "Edit Task", "Modify task:", text=old_text)
            if ok and new_text.strip():
                self.cursor.execute("UPDATE tasks SET description = ? WHERE description = ?", (new_text.strip(), old_text))
                self.conn.commit()
                self.load_tasks()
        else:
            QMessageBox.warning(self, "Warning", "No task selected!")

    def remove_task(self):
        current_item = self.task_list.currentItem()
        if current_item:
            task = current_item.text()
            self.cursor.execute("DELETE FROM tasks WHERE description = ?", (task,))
            self.conn.commit()
            self.load_tasks()
        else:
            QMessageBox.warning(self, "Warning", "No task selected!")

    def mark_done(self):
        current_item = self.task_list.currentItem()
        if current_item:
            old_text = current_item.text()
            if not old_text.startswith("✅ "):
                new_text = f"✅ {old_text}"
                self.cursor.execute("UPDATE tasks SET description = ? WHERE description = ?", (new_text, old_text))
                self.conn.commit()
                self.load_tasks()
        else:
            QMessageBox.warning(self, "Warning", "No task selected!")

    def search_task(self):
        query = self.search_input.text().lower()
        self.task_list.clear()
        self.cursor.execute("SELECT description FROM tasks")
        for row in self.cursor.fetchall():
            if query in row[0].lower():
                self.task_list.addItem(row[0])

# Run the application
app = QApplication(sys.argv)
window = ToDoApp()
window.show()
sys.exit(app.exec())
import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QListWidget, QPushButton, QLineEdit, QMessageBox, QInputDialog
)

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.conn = sqlite3.connect("todo.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 400, 500)

        self.layout = QVBoxLayout()

        # Search field
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Search task...")
        self.search_input.textChanged.connect(self.search_task)
        self.layout.addWidget(self.search_input)

        # Task input field
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter a new task...")
        self.layout.addWidget(self.task_input)

        # Task list
        self.task_list = QListWidget(self)
        self.layout.addWidget(self.task_list)

        # Buttons Layout
        btn_layout = QHBoxLayout()
        self.add_btn = QPushButton("Add Task")
        self.edit_btn = QPushButton("Edit Task")
        self.remove_btn = QPushButton("Remove Task")
        self.complete_btn = QPushButton("Mark as Done")

        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.edit_btn)
        btn_layout.addWidget(self.remove_btn)
        btn_layout.addWidget(self.complete_btn)

        self.layout.addLayout(btn_layout)
        self.setLayout(self.layout)

        # Button Actions
        self.add_btn.clicked.connect(self.add_task)
        self.edit_btn.clicked.connect(self.edit_task)
        self.remove_btn.clicked.connect(self.remove_task)
        self.complete_btn.clicked.connect(self.mark_done)

        self.load_tasks()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def load_tasks(self):
        self.task_list.clear()
        self.cursor.execute("SELECT description FROM tasks")
        for row in self.cursor.fetchall():
            self.task_list.addItem(row[0])

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            self.cursor.execute("INSERT INTO tasks (description) VALUES (?)", (task,))
            self.conn.commit()
            self.task_input.clear()
            self.load_tasks()
        else:
            QMessageBox.warning(self, "Warning", "Task cannot be empty!")

    def edit_task(self):
        current_item = self.task_list.currentItem()
        if current_item:
            old_text = current_item.text()
            new_text, ok = QInputDialog.getText(self, "Edit Task", "Modify task:", text=old_text)
            if ok and new_text.strip():
                self.cursor.execute("UPDATE tasks SET description = ? WHERE description = ?", (new_text.strip(), old_text))
                self.conn.commit()
                self.load_tasks()
        else:
            QMessageBox.warning(self, "Warning", "No task selected!")

    def remove_task(self):
        current_item = self.task_list.currentItem()
        if current_item:
            task = current_item.text()
            self.cursor.execute("DELETE FROM tasks WHERE description = ?", (task,))
            self.conn.commit()
            self.load_tasks()
        else:
            QMessageBox.warning(self, "Warning", "No task selected!")

    def mark_done(self):
        current_item = self.task_list.currentItem()
        if current_item:
            old_text = current_item.text()
            if not old_text.startswith("✅ "):
                new_text = f"✅ {old_text}"
                self.cursor.execute("UPDATE tasks SET description = ? WHERE description = ?", (new_text, old_text))
                self.conn.commit()
                self.load_tasks()
        else:
            QMessageBox.warning(self, "Warning", "No task selected!")

    def search_task(self):
        query = self.search_input.text().lower()
        self.task_list.clear()
        self.cursor.execute("SELECT description FROM tasks")
        for row in self.cursor.fetchall():
            if query in row[0].lower():
                self.task_list.addItem(row[0])

# Run the application
app = QApplication(sys.argv)
window = ToDoApp()
window.show()
sys.exit(app.exec())
