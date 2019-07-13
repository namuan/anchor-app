#!/usr/bin/env bash
cmd_usage()
{
    echo "usage: $0 COMMAND"
    echo "commands:"
    echo "  build        invokes pyinstaller"
    echo "  shell        runs a shell"
}

cmd_build()
{
    rm -rf ./build/
    rm -rf ./dist/
    exec pyinstaller $@
}

cmd_shell()
{
    exec /bin/bash
}

case "$1" in
    build|shell)
        cmd="$1"
        shift
        cmd_${cmd} $@
    ;;
    *)
        cmd_usage
        exit 1
    ;;
esac