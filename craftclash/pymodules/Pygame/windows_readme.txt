Latest Windows x64 (64-bit) installers for Pygame 1.9.2
=======================================================

- pygame-1.9.2a0-hg_8d9e6a1f2635+.win-amd64-py2.7.msi (5,095,424 bytes) (8)
- pygame-1.9.2a0-hg_8d9e6a1f2635+.win-amd64-py3.4.msi (4,956,160 bytes) (7,8)

Latest Windows x86 (32-bit) installers for Pygame 1.9.2
=======================================================

changeset ea3b3bb8714a:

- pygame-1.9.2a0-hg_ea3b3bb8714a.win32-py2.7.msi (5,062,656 bytes)  (8)
- pygame-1.9.2a0-hg_ea3b3bb8714a.win32-py3.4.msi (4,939,264 bytes)  (7,8)

Latest dependencies for Windows
===============================

- prebuilt-x86-pygame-1.9.2-20150922.zip (2,595,274 bytes) 32-bit  (9,10)
- prebuilt-x64-pygame-1.9.2-20150922.zip (2,792,038 bytes) 64-bit  (9,10)
- prebuilt-1.9.2-src-20150907.zip (30,491,639 bytes)

Older Windows x86 installers for Pygame 1.9.2a0 (changeset given in file name)
==============================================================================

changeset 5974ff8dae3c+:

- pygame-1.9.2a0-hg_5974ff8dae3c+.win32-py3.4.msi (4,776,448 bytes)   (7,8)

changeset 56e0eadfc267:

- pygame-1.9.2a0-hg_56e0eadfc267.win32-py3.3.msi (4,227,072 bytes)   (4,6)

changeset 12de2da43ecb:

- pygame-1.9.2a0-12de2da43ecb.win32-py3.3.msi (4,227,072 bytes)  (4,6)

changeset 851743cb4c5a:

- pygame-1.9.2a0.win32-py2.7.msi (3,948,544 bytes)  (4,5)
- pygame-1.9.2a0.win32-py3.3.msi (3,817,472 bytes)  (4,6)

Older Windows x86 installers for Pygame 1.9.2pre
================================================

changeset c3da16d323a1:

- pygame-1.9.2a0.win32-py3.2.msi (4,227,072 bytes)

Older Windows x86 installers for Pygame 1.9.1
=============================================

- pygame-1.9.1.win32-py2.7.msi (3,194,880 bytes)

Installers for Python versions other than 2.7 and 3.4 will not
be built unless requested.

Older Pygame x86 dependencies for Windows
=========================================

- prebuilt-pygame1.9.2-msvcr90-win32.zip (2,058,252 bytes)  (1)
- prebuilt-pygame1.9.2a0-msvcr90-win32.zip (5,338,404 bytes)  (2)
- prebuilt-pygame1.9.2pre-msvcr100-win32.zip (1,903,169 bytes)  (3)

The external libraries required to build Pygame for Pythons 2.6 and up.
Just unzip the prebuilt directory into the root Pygame working directory
and run python config.py. Answer Y to use prebuilt.

- prebuilt-pygame1.9.0-msvcr90-win32.zip (1,822,375 bytes)

The prebuilt included with Pygame 1.9.1 release.

- prebuilt-1.9.2-src.zip (33,036,706 bytes)

Library source code from which the Pygame 1.9.2 dependency binaries were built.



(1) For Python versions 2.6 - 3.2. These libraries were compiled with MinGW. They
    work when Pygame is built with Visual Studio 2009.

(2) For Python 2.6 to 3.2. This version includes the ffmpeg libraries needed to
   build the experimental pygame._movie module. However, it is outdated, and
   pygame._movie is buggy and not built by default.
   Use prebuilt-pygame1.9.0-msvcr90-win32.zip instead.

(3) For Python 3.3. These libraries were compiled with Visual Studio 2010 Express;
    they are untested with a MinGW built Pygame.

(4) Does not pass all Pygame unit tests.

(5) Built with Visual Studio 2009 Express.

(6) Built with Visual Studio 2010 Express.

(7) Fails only one UCS-4 related test for the font module.

(8) Uses the msvcrt MinGW built dependencies (see below)

(9) Built with MinGW; linked to msvcrt.dll. Only use with Pygame commit ea3b3bb8714a
    or later (2015-09-07)
(10) Includes stdint.h for Python 2.7 (MSVC 9.0)
