from win32 import win32gui

def EnumWindowsHandler (hwnd, extra):
    wintext = win32gui.GetWindowText(hwnd)
    if wintext and 'Everything' in wintext:
        print ("%08X: %s" % (hwnd, wintext))
    else:
        return None

if __name__ == '__main__':
    win32gui.EnumWindows(EnumWindowsHandler, None)