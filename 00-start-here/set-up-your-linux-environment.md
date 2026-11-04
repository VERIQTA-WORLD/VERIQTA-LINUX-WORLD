# Set up your Linux learning environment

Use an environment whose scope matches the exercise. For full-host administration, a disposable Linux VM with a working console provides a recoverable place to learn. Obtain the image from the distribution's official source and follow its installation and image-verification instructions.

## Match environment to the task

| Environment | Useful for | Important boundary |
| --- | --- | --- |
| Disposable Linux VM | Host services, networking, mounts and boot observations | Keep console access and the stated recovery/snapshot procedure |
| Linux container | Package/userland and process-isolation study | Host kernel, boot, devices and full service-manager behavior are different |
| Existing workstation | Selected read-only observations and temporary-file exercises | Your data and active work make destructive experiments inappropriate |
| Non-Linux host | Exercises explicitly described and recorded as portable | Portable success does not establish Linux-specific behavior |

Do not repartition, dual-boot, replace an existing OS or modify real cloud resources just to follow an introductory file exercise. The planned desktop collection will need its own tested installation procedures.

## Prepare recovery and prerequisites

Record the target distribution/release, architecture, image source, credentials storage and console route. Use an ordinary account for normal work. Identify which later exercises require authorized administrative access; do not grant unrestricted privileges to avoid understanding an error.

A VM snapshot can be useful for a lab reset, but it is not automatically an independent or application-consistent backup. Know which data the reset discards. Keep personal credentials and important files outside disposable experiments.

On the intended Linux VM, gather a baseline:

```bash
cat /etc/os-release
uname -r
uname -m
id
bash --version
python3 --version
```

Record actual results. Install missing prerequisites only through that distribution's supported package workflow after reading the exercise. Containers/minimal images may not include Bash, Python or systemd.

## Start with a temporary-file exercise

In an ordinary Bash shell where mktemp is available:

```bash
intro_lab=$(mktemp -d)
printf 'Linux World practice\n' > "$intro_lab/note"
cp "$intro_lab/note" "$intro_lab/copy"
cmp -- "$intro_lab/note" "$intro_lab/copy"
printf 'comparison status: %s\n' "$?"
cat "$intro_lab/copy"
```

Expect comparison status 0 and the original text. If the result differs, stop and inspect the actual error before continuing. This exercise creates no host service or privileged setting.

Cleanup after confirming the temporary paths:

```bash
rm -i -- "$intro_lab/note" "$intro_lab/copy"
rmdir -- "$intro_lab"
```

[Lab safety](linux-lab-safety.md) · [Distribution selection](../07-linux-distributions/choosing-a-linux-distribution.md) · [Start here](README.md)
