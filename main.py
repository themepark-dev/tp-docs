from pathlib import Path

def define_env(env):
    @env.macro
    def file_exists(filepath: str) -> bool:
        if not isinstance(filepath, str):
            return False
        filepath: Path = Path.cwd() / filepath.lstrip('/')
        return filepath.exists()
