import argparse
import sys


def main() -> int:
    ap = argparse.ArgumentParser(prog="kiln", description="Mod manager for Linux with Nexus Mods integration")
    ap.add_argument("uri", nargs="?", help="an nxm:// link (from the Nexus 'Mod Manager Download' button)")
    ap.add_argument("--register-nxm", action="store_true", help="make Kiln the nxm:// handler and exit")
    ap.add_argument("--install-desktop", action="store_true",
                    help="add Kiln to the app launcher without taking over nxm:// links, then exit")
    args = ap.parse_args()

    if args.register_nxm or args.install_desktop:
        from . import desktop
        p = desktop.register_nxm() if args.register_nxm else desktop.write_desktop_entry(False)
        print("Wrote", p)
        return 0

    from .gui import run
    return run(args.uri)


if __name__ == "__main__":
    sys.exit(main())
