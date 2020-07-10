import win32gui
import win32con
import win32api

# 계산기 있으면 끄기
hwnd = win32gui.FindWindow(None, "계산기")
print(hwnd)

win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

#메모장 있으면 글쓰기 Hi
hwnd = win32gui.FindWindow(None, "제목 없음 - 메모장")
edit = win32gui.GetDlgItem(hwnd, 0xF)

win32api.SendMessage(edit, win32con.WM_CHAR, ord('H'), 0)
win32api.Sleep(100)

win32api.SendMessage(edit, win32con.WM_CHAR, ord('i'), 0)
win32api.Sleep(100)