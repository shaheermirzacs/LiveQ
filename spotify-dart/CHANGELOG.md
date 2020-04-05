# Changelog

## 0.3.0

- unify package's Browser and IO exports, fix invalid SDK error #34
- improve static analysis health #33

## 0.2.1

- add oauth2 package for refresh flow
- fix pagination on several places
- add playlists/removeTrack
- add playlists/addTrack
- add createPlaylist
- fix my playlists
- refactor SpotifyApi classes
- upgrade json_serializable dependencies

## 0.2.0

- add token setter method for implicit grant
- add related artists
- add recently played artists
- add top tracks
- add categories
- add tracksByPlaylist
- fix currently playing

Please don't mind the weird commit history, I goofed and used rebase first and merge on the later pull requests.

## 0.1.6+3

- fix typo in tracks object
- move album model switch to model

## 0.1.5+1

- add external_ids and external_urls

## 0.1.4

- add related-artists to the artists endpoint

## 0.1.3+2

- use full Track object in search endpoint

## 0.1.3+1

- eliminate duplicate code (serializers)

## 0.1.3

- add currently playing endpoint

## 0.1.2

- make pub analyzer happy

## 0.1.1

- add search endpoint

## 0.0.9 - 0.1.0

- support Dart 2 with switch to json_serializable

## 0.0.8

- add missing _putImpl implementation to SpotifyMock

## 0.0.7

- add user's saved tracks endpoints

## 0.0.6

- add pagination support

## 0.0.5

- add user and playlist endpoints

## 0.0.4

- fix typo in artists endpoint
- add basic unit tests

## 0.0.3

- add support for albums and artists
- refactor code a little

## 0.0.1

- Initial version
