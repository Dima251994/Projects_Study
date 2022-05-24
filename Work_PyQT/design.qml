import QtQuick 2.0
Rectangle { // главный квадрат в который мы вкладываем другой
    color: "red"
    width:300
    height: 300
    Rectangle {  //создание треугольника, по сути это как Qlabel в Qt,создание определенного обьекта, в даном случае треугольника
        width: 200
        height: 200
        color: "green"
        radius: 7 // делает заокругленные части фигуры
        border.color: "blue" // цвет рамки
        border.width: 5 // ширина рамки
        anchors.centerIn: parent // становится в центр обьекта
        MouseArea { // создаем место для работы с мышкой
            anchors.fill: parent // вся местность квадрата будет рабочей
            onClicked: { // создание команды (onClicked не может иметь другое название) которая отображает в консоль Hello world
                console.log("Hello world")
            }
        }
        Text {  // добавление текста, и параметров
            text: "Hello world"
            anchors.centerIn: parent
        }
    }
}