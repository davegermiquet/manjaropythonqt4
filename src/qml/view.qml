import org.kde.mauikit 1.0 as Maui
import QtQuick 2.3

Maui.Page {


Rectangle {
    width: 200
    height: 100
    color: "red"

    Text {
        anchors.centerIn: parent
        text: "Hello, World!"
    }
}

}