This repository is an example of using Python with PYQT5. It is being worked on slowly while I have time, and as i work on it.

Feel free to contribute.

https://github.com/mauikit/mauikit/blob/master/demo/src/main.qml

Also note you can't use OPENGL you need OPENGLES with Mobile Plasma (Which runs on pinephone and is neederd with QT5

With QT5 Their suggestions to use PYQT5 instead of PySide2 and try the python functions on how to do it.

You also need to use this utility to create the qml file (you can't just lad the qml.qmrc

pyrcc5

This utility creates the import file, for mapping the qml files.

I think alot of the functionality that is in C++ is in the PYQT5 api. But the documentation is lacking, you can try copying the C++ API and mimic it in PYQT5 . Thats what i was doing, and was getting good results.

There are some changtes (like the pyrcc5 i mentioned and loading the qml.qrc files.

https://github.com/hovo1990/pyQt5-QML-examples/blob/master/tutOff3_property/main.py

https://stackoverflow.com/questions/54836382/pyqt-import-qml-theme-from-different-directory https://maui-project.gitbook.io/mauikit/documentation-1/controls https://www.programmersought.com/article/2274746094/
https://zetcode.com/gui/qtquick/
https://stackoverflow.com/questions/37843212/pyqt5-module-qtquick-is-not-installed
https://programtalk.com/python-examples/PyQt5.QtQml.QQmlComponent/

All these links should help you continue if you guys really want to code pythonm apps with pinephone.

Do to the missing QTQuick libraries on Manjaro im trying to do it this way:

QQmlApplicationEngine engine;
engine.load(QUrl(QStringLiteral("qrc:/main.qml")));
QQuickWindow *window = qobject_cast<QQuickWindow*>(engine.rootObjects().at(0));
if (!window) {
    qFatal("Error: Your root item has to be a window.");
    return -1;
}
window->show();
QQuickItem *root = window->contentItem();

QQmlComponent component(&engine, QUrl("qrc:/Button.qml"));
QQuickItem *object = qobject_cast<QQuickItem*>(component.create());

QQmlEngine::setObjectOwnership(object, QQmlEngine::CppOwnership);

object->setParentItem(root);
object->setParent(&engine);

object->setProperty("color", QVariant(QColor(255, 255, 255)));
object->setProperty("text", QVariant(QString("foo")));

to makepkg

type 

makepkg -d -f