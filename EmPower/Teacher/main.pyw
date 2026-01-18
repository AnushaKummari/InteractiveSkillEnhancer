from PyQt5.QtWidgets import *
from Frontend.src.Home import Home
from Frontend.src.LoginWindow import LoginWindow
from Frontend.src.Document_Formatter import *
from Frontend.src.SplashScreen import SplashScreen
import sys 

# i18n helper: load and apply English translations at runtime
try:
    from utils.i18n import load_translations, apply_translations
    TRANSLATIONS = load_translations('en')
except Exception:
    TRANSLATIONS = {}

if __name__ == '__main__':
    app = QApplication(sys.argv)

    splash = SplashScreen()

    # Center the splash screen window on the screen
    splash_width = splash.width()
    splash_height = splash.height()
    screen = QGuiApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    x = (screen_geometry.width() - splash_width) // 2
    y = (screen_geometry.height() - splash_height) // 2
    splash.move(x, y)

    # now show the splash window
    splash.show()
    splash.progress()

    # Show login window first
    login_window = LoginWindow()
    
    # Center the login window on the screen
    login_width = login_window.width()
    login_height = login_window.height()
    login_x = (screen_geometry.width() - login_width) // 2
    login_y = (screen_geometry.height() - login_height) // 2
    login_window.move(login_x, login_y)
    
    login_window.show()
    
    # Variable to hold the home window
    window = None
    
    # Define function to handle successful login
    def on_login_successful():
        global window
        splash.show()
        splash.progress()
        
        window = Home()
        window.showMaximized()
        window.show()

        # Apply translations to the whole window (if available)
        if TRANSLATIONS:
            try:
                apply_translations(window, TRANSLATIONS)
            except Exception:
                pass

        splash.finish(window)
    
    # Connect login signal to handler
    login_window.login_successful.connect(on_login_successful)

    sys.exit(app.exec_()) 

