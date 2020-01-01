#include "playbar.h"
#include "ui_playbar.h"

PlayBar::PlayBar(QWidget *parent) :
    QToolBar(parent),
    ui(new Ui::PlayBar)
{
    ui->setupUi(this);

    timelabel = new QLabel("");
    nowPlayingLabel = new QLabel("");

    addWidget(timelabel);
    addWidget(nowPlayingLabel);

    connect(ui->actionPlay,&QAction::triggered,this,&PlayBar::playTriggered);
    connect(ui->actionStop,&QAction::triggered,this,&PlayBar::stopTriggered);
    connect(ui->actionLoadSong,&QAction::triggered,this,&PlayBar::selectSongTriggered);
}

PlayBar::~PlayBar()
{
    delete ui;
    delete nowPlayingLabel;
    delete timelabel;
}
