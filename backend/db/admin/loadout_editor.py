import json
import sys
from datetime import datetime
from db.json_database_engine import JSONDatabaseEngine
from enum import EnumMeta
from model.attachment import *
from model.weapon import Weapon
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QComboBox, QFormLayout, QLabel, QHBoxLayout, QPushButton


def _start_ui():
    app = QApplication(sys.argv)
    editor = LoadoutEditor()
    editor.show()
    sys.exit(app.exec_())


class LoadoutEditor(QWidget):

    def __init__(self):
        super().__init__()
        self._db = JSONDatabaseEngine()
        self._selected_player = None

        self.setWindowTitle("Loadout Editor")
        self.resize(600, 400)
        self.setLayout(QFormLayout())

        player_field = QComboBox()
        usernames = sorted([p.username.lower() for p in self._db.select_players()])
        player_field.addItems(usernames)
        player_field.setCurrentIndex(-1)
        player_field.currentTextChanged.connect(self._on_select_player)
        self.layout().addRow(QLabel("Player"), player_field)

        self._loadout_field = QComboBox()
        self._loadout_field.addItems(sorted([str(w) for w in Weapon]))
        self._loadout_field.setEditable(True)
        self._loadout_field.setCurrentIndex(-1)
        self._loadout_field.currentTextChanged.connect(self._on_select_loadout)
        self.layout().addRow(QLabel("Loadout"), self._loadout_field)

        self._game_field = QComboBox()
        self._game_field.addItems([g.value for g in Game])
        self._game_field.setCurrentIndex(-1)
        self.layout().addRow(QLabel("Game"), self._game_field)

        attachments = [Muzzle, Barrel, Laser, Optic, Stock, Underbarrel, Ammunition, RearGrip, Perk, TriggerAction]
        self._attachment_fields = {a.get_class_name(): self._add_attachment_field(a) for a in attachments}

        self._source_field = QLineEdit()
        self.layout().addRow(QLabel("Source"), self._source_field)

        self._command_field = QLineEdit()
        self._message_field = QLineEdit()

        command_layout = QHBoxLayout()
        command_layout.addWidget(self._command_field)
        command_layout.addWidget(self._message_field)
        command_layout.setContentsMargins(0, 0, 0, 0)

        command_widget = QWidget()
        command_widget.setLayout(command_layout)
        self.layout().addRow(QLabel("Command"), command_widget)

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self._on_submit)
        self.layout().addWidget(submit_button)

        self._status_text = QLabel("")
        self.layout().addWidget(self._status_text)

    def _add_attachment_field(self, enum: EnumMeta):
        field = QComboBox()
        field.addItem("")

        values = [str(attachment) for attachment in enum]
        sorted_values = sorted(values)
        field.addItems(sorted_values)

        self.layout().addRow(QLabel(enum.get_class_name()), field)
        return field

    def _on_select_player(self, username: str):
        self._clear_editor()
        self._selected_player = self._db.select_player(username)
        self._on_select_loadout(loadout_key=self._loadout_field.currentText())

    def _on_select_loadout(self, loadout_key: str):
        self._clear_editor()

        if not self._selected_player:
            return

        loadout = self._selected_player.loadouts.get(loadout_key)

        if not loadout:
            self._source_field.setText(f"https://www.twitch.tv/{self._selected_player.username.lower()}")
            return

        game_index = self._game_field.findText(loadout["game"])
        self._game_field.setCurrentIndex(game_index)
        self._source_field.setText(loadout["source"])

        for k, v in loadout["attachments"].items():
            field = self._attachment_fields[k]
            index = field.findText(v)
            field.setCurrentIndex(index)

    def _on_submit(self):
        username = self._selected_player.username.lower()

        loadout = self._loadout_field.currentText()
        attachments = {k: v.currentText() for k, v in self._attachment_fields.items() if v.currentText() != ""}

        if len(attachments) > 5:
            self._log(f"Error: {len(attachments)} attachments selected")
            return

        game = self._game_field.currentText()
        source = self._source_field.text()

        if not game or not source:
            self._log(f"Error: required fields missing")
            return

        command = (self._command_field.text(), self._message_field.text())

        self._add_loadout(username, loadout, attachments, game, source, command)

    def _add_loadout(self, username: str, loadout: str, attachments: dict, game: str, source: str, command: tuple):
        player = self._db.select_player(username)

        player.last_updated = datetime.now().isoformat()
        player.loadouts[loadout] = {
            "game": game,
            "source": source,
            "attachments": attachments
        }

        cmd, msg = command

        if cmd:
            player.commands[cmd] = msg

        self._db.add_player(player)

        self._selected_player = self._db.select_player(username)
        self._log(f"Added {player.username}'s {loadout}:\n{json.dumps(player.loadouts[loadout], indent=4)}")

    def _log(self, message: str):
        self._status_text.setText(message)

    def _clear_editor(self):
        [field.setCurrentIndex(-1) for field in self._attachment_fields.values()]
        self._game_field.setCurrentIndex(-1)
        self._source_field.setText("")
        self._command_field.setText("")
        self._message_field.setText("")


if __name__ == '__main__':
    _start_ui()
