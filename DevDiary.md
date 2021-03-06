Developer's Diary
====================

During my first days with PyQt I learned a lot of things: Python, Qt, architectural concepts, project organisation, you name it.
The sheer flood of information and concepts to learn are overwhelming.
So I decided to write a Developer's Diary, to keep track of the things I learn, why I made some specific decisions,
document the progress.

**Note:** On 13.04.2019, I decided to trash the python/Qt idea, and switch to Electron instead. Why? Well, just because. I lost
interest in python/Qt, as it is "yet another framework" and is nothing really new for me. So I stick to a more familiar environment:
JavaScript, and try Electron as an App framework instead.

11.11.2018 - Model / DB considerations
-------------

I want to store the directories to inspect in a local storage - I will set up a local sqlite db for all data related things,
so I will also store the read directories in a table:

* Model "MusicDir"
  * Table: music_dir
  * props:
    * id: int, auto-increment
    * path: string
    * last_sync: timestamp

Therefore I need to see how this is done in Qt, DB and Model-wise.

So far I learned:

* SQLite has its own unique ID (ROWID, or OID), so it is not necessary to add auto-increment ID columns.
* SQLite is not "type safe": It knows only a handful of base datatypes, and a column has no fixed type.
* SQLite knows no datetype data type, instead one can use a simple text column.
* DB handling in Qt is very easy with the QSqlDatabase, QSqlQuery, QSql*View classes.

I decided to create Model classes which inherit from a QSql*View class. Those models also have a static method for creating
the underlying table structure (createTable), which is executed during app boot.

29.10.2018 - Reading Audio meta tags
--------------------------------------

I started investigating audio metadata. After a short Internet search, I found the python library 'mutagen', which
can extract audio meta data from almost any audio file.

I gave it a short try with walking through some audio folders. It works really easy.

Unfortunately, audio meta tags are all but standardized... every format uses its own meta infos,
and even Id3V2 has no real "standard" of fields - so this need to be abstracted for every supported type,
which I will do on another day.
I guess I will create audio processor classes for each type that is supported by mutagen's FileType base class.

An overview of ID3V2 declared frames (= meta info fields) can be found here:

http://id3.org/id3v2.3.0#Declared_ID3v2_frames

28.10.2018
-------------

Choosing and playing single files already work - What I missed already was a "remember last opened folder" functionality.
So I tried the QSettings object today.
Not much of a surprise here - simple to use. It is even easier than the C++-Version: QSettings.getValue() directly
returns the originally stored data type - you don't get a QVariant type.

So choosing a single song already remembers the last opened folder so far.

27.10.2018
--------------

### .ui-Files with QtDesigner

Today I experienced with QtDesigner, creating a .ui-File for the player widget - it worked like a charm, no fiddling, no
debugging, just load the .ui-File with PyQt5.uic.loadUi, that's it! I'm a bit surprised it was so easy....

### Resources

For the UI file, I want to use FontAwesome icons, the SVG version. Qt knows "resource files", which easily can be
defined within QtDesigner, too.

After defining the resources, they can be used within QtDesigner.
But they are not automatically available within the running program: You have to compile the resources and import them in the
main program.

I created a Makefile to generate the resource files:

* `make` builds all resource files (`.qrc`), using `pyrcc5`, in the `resources/` dir.
* in the app.py main program, the resources need to be imported: `import resources.icons`, for example.

Super-easy, too, if you know how.

### Use own widgets in QtDesigner

I plan to create several custom widgets as own classes with a .ui file. Therefore I need to use those widgets in QtDesigner,
e.g. to "patch" them together in the main window.

I found out that this is possible in QtDesigner, using the Placeholder for Widgets functionality: You can right-click
on a widget and choose "Set as placeholder for defined class": You then can define the class that will be injected during runtime.

**Important:** The include file must be the Python module defining the class, not a c header file:

![Class placeholder dialog](doc/images/qdesigner_placeholder_widget.png)

The widget then can be used in QtDesigner. Only drawback: It is only an empty placeholder, so no UI is shown.

### Loader animation with animated gif

I wanted to indicate loading / busy status globally in the status bar of the main widget, using an animated gif.
This was surprisingly easy:

