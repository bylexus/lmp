LMP - Lexus Music Player
==========================

A learning project for myself.

Learning Objectives
--------------------

With this project, I want to refresh / learn the following things:

* python, especially how to organize a project, dependencies, virtual envs
* Project organization: How to organize files / modules / packages
* QT, with python, so PyQT
* Play music with Python / QT
* Handle MP3 tags in a (memory) DB


Planned Features
-------------------

This is an unordered list of features that MAY be implemented some day - in unknown releases.

* Plays sound files (mp3, aac, wav, ogg, ...?)
* can be started with file(s) from command line
* folder browser (no file index)
* Index browser (by title, album, interpret)
* search (index and file-based)
  * simple "google" search
  * specific by attributes
  * sophisticated and/or combination search
* Creates a file index:
  * parses folder tree
  * extracts meta infos from files (mp3 tags etc)
  * stores meta info as well as file hash
  * meta infos: title, album, interpret, length, genre ....?
  * file index is stored in a in-memory-db for speed, and stored using sqlite backup api back to disk.
  * indexing is taking place in the background
* Player supports playing, pausing, stopping, seeking
  * Always plays a "playlist", either a user playlist or an internal one (all, single song)
  * play in order, or random
* Playlists: Create playlists, add songs to it
  * internal playlists, always available:
    * all songs
    * actual song
    * on-the-fly playlist (e.g. if playing a single album)

Dev Notes
--------------

* Python >= 3.7 needed
* Build a Pyhton Virtual Env:
  * `python3 -m venv ./`
  * `source bin/activate`
* Install requirements:
  * `pip install -r requirements.txt`
* Freeze requirements:
  * `pip freeze > requirements.txt`
