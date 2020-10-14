import cx_Freeze

executables = [cx_Freeze.Executable("Sneaky Snake.py")]
cx_Freeze.setup(
    name = "Sneaky Snake",
    options = {"build_exe":{"packages":["pygame"], "include_files":["apple.png", "head.png", "body.png", "icon.png"]}},
    description = "Sneaky Snake Game",
    executables = executables
    )

                
