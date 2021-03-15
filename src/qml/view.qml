import org.kde.mauikit 1.0 as Maui
import QtQuick 2.3

Maui.ApplicationWindow {
    id: root
    width: 300; height: 100
    title: "my window"
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
}