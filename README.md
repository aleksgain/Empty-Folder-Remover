# Empty-Folder-Remover

A python script to delete empty (or almost empty) directories. Can be tweaked to run with or without user input, just comment out inputs and use default values. Creation inspired by switching from CouchPotato to Radarr that requires separate directories for each movie. Unfortunately, when the movie is watched and deemed unworthy of my collection and therefore deleted in Plex, directory remains, so are subtitles and other supporting files in it. Not a big deal with a small collection but a total pain when there are thousands of folders. This script takes care of the issue quickly and rather efficiently.

Script asks for user input for working directory (defaults to ./ if not specified) and min folder size (100MB if not specified). Please note that it does not scan for the size of subdirectories becasue it's not needed for my purposes.
