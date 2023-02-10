
**Contents** <a name="Contents"></a>
* [Automating backups](#Automating-backups)
* [python](#python)

[Back to Contents](#Contents)

## Automating backups
- If you’re using your Linux system to work on an important project, you can create a shell script that automatically takes snapshots of specific directories. Designating these directories in a config- uration file allows you to change them when a particular project changes. This helps avoid a time- consuming restore process from your main archive files.

- Obtaining the required functions;
The workhorse for archiving data in the Linux world is the tar command. The tar command is used to archive entire directories into a single file. Here’s an example of creating an archive file of a working directory using the tar command:
```
$ tar -cf archive.tar /home/deolu/Project/*.* tar: Removing leading '/' from member names
$
$ ls -l archive.tar
-rw-rw-r--. 1 deolu deolu 51200 Aug 27 10:51 archive.tar $
```
- To get rid of that message in the script. I can accomplish this by redirecting STDERR to the /dev/null file;
```
$ tar -cf archive.tar /home/deolu/Project/*.* 2>/dev/null $
$ ls -l archive.tar
```
- Because a tar archive file can consume lots of disk space, it’s a good idea to compress the file. I can do this by simply adding the -z option. I should be sure to use the proper file extensions to denote that the file is a tarball. Either .tar.gz or .tgz is fine.
```
$ tar -zcf archive.tar.gz /home/deolu/Project/*.* 2>/dev/null $
$ ls -l archive.tar.gz
```
- Now I have the main component for your archive script completed.

[Back to Contents](#Contents)