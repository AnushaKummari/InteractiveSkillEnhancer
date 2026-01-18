"""
Login Window for Teacher Dashboard
This module provides the authentication screen before accessing the teacher dashboard.
"""

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox, QApplication
)
from PyQt5.QtCore import Qt, QSize, pyqtSignal, QTimer
from PyQt5.QtGui import QFont, QIcon, QPixmap, QColor
from PyQt5.QtGui import QLinearGradient, QPalette
import os


class LoginWindow(QMainWindow):
    """
    Login window for teacher authentication.
    Emits login_successful signal when credentials are valid.
    """
    
    # Signal to indicate successful login
    login_successful = pyqtSignal()
    
    # Default credentials
    VALID_EMAIL = "teacher@gmail.com"
    VALID_PASSWORD = "Teacher123"
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Initialize the login UI with title and login form"""
        
        # Set window properties
        self.setWindowTitle("Interactive Skill Enhancer - Teacher Login")
        self.setGeometry(100, 100, 800, 600)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Add title section
        title_layout = self._create_title_section()
        
        # Add login form section
        form_layout = self._create_login_form()
        
        # Combine layouts with stretch
        main_layout.addLayout(title_layout, 1)
        main_layout.addLayout(form_layout, 2)
        main_layout.addStretch()
        
        central_widget.setLayout(main_layout)
        
        # Style the window
        self._apply_styles()
        
    def _create_title_section(self):
        """Create the title section of the login window"""
        
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(50, 50, 50, 30)
        
        # Main title
        title_label = QLabel("Interactive Skill Enhancer")
        title_font = QFont()
        title_font.setPointSize(28)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50;")
        
        # Subtitle
        subtitle_label = QLabel("A Personalised Learning Tool")
        subtitle_font = QFont()
        subtitle_font.setPointSize(16)
        subtitle_font.setItalic(True)
        subtitle_label.setFont(subtitle_font)
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setStyleSheet("color: #34495e;")
        
        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)
        layout.addSpacing(20)
        
        return layout
    
    def _create_login_form(self):
        """Create the centered floating login form"""
        
        # Outer layout to center the form
        outer_layout = QHBoxLayout()
        outer_layout.addStretch()
        
        # Inner layout for the form
        form_layout = QVBoxLayout()
        form_layout.setSpacing(15)
        form_layout.setContentsMargins(40, 40, 40, 40)
        
        # Form title
        form_title = QLabel("Teacher Login")
        form_title_font = QFont()
        form_title_font.setPointSize(18)
        form_title_font.setBold(True)
        form_title.setFont(form_title_font)
        form_title.setAlignment(Qt.AlignCenter)
        form_title.setStyleSheet("color: #2c3e50;")
        form_layout.addWidget(form_title)
        
        form_layout.addSpacing(20)
        
        # Email label and input
        email_label = QLabel("Email:")
        email_label_font = QFont()
        email_label_font.setPointSize(11)
        email_label.setFont(email_label_font)
        email_label.setStyleSheet("color: #2c3e50; font-weight: bold;")
        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        self.email_input.setMinimumHeight(40)
        self._style_input(self.email_input)
        
        form_layout.addWidget(email_label)
        form_layout.addWidget(self.email_input)
        
        # Password label and input
        password_label = QLabel("Password:")
        password_label_font = QFont()
        password_label_font.setPointSize(11)
        password_label.setFont(password_label_font)
        password_label.setStyleSheet("color: #2c3e50; font-weight: bold;")
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumHeight(40)
        self._style_input(self.password_input)
        
        form_layout.addWidget(password_label)
        form_layout.addWidget(self.password_input)
        
        form_layout.addSpacing(20)
        
        # Login button
        self.login_button = QPushButton("Login")
        self.login_button.setMinimumHeight(45)
        self.login_button.setMinimumWidth(150)
        self.login_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.login_button.setCursor(Qt.PointingHandCursor)
        self._style_login_button(self.login_button)
        self.login_button.clicked.connect(self.handle_login)
        
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.login_button)
        button_layout.addStretch()
        
        form_layout.addLayout(button_layout)
        
        form_layout.addSpacing(10)
        
        # Error message label (initially hidden)
        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: #e74c3c; font-weight: bold;")
        self.error_label.setAlignment(Qt.AlignCenter)
        self.error_label.setVisible(False)
        form_layout.addWidget(self.error_label)
        
        # Create a widget to hold the form with a background
        form_widget = QWidget()
        form_widget.setLayout(form_layout)
        form_widget.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                border-radius: 10px;
                border: 1px solid #bdc3c7;
            }
        """)
        form_widget.setMinimumWidth(350)
        form_widget.setMaximumWidth(450)
        
        outer_layout.addWidget(form_widget)
        outer_layout.addStretch()
        
        return outer_layout
    
    def _style_input(self, input_field):
        """Apply styling to input fields"""
        input_field.setStyleSheet("""
            QLineEdit {
                background-color: #ecf0f1;
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                padding: 8px;
                font-size: 12px;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
                background-color: #ffffff;
            }
        """)
    
    def _style_login_button(self, button):
        """Apply styling to login button"""
        button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 30px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1f618d;
            }
        """)
    
    def _apply_styles(self):
        """Apply overall window styling with background image"""
        # Get the background image path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        bg_path = os.path.join(current_dir, '../Images/login_bg.png')
        
        # Apply background image if it exists
        if os.path.exists(bg_path):
            self.setStyleSheet(f"""
                QMainWindow {{
                    background-image: url('{bg_path}');
                    background-repeat: no-repeat;
                    background-position: center;
                    background-attachment: fixed;
                }}
            """)
        else:
            # Fallback to solid color if image not found
            self.setStyleSheet("""
                QMainWindow {{
                    background-color: #ecf0f1;
                }}
            """)
    
    def handle_login(self):
        """Handle login button click"""
        email = self.email_input.text().strip()
        password = self.password_input.text()
        
        # Validate credentials
        if self.validate_credentials(email, password):
            # Emit signal to indicate successful login
            self.login_successful.emit()
            self.close()
        else:
            # Show error message
            self.error_label.setText("Invalid email or password!")
            self.error_label.setVisible(True)
            self.password_input.clear()
            
            # Hide error message after 3 seconds
            QTimer.singleShot(3000, lambda: self.error_label.setVisible(False))
    
    def validate_credentials(self, email, password):
        """
        Validate the provided credentials.
        
        Args:
            email (str): The email address
            password (str): The password
            
        Returns:
            bool: True if credentials are valid, False otherwise
        """
        return email == self.VALID_EMAIL and password == self.VALID_PASSWORD
    
    def keyPressEvent(self, event):
        """Handle key press events (Enter to login)"""
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.handle_login()
        else:
            super().keyPressEvent(event)
