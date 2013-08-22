from ctypes import *
from ctypes.wintypes import BOOL,HWND,RECT,LPCWSTR,UINT,INT,DWORD,WORD, WCHAR
import datetime
#from ctypes.util import find_library
libc = cdll.msvcrt
libw = windll.kernel32
#print libw
FindFirstFile = libw.FindFirstFileW
FindNextFile = libw.FindNextFileW
FindClose = libw.FindClose
GetFileAttributes = libw.GetFileAttributesW
GetLastError = libw.GetLastError
#printf = libc.printf

class FILETIME(Structure):
	_fields_ = [("dwLowDateTime", DWORD),
		("dwHighDateTime", DWORD)]

class WIN32_FIND_DATAW(Structure):
	_fields_ = [("dwFileAttributes", DWORD),
		("ftCreationTime", FILETIME),
		("ftLastAccessTime", FILETIME),
		("ftLastWriteTime", FILETIME),
		("nFileSizeHigh", DWORD),
		("nFileSizeLow", DWORD),
		("dwReserved0", DWORD),
		("dwReserved1", DWORD),
		("cFileName",c_wchar*32767), #32767 MAX_PATH for windows???
		("cAlternateFileName", c_wchar*14)]
	


def Wlistdir(Path):
	listdir = []
	dir_p = WIN32_FIND_DATAW()
	hfind = FindFirstFile(Path,byref(dir_p)) # byref works as pointer but skip some treatments required if a real pointer was used
	if hfind != -1:
		
		while True:
			#print dir_p.cFileName, ": ", dir_p.nFileSizeLow
			if dir_p.cFileName <> "." and dir_p.cFileName <> "..":
				#print dir_p.dwFileAttributes
				listdir.append([dir_p.cFileName, dir_p.nFileSizeLow,isdir(dir_p)])
				
			dp = FindNextFile(hfind, byref(dir_p))
			
			if not dp:
				FindClose(hfind)
				break
				
		return listdir
		
	else:
		return []
		print "error:", GetLastError(), Path

def isdir(dir_p):
	if dir_p.dwFileAttributes & 16:
		
		return True
	else:
		return False

