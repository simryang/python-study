import win32gui

def window_enumeration_handler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

top_windows = []
win32gui.EnumWindows(window_enumeration_handler, top_windows)

for hwnd, title in top_windows:
    print(hwnd, title)