* create a QLabel with a QMovie, which takes an animated gif
* Add the widget to the main window's statusbar with 'addPermanentWidget'
* Make a show/hide function/slot in the QApplication class to show/hide it from anywhere

### First steps with non-gui-Threads

Since one of the first tasks in the application would be to scan a dir for sound files, I read about running long-running workers.
Qt knows QThreadPool and QRunnable: A thread management system designed for that case.

Basically one runs a Task (QRunnable) in a thread pool, and can signal the ui thread via standard signals.
I had some difficulties at the beginning, because a Worker that inherits from QRunnable cannot (or it seems not to) define
singals directly: To define signals, the class must inherit from QObject, and that seems to be interferring with QRunnable.

After outsourcing the singnals (`finished`, e.g.) into its own QObject-based class, it worked as expected.

See https://www.pymadethis.com/article/multithreading-pyqt-applications-with-qthreadpool/ for a good explanation and example.

22.10.2018 - Idea collection
-----------------------------

Today I did not program much - I just found / read some new Qt concepts:

* `QSetting`: This is an easy-to-use mechanism for storing / reading application settings in a platform-independant way.
  I will use this mechanism for all settings-related things.
  @see http://doc.qt.io/qt-5/qsettings.html
* QML: I just read about the QML architecture as an alternative to widget-based UI creation: QML is an own language
  by itself to define UIs including interactions, which then can be loaded / connected to C++/python code.
  Start here: http://pyqt.sourceforge.net/Docs/PyQt5/qml.html and here: http://doc.qt.io/qt-5/qmlapplications.html
  It MAY be a bit complex to start with - I have to read some more first.
* The alternative is a QWidget based architecture, but using .ui files (from the visual QtCreator / QtDesigner).
  I installed qt5-qtdesigner from macports, which allows to create .ui files. For integrating them in python,
  see here: https://stackoverflow.com/questions/2398800/linking-a-qtdesigner-ui-file-to-python-pyqt#2500905, and
  the official PyQt doc: http://pyqt.sourceforge.net/Docs/PyQt5/designer.html

After reading a bit about QML and QWidget based approaches, I think I go for the QWidget Approach using QtDesigner and .ui-files.
For desktop-based apps, it seems to be the easier / better approach.


20.10.2018 - Qt Basics
-------------------------

Today I learned the core concepts of Qt, and how to use them via PyQt. What I learned so far:

* QWidget: The base UI class: All UI widgets are QWidgets. A QWidget has a layout, and the layout contains
  child widgets.
* Slots / Signals: Others will call them Events and Listeners, but the concept is the same: Components can offer
  signals, which can be consumed or "directed" to slots (which are the event listener functions).
  * Signals must be defined class wide with `pyqtSignal()`
  * Slots MAY be defined as class methods and annotated via `@pyqtSlot()`

### The Manager

I decided to de-couple most of the "background service" functionality into Service classes, with a singleton Manager to
get access to them.
A first service is the `MPlayer` service, which is a derived `QMediaPlayer`, to manage the whole play / playlist management in a
central location, decoupled from UI components.

The Manager class is available as singleton Manager object. To access the services, I decided to make them available on-demand
by using Python "Properties":

Python properties: you can define access methods for private class attributes using "properties":
I decieded to define properties to access the singleton service instances as a Getter property. I learned about the
`@property` decorator, which defines getter/setter for a private class attribute. Very neat!

### The first UI components - LogWin and PlayerWidget

I created the first UI components:

* LogWin is a window showing a simple text panel that contains all log entries that are produced: It connects to the Logger class
  via signal/slot mechanism, and outputs the logged messages in the text fields.

* PlayerWidget is a panel showing the acutual playing song, with play controls (play, pause, stop, duration, seek bar).
  It listens (via slots) on signals from the MPlayer service.
  I decided in the same time to ONLY use the concept of Playlists - Qt already offers that concept with `QMediaPlaylist`.
  I will use that feature thourough the application.


19.10.2018 - first steps
--------------------------

Before I really started I played a bit with the project structure - How do I organize the Python files / classes?
I want to organize things in a OO way, so use OO classes where ever possible.

The easiest way that I figured out is to keep all classes in a folder structure, one class per .py file, while those class files acts as
python modules at the same time - Instead of explicitely creating real packages with a `__init__.py` file, I decided to just
drop them in folders: That way I can use them as python modules without further configs.

