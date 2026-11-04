| Command | What you can do with it |
| --- | --- |
| `lpstat -p -d` | List printers and the default destination. |
| `lpstat -t` | Inspect printing system status. |
| `lpoptions` | Inspect printing options. |
| `lpoptions -p PRINTER -l` | List a printer's supported options. |
| `lp -d PRINTER FILE` | Submit a file to a printer. |
| `lpq` | Inspect the default print queue. |
| `mailq` | List queued mail through the installed mail system. |
| `postqueue -p` | List the Postfix mail queue. |
| `postconf -n` | Read non-default Postfix configuration. |
| `exim -bp` | List Exim queued messages. |
| `ffmpeg -version` | Print the FFmpeg version. |
| `ffprobe -v error -show_format -show_streams MEDIA_FILE` | Inspect a media file's format and streams. |
| `ffmpeg -i INPUT_FILE OUTPUT_FILE` | Transcode media into a new output file, subject to format support. |
| `magick identify IMAGE_FILE` | Inspect an image's dimensions and metadata. |
| `magick INPUT_IMAGE -resize 800x800 OUTPUT_IMAGE` | Resize an image to fit within 800 by 800 pixels. |
| `pactl info` | Inspect PulseAudio-compatible server information. |
| `pactl list short sinks` | List audio output sinks in a compact table. |
| `wpctl status` | Inspect PipeWire audio devices and routing through WirePlumber. |
| `aplay -l` | List hardware playback devices. |
| `arecord -l` | List hardware recording devices. |
