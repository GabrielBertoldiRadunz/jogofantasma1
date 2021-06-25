import cx_Freeze
executables = [cx_Freeze.Executable(script="jogofantasma1.py", icon="assets/icon.ico")]

cx_Freeze.setup(
    name="Fuja do Fantasma",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files":["assets"]
    }},
    executables = executables
)