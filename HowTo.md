### HowTos

#### Generating Icns file from SVG

This will generate an icns file in packaging/data/icons/

```
$ ./mk-icns.sh $PWD/anchor/images/anchor.svg anchor
```

#### Running PyInstaller with Docker

Works for Linux

```
docker run --rm -ti -v $(pwd):/data imon/pyinstaller build packaging/pyinstaller/anchor.osx.spec
```

For Apple

```
py2app ...
```

#### Icons from

https://icons8.com/icon/pack/free-icons/ios-glyphs

#### Generate Resources

```
$ pyrcc5 -compress 9 -o anchor/resources_rc.py anchor/resources.qrc
```

#### Generate code from ui files

```
$ for i in `ls resources/ui/*.ui`; do FNAME=`basename $i ".ui"`; pyuic5 $i > "anchor/ui/generated/$FNAME.py"; done
```