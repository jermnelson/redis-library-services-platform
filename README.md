[ALA]: https://github.com/jermnelson/aristotle-library-apps
[BDS]: https://github.com/jermnelson/BIBFRAME-Datastore

Redis Library Services Platform
===============================

The Redis Library Services Platform includes the 
[Aristotle Library Apps][ALA] and the 
[BIBFRAME Datastore][BDS] projects and is 
meant to coordinate continuous integration of these two projects.

## Installing
Directions for installing a standalone Redis Library Services Platform (RLSP) are available 
for a number of different platforms. The directory structure for a standalone RLSP is:

/redis-library-services-platform <- Root
 /aristotle-library-apps/
 /bibframe-datastore/
 setup.py
 run_rlsp.ps1
 run_rlsp.sh
 
   


This project also contains two light-weight web and json interfaces into the Redis
Library Services Platform. The first is a json interface to a Redis Bibliographic 
Datastore and the second is a json and html5 metadata services interface to a
scientific, cultural, social, and historical datasets. The first implementation is
a [ISA Commons](http://www.isacommons.org/) biological interface to a Redis Bibliographic
Datastore.

