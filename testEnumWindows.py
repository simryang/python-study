# -*- coding:utf-8 -*-
# TeraCopy 내부의 모든 윈도우 객체를 나열합니다.
#from win32 import win32gui
import win32gui
#import pywintypes
import sys
 
# 부모 윈도우의 핸들을 검사합니다.
class WindowFinder:
	def __init__(self, windowname):
		try:
			win32gui.EnumWindows(self.__EnumWindowsHandler, windowname)		
		except pywintypes.error as e:
			# 발생된 예외 중 e[0]가 0이면 callback이 멈춘 정상 케이스
			if e[0] == 0: pass
 
	def __EnumWindowsHandler(self, hwnd, extra):
		wintext = win32gui.GetWindowText(hwnd)
		if wintext.find(extra) != -1:
			self.__hwnd = hwnd
			return pywintypes.FALSE # FALSE는 예외를 발생시킵니다.	
 
	def GetHwnd(self):
		return self.__hwnd
 
	__hwnd = 0
 
# 자식 윈도우의 핸들 리스트를 검사합니다.
class ChildWindowFinder:
	def __init__(self, parentwnd):
		try:
			win32gui.EnumChildWindows(parentwnd, self.__EnumChildWindowsHandler, None)		
		except pywintypes.error as e:
			if e[0] == 0: pass		
 
	def __EnumChildWindowsHandler(self, hwnd, extra):
		self.__childwnds.append(hwnd)
 
	def GetChildrenList(self):
		return self.__childwnds
 
	__childwnds = []
 
# windowname을 가진 윈도우의 모든 자식 윈도우 리스트를 얻어낸다.
def GetChildWindows(windowname):
 
	# TeraCopy의 window handle을 검사한다.
	teracopyhwnd = WindowFinder(windowname).GetHwnd()
 
	# Teracopy의 모든 child window handle을 검색한다.
	childrenlist = ChildWindowFinder(teracopyhwnd).GetChildrenList()
 
	return teracopyhwnd, childrenlist
 
# main 입니다.
def main(argv):
	hwnd, childwnds = GetChildWindows('Everything')
	print ("%X %s" % (hwnd, win32gui.GetWindowText(hwnd)))
 
	print ("HWND     CtlrID\tClass\tWindow Text")
	print ("===========================================")
 
	for child in childwnds:
		ctrl_id  = win32gui.GetDlgCtrlID(child)
		wnd_clas = win32gui.GetClassName(child)
		wnd_text = win32gui.GetWindowText(child)		
		print ("%08X %6d\t%s\t%s" % (child, ctrl_id, wnd_clas, wnd_text))
 
	return 0
 
if __name__ == '__main__':
	sys.exit(main(sys.argv))