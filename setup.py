import sys

import os
from pathlib import Path
from setuptools import setup

py2exe_build = False
py2app_build = False

if "py2exe" in sys.argv:
    try:
        import py2exe

        py2exe_build = True
    except ImportError:
        print("Cannot find py2exe")
elif "py2app" in sys.argv:
    py2app_build = True

requirements = [
    "PyQt5 == 5.10.1",
    "gitpython",
    "tinydb",
    "requests",
    "requests-cache"
]

test_requirements = [
    'pytest',
    'pytest-cov',
    'pytest-faulthandler',
    'pytest-mock'
]

import anchor

app_name = anchor.__appname__
version = anchor.__version__
description = anchor.__description__

tmp_package_dir = Path(os.getcwd()).joinpath("tmp-packaging")
dist_dir = tmp_package_dir.joinpath('dist').as_posix()
bdist_dir = tmp_package_dir.joinpath('build').as_posix(),

APP = ['anchor/application.py']

if py2app_build:
    py2app_options = {
        'iconfile': 'packaging/data/icons/anchor.icns'
    }

    extra_options = dict(
        app=APP,
        options={'py2app': py2app_options},
    )
else:
    extra_options = dict()

setup(
    name=app_name,
    version=version,
    description=description,
    author="NL",
    author_email='info@deskriders.dev',
    url='https://github.com/namuan/anchor-app',
    packages=[
        'anchor',
        'anchor.ui',
        'anchor.ui.generated',
        'anchor.ui.presenters',
        'anchor.ui.themes',
        'anchor.ui.widgets',
        'anchor.core',
        'anchor.external',
        'anchor.model',
        'anchor.images',
        'anchor.styles'
    ],
    package_data={
        'anchor.images': ['*.png'],
        'anchor.styles': ['*.qss']
    },
    entry_points={
        'gui_scripts': [
            'context=anchor.application:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='context focused workflow',
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    **extra_options
)

if py2app_build:
    print('*** Removing unused Qt frameworks ***')
    framework_dir = os.path.join(dist_dir, "anchor.app/Contents/Resources/lib/python{0}.{1}/PyQt5/Qt/lib".format(
        sys.version_info.major, sys.version_info.minor))
    frameworks = [
        'QtDeclarative.framework',
        'QtHelp.framework',
        'QtMultimedia.framework',
        'QtNetwork.framework',
        'QtScript.framework',
        'QtScriptTools.framework',
        'QtSql.framework',
        'QtDesigner.framework',
        'QtTest.framework',
        'QtWebKit.framework',
        'QtXMLPatterns.framework',
        'QtCLucene.framework',
        'QtBluetooth.framework',
        'QtConcurrent.framework',
        'QtMultimediaWidgets.framework',
        'QtPositioning.framework',
        'QtQml.framework',
        'QtQuick.framework',
        'QtQuickWidgets.framework',
        'QtSensors.framework',
        'QtSerialPort.framework',
        'QtWebChannel.framework',
        'QtWebKitWidgets.framework',
        'QtWebSockets.framework']

    for framework in frameworks:
        for root, dirs, files in os.walk(os.path.join(framework_dir, framework)):
            for file in files:
                os.remove(os.path.join(root, file))
