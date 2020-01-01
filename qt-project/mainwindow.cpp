#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include "testdialog.h"
#include <QFileDialog>
#include <QStandardPaths>
#include <QMediaPlayer>

MainWindow::MainWindow(QWidget *parent)
        : QMainWindow(parent)
        , ui(new Ui::MainWindow)
{
        ui->setupUi(this);
        this->setCentralWidget(ui->centralwidget);

        ui->toolBar->addWidget(new QLabel("Now playing ..."));
        connect(ui->toolBar, &PlayBar::selectSongTriggered,this,&MainWindow::selectSong);
}

MainWindow::~MainWindow()
{
        delete ui;
}

void MainWindow::helloSlot()
{
        qDebug("Hello, world!");
        TestDialog td(this);
        td.exec();
}

void MainWindow::selectSong()
{
        qDebug("Hello, world!");
        auto fileName = QFileDialog::getOpenFileUrl(
                                this,
                                "Open Song",
                                QStandardPaths::locate(QStandardPaths::MusicLocation,"",QStandardPaths::LocateDirectory),
                                "Audio files (*.mp3 *.m4a *.ogg)"
                                );
        QMediaPlayer *p = new QMediaPlayer;
        p->setMedia(fileName);
        p->setVolume(50);
        p->play();
}
