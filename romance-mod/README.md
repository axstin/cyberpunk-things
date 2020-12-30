# What
In theory, this should allow you to romance any of the 4 romanceable characters, regardless of player gender. Works by patching two functions in Cyberpunk2077.exe responsible for setting "*_romanceable" fact values.

# Usage

### Python
Run `python romance_patch.py <path_to_cyberpunk.exe>`

### Manual
Search for the signature `40 53 48 83 EC 20 48 8B 01 48 8B D9 FF 90 18 01 00 00` in Cyberpunk2077.exe with your favorite hex editor. There should be two results, replace the first 3 bytes of each with `B0 01 C3`

### [CyberEngineTweaks](https://github.com/yamashi/CyberEngineTweaks)
Install [CyberEngineTweaks](https://github.com/yamashi/CyberEngineTweaks) and run the following:

```lua
for i, v in next, {"judy","river","kerry","panam"} do
    Game.GetQuestsSystem():SetFactStr(v.."_romanceable", 1)
end
```

Then, save and reload your game.

# Undoing changes
To undo changes, remove changes made to Cyberpunk2077.exe and go back to a save made before the patch. If you don't want to lose progress, use CyberEngineTweaks to set the appropriate `judy_romanceable`, `panam_romanceable`, or etc. facts to 0.

# Disclaimer
Not completely tested. Patch may need to be applied before receiving certain quests (e.g. Ghost Town for Panam) in order to work.