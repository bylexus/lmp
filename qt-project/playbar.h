#ifndef PLAYBAR_H
#define PLAYBAR_H

#include <QWidget>
#include <QToolBar>
#include <QLabel>

namespace Ui {
class PlayBar;
}

class PlayBar : public QToolBar
{
    Q_OBJECT

public:
    explicit PlayBar(QWidget *parent = nullptr);
    ~PlayBar();

signals:
    void playTriggered();
    void pauseTriggered();
    void stopTriggered();
    void selectSongTriggered();

private:
    Ui::PlayBar *ui;

    QLabel *nowPlayingLabel;
    QLabel *timelabel;
};

#endif // PLAYBAR_H