So I came up with the following structure:

```
./
 +-- classes/
 | +-- [sub-folder]/[Class].py
 +-- app.py
```

app.py is the main program, all other files are going into sub-folders in classes/.


18.10.2018 - the beginning
----------------------------

This is the day I start LMP "Lexus Music Player". The main motivation for this project is to learn Qt, in combination with
Python. So I searched for a useful project that can be implemented as a "classic" standalone UI application, which
brought me to the idea of a music player - because iTunes sucks!

I started writing a very brief requirements spec down - just some ideas that came to my mind.

### First things first - pip, venv and Qt as requirement

I started by setting up a rudimentary virtual env - python3 has this already included, and it is really easy to use:

`python3 -m venv folder/`

then

`source folder/bin/activate`

and your're ready to go.

Then installing Qt with pip was really simple:

`pip install PyQt5`
and for writing a requirements file:
`pip freeze > requirements.txt`

Voilà!

### First steps with Qt

Then I did a very brief PyQt Hello World - no surprises here: It just ran out of the box.


13.04.2019 - Switching to JavaScript / Electron
-------------------------------------------------

I decided to stick to what I already know: Web technologies. So I decided that I switch to:

* Electron as an Application platform
* VueJS as a JavaScript framework
* Bootstrap (with VueJS) as a CSS base framework

After initial research I found that a lot of boilerplate is needed, as usual :-)

* To make use of Single File Components in VueJS, I need a bundler. So I use webpack for that
* So first things first: I need to set up the whole webpack stack / config to have:
  * single file vuejs components
  * sass / css compiling within these components
  * have one bundle entry point for my main html

This will take my today's time frame, I guess.

So I have implemented a very first proof-of-concept already:

* all build config is done (webpack mainly)
* FontAwesome is integrated via npm / build via webpack
* proof-of-concept audio player is working

As a next step I will design the main layout: always available side menu, always visible player (actual song), main window (will
eventually show songs / library).

19.05.2019
-----------

Goal: create a Player component, which is playing / displaying the actual song and controls:
- play, pause, stop, progress etc
- time info
- song info

This implies the definition of a Song model.

Progress so far:
- implemented Vuex with a global app state. Handles one song play state for now.
- created a PlayerService: a singleton player service that handles playing the actual song.
  It commits the relevant state changes when playing / changing song etc.
- The Player view listens to the global state and allows controlling the play.
- I organised the store into modules, to better separate them: For now, there is there is the
  'actualSong' module, so the store contains of 'store.actualSong.*' for the actual playing song.
- Player component / PlayerService already supports loading, start/stop/pause and seeking a song! Wow,
  that was not so hard after all!

Then I began experimenting with recursively walking a file tree to create an audio file index.
In electron apps it is possible to access also node.js-own modules like 'fs' or 'pat^'. In the render
process, this can be aquired using "window.require()".
I use the walkdir and mime modules to walk and filter audio files. A first experiment works flawlessly.

Also, reading ID3 tags seems to work in a first experiment, using the simple node-id3 library. Great! The biggest hurdles are already taken...

This lib is not able to parse MP4 files. It seems there is another one: mp4js, which I will try another day.

21.05.2019
--------------

yesterday I proof-of-concept the recursive file analyzing. I used walkdir asynchronously in the render thread.
This seems not to be optimal: I have to sync-require the packages in the Render thread, using window.require(), to
have access to nodejs-only modules. I want to move those background jobs to the main thread instead,
using inter-process-communication with ipcMain / ipcRenderer.

Target achieved :-) The inspection process is now done in the main thread,
while the UI only fires / listen to main thread events.

Refactor: The sync process should be initiated / listened to somewhere
globally, and also a global syncing state should be set during this time.
Now it is still done locally in the Settings view, which will get removed
when the UI changes.

26.05.2019
----------

Today I created a wrapper around the ipcRenderer.send() / ipcMain.on() mechanism,
to make "RPC" calls (not quite correct, but let's stick by that name) to the
main thread easier.

I created a gist for future usage, maybe I will publish it as an NPM module some day: https://gist.github.com/bylexus/062e77b0ed2af3b516d8cc4d34d1d085
