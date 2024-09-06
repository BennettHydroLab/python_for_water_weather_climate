mkdir -p /home/jovyan/.local/share/code-server/extensions
code-server --install-extension ms-python.python \
    && code-server --install-extension ms-toolsai.jupyter \
    && code-server --install-extension charliermarsh.ruff \
    && code-server --install-extension catppuccin.catppuccin-vsc
