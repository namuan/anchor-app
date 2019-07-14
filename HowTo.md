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

#### Releases

Make sure versions are up to date and should match in anchor/__init__.py and .travis.yml
Push the changes

Import anchor-app project in Travis
Setup GITHUB_TOKEN in Travis for both anchor-app and anchor-app-osx

After building, we should see a new Tag in anchor-app with the version number

After the release is published, change the BUILD_VERSION="0.0.1" in anchor-app-osx to match the version in anchor-app.
