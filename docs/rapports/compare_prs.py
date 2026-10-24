#!/usr/bin/env python3

import subprocess
import sys
import tempfile
from pathlib import Path


def git(args, cwd=None, check=True):
    proc = subprocess.run(
        ["git", *args],
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if check and proc.returncode != 0:
        sys.stderr.write(proc.stdout)
        raise SystemExit(proc.returncode)
    return proc.returncode, proc.stdout


def names(base, tip):
    code, out = git(["diff", "--name-only", f"{base}...{tip}"])
    return [line for line in out.splitlines() if line]


def shortstat(base, tip):
    code, out = git(["diff", "--shortstat", f"{base}...{tip}"])
    return out.strip()


def conflict_paths(base, tip):
    code, out = git(
        ["merge-tree", "--write-tree", "--name-only", base, tip],
        check=False,
    )
    paths = []
    for line in out.splitlines():
        marker = "Merge conflict in "
        if line.startswith("CONFLICT") and marker in line:
            paths.append(line.split(marker, 1)[1].strip())
    return code, paths


def sequential(base, first, second):
    with tempfile.TemporaryDirectory(prefix="pr-compare-") as tmp:
        wt = str(Path(tmp) / "wt")
        git(["worktree", "add", "--detach", wt, base])
        try:
            code, out = git(["merge", "--ff-only", first], cwd=wt, check=False)
            print(f"sequential ff {first}: exit {code}")
            print(out.strip())
            code2, out2 = git(
                ["merge", "--no-commit", "--no-ff", second],
                cwd=wt,
                check=False,
            )
            print(f"sequential merge {second}: exit {code2}")
            code3, unmerged = git(
                ["diff", "--name-only", "--diff-filter=U"],
                cwd=wt,
                check=False,
            )
            paths = [line for line in unmerged.splitlines() if line]
            print(f"sequential unmerged: {len(paths)}")
            for path in paths:
                print(path)
            git(["merge", "--abort"], cwd=wt, check=False)
            return paths
        finally:
            git(["worktree", "remove", "--force", wt], check=False)


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "origin/main"
    left = sys.argv[2] if len(sys.argv) > 2 else "origin/cursor/coherence-objectives-dbc9"
    right = sys.argv[3] if len(sys.argv) > 3 else "origin/claude/lucid-edison-imzaab"
    print(f"base {base} {git(['rev-parse', base])[1].strip()}")
    print(f"left {left} {git(['rev-parse', left])[1].strip()}")
    print(f"right {right} {git(['rev-parse', right])[1].strip()}")
    print(f"left ahead/behind {git(['rev-list', '--left-right', '--count', f'{base}...{left}'])[1].strip()}")
    print(f"right ahead/behind {git(['rev-list', '--left-right', '--count', f'{base}...{right}'])[1].strip()}")
    print(f"left shortstat {shortstat(base, left)}")
    print(f"right shortstat {shortstat(base, right)}")
    left_names = set(names(base, left))
    right_names = set(names(base, right))
    both = sorted(left_names & right_names)
    print(f"left files {len(left_names)}")
    print(f"right files {len(right_names)}")
    print(f"overlap {len(both)}")
    for path in both:
        print(f"overlap {path}")
    print(f"only right {len(right_names - left_names)}")
    for path in sorted(right_names - left_names):
        print(f"only-right {path}")
    for label, tip in (("left", left), ("right", right)):
        code, paths = conflict_paths(base, tip)
        print(f"merge-tree {label} exit {code} conflicts {len(paths)}")
        for path in paths:
            print(f"conflict-{label} {path}")
    print("sequential base then right then left")
    sequential(base, right, left)


if __name__ == "__main__":
    main()
