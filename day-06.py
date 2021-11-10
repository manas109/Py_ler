Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from icecream import ic
>>> k=10
>>> ic(k)
[38;5;247mic[39m[38;5;245m|[39m[38;5;245m [39m[38;5;247mError[39m[38;5;245m:[39m[38;5;245m [39m[38;5;247mFailed[39m[38;5;245m [39m[38;5;247mto[39m[38;5;245m [39m[38;5;247maccess[39m[38;5;245m [39m[38;5;247mthe[39m[38;5;245m [39m[38;5;247munderlying[39m[38;5;245m [39m[38;5;247msource[39m[38;5;245m [39m[38;5;247mcode[39m[38;5;245m [39m[38;5;100mfor[39m[38;5;245m [39m[38;5;247manalysis[39m[38;5;245m.[39m[38;5;245m [39m[38;5;247mWas[39m[38;5;245m [39m[38;5;247mic[39m[38;5;245m([39m[38;5;245m)[39m[38;5;245m [39m[38;5;247minvoked[39m[38;5;245m [39m[38;5;100min[39m[38;5;245m [39m[38;5;247ma[39m[38;5;245m [39m[38;5;247mREPL[39m[38;5;245m [39m[38;5;245m([39m[38;5;247me[39m[38;5;245m.[39m[38;5;247mg[39m[38;5;245m.[39m[38;5;245m [39m[38;5;166mfrom[39m[38;5;245m [39m[38;5;136mthe[39m[38;5;245m [39m[38;5;247mcommand[39m[38;5;245m [39m[38;5;247mline[39m[38;5;245m)[39m[38;5;245m,[39m[38;5;245m [39m[38;5;247ma[39m[38;5;245m [39m[38;5;247mfrozen[39m[38;5;245m [39m[38;5;247mapplication[39m[38;5;245m [39m[38;5;245m([39m[38;5;247me[39m[38;5;245m.[39m[38;5;247mg[39m[38;5;245m.[39m[38;5;245m [39m[38;5;247mpackaged[39m[38;5;245m [39m[38;5;100mwith[39m[38;5;245m [39m[38;5;247mPyInstaller[39m[38;5;245m)[39m[38;5;245m,[39m[38;5;245m [39m[38;5;100mor[39m[38;5;245m [39m[38;5;247mdid[39m[38;5;245m [39m[38;5;247mthe[39m[38;5;245m [39m[38;5;247munderlying[39m[38;5;245m [39m[38;5;247msource[39m[38;5;245m [39m[38;5;247mcode[39m[38;5;245m [39m[38;5;247mchange[39m[38;5;245m [39m[38;5;247mduring[39m[38;5;245m [39m[38;5;247mexecution[39m[38;5;166m?[39m
10
>>> import os
>>> dir(os)
['DirEntry', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_walk', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write']
>>> 
>>> 
>>> 
>>> ['DirEntry', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_walk', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write']
['DirEntry', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_walk', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write']
>>> os.listdir()
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python39.dll', 'pythonw.exe', 'Scripts', 'tcl', 'Tools', 'vcruntime140.dll', 'vcruntime140_1.dll']
>>> from file in os.listdir("my_dir"):
	
SyntaxError: invalid syntax
>>> import os
>>> from file in os.listdir("my_dir"):
	
SyntaxError: invalid syntax
>>> for file in os.listdir("my_dir"):
	if frile.endswith(".txt"):
		print(file)

		
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    for file in os.listdir("my_dir"):
FileNotFoundError: [WinError 3] The system cannot find the path specified: 'my_dir'
>>> import os
>>> for file in os.listdir(r"E:\CG projects"):
	if file.endswith(".txt"):
		print(file)

		
>>> 
>>> a=1
>>> b=0
>>> if a and b :
	print("hai")

	
>>> b=1
>>> if a and b :
	print("hai")

	
hai
>>> if a or b :
	print("hai")

	
hai
>>> a=1
>>> a
1
>>> while a<10:
	print(a)

	
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    print(a)
KeyboardInterrupt
>>> while a<10:
	print(a)
	a=a+1

	
1
2
3
4
5
6
7
8
9
>>> a=1
>>> while a<=10:
	print(a)
	a=a+1

	
1
2
3
4
5
6
7
8
9
10
>>> a=1
>>> a=10
>>> a
10
>>> while(a>=1):
	print(a,end=' ')
	a=a-1

	
10 9 8 7 6 5 4 3 2 1 
>>> a=10
>>> while(a>=1):
	print(a,'')
	a=a-1

	
10 
9 
8 
7 
6 
5 
4 
3 
2 
1 
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(1,10):
	print(i)

	
1
2
3
4
5
6
7
8
9
>>> for i in range(1,10,2):
	print(i)

	
1
3
5
7
9
>>> name='manu'
>>> for i in name:
	print(i)

	
m
a
n
u
>>> names=['manu','anu','janu']
>>> for i in names:
	print(i)

	
manu
anu
janu
>>> 