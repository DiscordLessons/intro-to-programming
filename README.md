# intro-to-programming


## Getting Started With the Requests Library
```sh
pip install requests
```


## Visual Studio Code Notes

- To use a keyboard binding to toggle focus between editor and terminal:
    1. ctrl+shift+p
    2. Select "Preferences: Open Keyboard Shortcuts (JSON)
    3. Add the following entry within the brackets:
    ```sh
    // Toggle between terminal and editor focus
    { "key": "ctrl+`", "command": "workbench.action.terminal.focus"},
    { "key": "ctrl+`", "command": "workbench.action.focusActiveEditorGroup", "when": "terminalFocus"}
    ```
    4. Now, ctrl+` will toggle focus.