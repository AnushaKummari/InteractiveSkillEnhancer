import json
import os
from PyQt5.QtWidgets import QWidget


def load_translations(lang='en'):
    base = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base, 'i18n', f'{lang}.json')
    if not os.path.exists(path):
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def apply_translations(root: QWidget, translations: dict):
    """Walk the widget tree starting at root and replace texts that match Bengali keys.

    This is non-destructive: it only replaces text when the widget's current text
    exactly matches a language key in translations. For generated UI code that
    sets Bengali strings via retranslateUi, this will swap them to English.
    """
    if root is None:
        return

    # Helper to attempt setText / setPlaceholderText on known Qt widgets
    def try_set_text(w, new_text):
        # QLabel, QPushButton, QComboBox (current text items handled separately), QLineEdit
        if hasattr(w, 'setText') and callable(getattr(w, 'setText')):
            try:
                w.setText(new_text)
                return True
            except Exception:
                pass
        if hasattr(w, 'setPlaceholderText') and callable(getattr(w, 'setPlaceholderText')):
            try:
                w.setPlaceholderText(new_text)
                return True
            except Exception:
                pass
        return False

    # If the root has a text matching a Bengali key, apply replacement
    def replace_if_match(w):
        # Check common getters
        current_text = None
        try:
            if hasattr(w, 'text') and callable(getattr(w, 'text')):
                current_text = w.text()
        except Exception:
            current_text = None

        # Some widgets like QComboBox store items rather than a text() property.
        # We'll handle combobox items separately below.

        if isinstance(current_text, str) and current_text in translations:
            try_set_text(w, translations[current_text])

    # BFS traversal
    stack = [root]
    visited = set()
    while stack:
        w = stack.pop()
        if w in visited:
            continue
        visited.add(w)

        # Try to replace widget text
        replace_if_match(w)

        # Handle QComboBox items explicitly
        try:
            # Import here to avoid top-level Qt imports if not used elsewhere
            from PyQt5.QtWidgets import QComboBox
            if isinstance(w, QComboBox):
                for i in range(w.count()):
                    item_text = w.itemText(i)
                    if item_text in translations:
                        w.setItemText(i, translations[item_text])
        except Exception:
            pass

        # Enqueue children
        try:
            for child in w.findChildren(QWidget):
                if child not in visited:
                    stack.append(child)
        except Exception:
            pass
