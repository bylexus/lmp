cmake_minimum_required(VERSION 3.5)

project(lmp LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt5 COMPONENTS Widgets Multimedia MultimediaWidgets REQUIRED)

SET(QT_USE_QTMULTIMEDIA TRUE)
SET(QT_USE_QTMULTIMEDIAWIDGETS TRUE)
SET(EXECUTABLE_NAME lmp)


add_executable(${EXECUTABLE_NAME}
  main.cpp
  mainwindow.cpp
  mainwindow.h
  mainwindow.ui
  testdialog.cpp
  testdialog.h
  testdialog.ui
  playbar.cpp
  playbar.h
  playbar.ui
)


target_link_libraries(${EXECUTABLE_NAME} PRIVATE
    Qt5::Widgets
    Qt5::Multimedia
    Qt5::MultimediaWidgets
)
