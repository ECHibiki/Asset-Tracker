## Static vs Dynamic Linking

When building with pyinstaller it will statically link everything requiring certain LGPL conditions<br/>
These conditions are bypassed with:
```pyinstaller --runtime-tmpdir /tmp --add-data /path/to/PySide2/lib/PySide2/:PySide2 --add-binary /path/to/PySide2/lib/Qt*:qt.conf your_script.py```
