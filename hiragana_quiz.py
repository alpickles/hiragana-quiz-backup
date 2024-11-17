import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QPushButton, QLabel, QLineEdit, \
    QGroupBox, QGridLayout
from PyQt5.QtCore import Qt

# Hiragana dictionary
hiragana_dict = {
    'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
    'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
    'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
    'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
    'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
    'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
    'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
    'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    'わ': 'wa', 'を': 'wo', 'ん': 'n'
}


class HiraganaQuizApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hiragana Quiz")

        self.layout = QVBoxLayout()

        # Frame for checkboxes (selection) - Grid layout
        self.selection_groupbox = QGroupBox("Select Hiragana Characters")
        self.selection_layout = QGridLayout()
        self.selection_groupbox.setLayout(self.selection_layout)

        self.checkbox_vars = {}
        self.checkboxes = []
        row, col = 0, 0

        # Add checkboxes to the grid layout
        for character in hiragana_dict:
            var = QCheckBox(character)
            var.setChecked(True)  # Default to selected
            self.checkbox_vars[character] = var
            self.checkboxes.append(var)
            self.selection_layout.addWidget(var, row, col)

            col += 1
            if col > 4:  # Limit number of columns per row
                col = 0
                row += 1

        self.layout.addWidget(self.selection_groupbox)

        # Select All / Deselect All Buttons
        self.button_layout = QHBoxLayout()
        self.select_all_button = QPushButton("Select All")
        self.select_all_button.clicked.connect(self.select_all)
        self.deselect_all_button = QPushButton("Deselect All")
        self.deselect_all_button.clicked.connect(self.deselect_all)
        self.button_layout.addWidget(self.select_all_button)
        self.button_layout.addWidget(self.deselect_all_button)
        self.layout.addLayout(self.button_layout)

        # Display character
        self.character_label = QLabel()
        self.character_label.setAlignment(Qt.AlignCenter)
        self.character_label.setStyleSheet("font-size: 48px;")
        self.layout.addWidget(self.character_label)

        # User input field
        self.romaji_entry = QLineEdit()
        self.romaji_entry.setStyleSheet("font-size: 24px;")
        self.layout.addWidget(self.romaji_entry)

        # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.submit_button)

        # Feedback label
        self.feedback_label = QLabel()
        self.feedback_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.feedback_label)

        # Next button
        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_character)
        self.layout.addWidget(self.next_button)

        self.selected_characters = list(hiragana_dict.keys())  # Default to all characters
        self.current_character = ''

        self.setLayout(self.layout)
        self.next_character()  # Start the quiz with the first character

    def check_answer(self):
        user_input = self.romaji_entry.text().strip().lower()
        correct_answer = hiragana_dict[self.current_character]

        if user_input == correct_answer:
            self.feedback_label.setText("Correct!")
            self.feedback_label.setStyleSheet("color: green;")
        else:
            self.feedback_label.setText(f"Incorrect! The correct answer is: {correct_answer}")
            self.feedback_label.setStyleSheet("color: red;")

    def next_character(self):
        # Update the selected characters based on checkbox selections
        self.selected_characters = [character for character, var in self.checkbox_vars.items() if var.isChecked()]

        if not self.selected_characters:
            self.feedback_label.setText("Please select at least one character to practice.")
            self.feedback_label.setStyleSheet("color: red;")
            return

        # Pick a random character from the selected list
        self.current_character = random.choice(self.selected_characters)
        self.character_label.setText(self.current_character)
        self.romaji_entry.clear()  # Clear the input field
        self.feedback_label.clear()  # Clear the feedback label

    def select_all(self):
        """Select all checkboxes"""
        for var in self.checkbox_vars.values():
            var.setChecked(True)

    def deselect_all(self):
        """Deselect all checkboxes"""
        for var in self.checkbox_vars.values():
            var.setChecked(False)


# Main execution
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HiraganaQuizApp()
    window.show()
    sys.exit(app.exec_())
