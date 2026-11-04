#!/usr/bin/env python3
"""Execute nine bounded portable walkthroughs; does not certify GNU/Linux behavior.

Runs examples that create temporary files and confirms their cleanup. Supplies
confirmation replies only to those isolated example scripts. No sudo is used.
"""
from pathlib import Path
import re, subprocess, tempfile, os
base=Path(__file__).resolve().parents[1]/'04-commands-and-cheat-sheets'
selected={
 'files-and-directories/navigation-commands.md':['/notes/week 1'],
 'files-and-directories/file-management-commands.md':['renamed.txt'],
 'files-and-directories/file-search-commands.md':['notes one.txt'],
 'text-processing/grep-reference.md':['2:ERROR disk','3:ERROR network','previous status: 1'],
 'text-processing/sed-reference.md':['mode=test','label=test-test','mode=dev'],
 'text-processing/awk-reference.md':['api 8','web 17'],
 'text-processing/pipes-and-redirection.md':['apple','pear','pipeline status: 1'],
 'backup-and-recovery/tar-reference.md':['note'],
 'backup-and-recovery/rsync-reference.md':['note'],
}
for name,expected in selected.items():
    code=re.search(r'^```bash\n(.*?)^```',(base/name).read_text(),re.M|re.S)[1]
    variable=re.search(r'^(\w+)=\$\(mktemp -d\)',code)[1]
    code=code.replace(f'{variable}=$(mktemp -d)',f'{variable}=$(mktemp -d)\nprintf "CHECK_PATH:%s\\n" "${variable}"',1)
    code=re.sub(r'^(cmp .+)$',r'\1 || exit 91',code,flags=re.M)
    with tempfile.NamedTemporaryFile('w',suffix='.sh',delete=False) as f:
        f.write(code); script=f.name
    try:
        result=subprocess.run(['bash',script],input='y\n'*20,text=True,capture_output=True,timeout=15)
        assert result.returncode==0, (name,result.stderr)
        assert all(e in result.stdout for e in expected),(name,result.stdout)
        created=re.search(r'CHECK_PATH:(.+)',result.stdout)[1]
        assert not Path(created).exists(),(name,'cleanup incomplete',created)
        assert 'No such file' not in result.stderr,(name,result.stderr)
        print('PASS',name,'expected text, comparisons and cleanup')
    finally:
        os.unlink(script)
