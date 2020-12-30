# Save Lock Bypass

## Cheat Engine

Run Auto Assemble script:

```
aobScanModule(blah, Cyberpunk2077.exe, 0F 84 CA 00 00 00 4D)

blah:
db E9 CB 00 00 00 90
```

## File Edit

Open `Cyberpunk2077.exe` with your favorite hex editor, scan for `0F 84 CA 00 00 00 4D 8B 07`, and replace the first 6 bytes with `E9 CB 00 00 00 90`

This patch changes a `jz` to a `jmp` at `Cyberpunk2077.exe+2BF4131` (as of 1.06)