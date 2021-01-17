# rm_empty_dirs_eeb
Remove empty dirs under a specified starting path

The first and only argument to the script should be a path.
Under this path, the script will search for directories that have 0 items.
That is, if the directory has no files and no sub-directories, it will
optionally be removed.

The script will ask for confirmation once before removing all such directories.
