import sys
import re
import os

if len(sys.argv) < 2:
    print("usage: romance_patch.py path_to_cyberpunk.exe")
    exit()

def craft_signature_regex(aob):
    signature = b""
    for hexstr in aob.split(" "):
        if "?" in hexstr:
            signature += b"."
        else:
            signature += re.escape(chr(int(hexstr, 16))).encode("charmap")
    
    return signature

def sigscan(data, aob):
    regex = craft_signature_regex(aob)
    results = []
    for result in re.finditer(regex, data):
        results.append(result.start())
    return results

def patch(data, offset, what):
    print("patching %s -> %s @ %X" % (" ".join([ '%02X' % b for b in data[offset:offset+len(what)] ]), " ".join([ '%02X' % b for b in what ]), offset))
    data[offset:offset+len(what)] = what

exe_path = sys.argv[1]
data = None

with open(exe_path, mode="rb") as file:
    data = bytearray(file.read())

# scan "40 53 48 83 EC 20 48 8B 01 48 8B D9 FF 90 18 01 00 00"
results = sigscan(data, "40 53 48 83 EC 20 48 8B 01 48 8B D9 FF 90 ?? ?? ?? ?? 84 C0 ?? 18")
assert len(results) == 2, "2 scan results expected"

# patch
for offset in results:
    patch(data, offset, b"\xB0\x01\xC3\x90\x90\x90") # mov al, 1; ret; nop; nop; nop

# backup
old_path = exe_path + ".old"
os.rename(exe_path, old_path)
print("%s renamed to %s" % (exe_path, old_path))

# patch
with open(exe_path, "wb") as file:
    file.write(data)
print("patched file saved to %s" % exe_path)

print("done!")



    


