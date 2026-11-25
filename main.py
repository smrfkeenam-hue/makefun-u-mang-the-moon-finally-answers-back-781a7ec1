import os

ENTRY = "You howl, you wish, you promise me the moon at 2 a.m. — four billion years of this, and not one of you has ever wished me a good night back."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(out_dir + "/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
