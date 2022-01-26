#!/usr/bin/env python3
import os
from pathlib import Path


class CheckPathForUpdates:
    old_mtime: float = 0

    def __init__(self, path: Path, mtime_file: Path = Path('.mtime')):
        self.target = path
        self.mtime_file = mtime_file

        if self.mtime_file.exists():
            try:
                self.old_mtime = float(self.mtime_file.read_text())
            except ValueError:
                pass

    def has_this_updated(self):
        mtime: float = self.target.stat().st_mtime
        self.mtime_file.write_text(str(mtime))
        return mtime > self.old_mtime


lib_check = CheckPathForUpdates(Path('lib'))
if lib_check.has_this_updated():
    exit(0)
else:
    exit(1)
