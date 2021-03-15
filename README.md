
TLDR:


To Make this on Manjaro PinePhone please do the following:

makepkg -d -f

This repository shows a working example of using Plasma Mobile and QT5 using QQmlApplicationEngine
as we are unable to use QTQuick module.

MauiKit is used in this example.

Feel free to contribute.

pyrcc5 is needed to do locators of QML Files.

- This utility creates the import file, for mapping the qml files.

references:

I think alot of the functionality that is in C++ is in the PYQT5 api. But the documentation is lacking, you can try copying the C++ API and mimic it in PYQT5 . Thats what i was doing, and was getting good results.

There are some changtes (like the pyrcc5 i mentioned and loading the qml.qrc files.

https://github.com/hovo1990/pyQt5-QML-examples/blob/master/tutOff3_property/main.py

https://stackoverflow.com/questions/54836382/pyqt-import-qml-theme-from-different-directory https://maui-project.gitbook.io/mauikit/documentation-1/controls https://www.programmersought.com/article/2274746094/
https://zetcode.com/gui/qtquick/
https://stackoverflow.com/questions/37843212/pyqt5-module-qtquick-is-not-installed
https://programtalk.com/python-examples/PyQt5.QtQml.QQmlComponent/
https://stackoverflow.com/questions/26704621/how-to-create-a-qqmlcomponent-from-c-at-runtime/26705694
https://github.com/mauikit/mauikit/blob/master/demo/src/main.qml
