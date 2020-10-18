<h4 align="center"> ezdump, a simple installer script !</h4>

## About

```
Please note that this script is primarely aimed at Epitech students who want to quickly install anything they might need, though you can use it if you are not an epitech student.
```

---

This script aims to install quickly and simply anything a first-year Epitech student might need on his fresh Linux install.
Altough it is a bit opinionated, you can require the script to install specific dotfiles, and programs quite easely.
The script currently works on:
- debian-type OS's (Ubuntu, Debian, POP OS, Kali, Parrot OS, etc...)
- archlinux-type OS's (Archlinux, BlackArch, Artix Linux, etc...)
- fedora
- openSUSE

If you're using another distribution, or you have a suggestion, you can of course fork the project, and update it.
This simple bash script is *not* POSIX-compliant, and comports some *bashisms*, you need to make sure you are in a bash shell.

## Features

- minimalistic dotilfes installer, through a repository
- package installer, read from a file
- colored output
- install routine for Epitech-required Criterion, and CSFML
- install routine for an alternate package manager, such as yay, snap or flatpak
- disable the system-beep from the motherboard when you start up your computer

## How do I use it ?

You can check the script usage by doing:
```bash
sudo ./ezdump -h
```

To set a custom dotfiles repository:
```bash
sudo ./ezdump -d [url]
```

To set a custom package list: (Please refer to the `pkgs` file)
```bash
sudo ./ezdump -f [file path]
```

If no arguments are provided, the script will install my dotfiles, along with the packages listed in `pkgs`.
