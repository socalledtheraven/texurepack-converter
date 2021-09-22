import os, shutil

def fix_mcmeta(version):
    mcmeta_file = open(r"pack.mcmeta", "w+")
    for line in mcmeta_file:
        if '"pack_format":' in line:
            current_version = mcmeta_file.readline()
            current_version = int(current_version[-1])
            mcmeta_file.write('"pack_format": {}'.format(version))
    if current_version > 7:
        print("This version is currently unsupported")

def fix_models():
    shutil.copytree("/assets/", "/packname/assets/minecraft", dirs_exist_ok=True)


def main():
    user_version = int(input("What version do you want the pack to work for?"))
    fix_mcmeta(user_version)


