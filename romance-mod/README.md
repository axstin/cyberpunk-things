# Romance Mod
In theory, this mod should allow you to romance any of the 4 romanceable characters, regardless of player gender. Works by patching two functions in Cyberpunk2077.exe responsible for setting "\_romanceable" fact values. Best applied _before_ important romance quests/questlines are received/started.

## Usage

There are three methods that can be used to apply the mod:

#### Python Script
Run `python romance_patch.py <path_to_cyberpunk.exe>`

#### Manual Method
Search for the signature `40 53 48 83 EC 20 48 8B 01 48 8B D9 FF 90 18 01 00 00` in Cyberpunk2077.exe with your favorite hex editor. There should be two results; replace the first 3 bytes of each with `B0 01 C3`.

#### Using CyberEngineTweaks
Install [CyberEngineTweaks](https://github.com/yamashi/CyberEngineTweaks) and run the following:

```lua
for i, v in next, { "judy", "river", "kerry", "panam" } do
    Game.GetQuestsSystem():SetFactStr(v .. "_romanceable", 1)
end
```

Then, save and reload your game.

## Undoing changes
To undo changes, remove changes made to Cyberpunk2077.exe and go back to a save made before the patch. If you don't want to lose progress, use CyberEngineTweaks to set the appropriate `judy_romanceable`, `panam_romanceable`, or etc. facts to 0 instead.

## Details

The two patched functions are defined in game code as follows (pseudocode):

```cpp
bool is_river_or_judy_romanceable() {
    return !is_body_gender_male() && !is_brain_gender_male();
}

bool is_kerry_or_panam_romanceable() {
    return is_body_gender_male() && is_brain_gender_male();
}
```

They are used to set certain _romanceable facts every **game load**, like so:

```cpp
if (is_river_or_judy_romanceable()) {
    set_fact("river_romanceable", 1);
    set_fact("judy_romanceable", 1);
}
if (is_kerry_or_panam_romanceable()) {
    set_fact("kerry_romanceable", 1);
    set_fact("panam_romanceable", 1);
}
```

This code overwrites existing romance facts (retrieved from save files) if the conditions are met. Once the patch is applied, both checks return true and all facts are set every load. If the functions are patched with `B0 00 C3` instead of `B0 01 C3`, the override code is disabled.