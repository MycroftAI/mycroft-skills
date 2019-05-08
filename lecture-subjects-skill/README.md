## Lecture Subjects
Tells you what your lecture is about

## Description
When asked what kind of lecture there is today, mycroft answers with the right subject. this works as a teaching example for home assistants.

In "dates.txt" the user puts dates for upcoming lectures with some requirements:
-one date per line
-in the format YYYYMMDD
-in the right order, with the first upcoming lecture date highest on the list, the second lecture date second and so on.

The user can modify the .dialog files to match the lectures. Files will be named "lecture1", "lecture2" and so on. 
Observe that the amount of lecture.dialog files must match the amount of dates in "dates.txt". Otherwise an error will occur.

If '*' is put on the first line of "dates.txt", a default dialog line will be used.
If the date of today cannot be found in "dates.txt", nolecture.dialog will be used. This means that there is no lecture today.



## Examples
 - "What is the subject of the lecture"
 - "What theme does the lecture have"

## Credits
Viljanen


