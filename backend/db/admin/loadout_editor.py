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
        self.setWindowTitle("Loadout Editor")
        self.resize(600, 400)

        self._db = JSONDatabaseEngine()
        self._selected_player = None

        layout = QFormLayout()
        self.setLayout(layout)

        player_field = QComboBox()
        usernames = sorted([p.username.lower() for p in self._db.select_players()])
        player_field.addItems(usernames)
        player_field.setCurrentIndex(-1)
        player_field.currentTextChanged.connect(self._on_select_player)
        layout.addRow(QLabel("Player"), player_field)

        self._loadout_field = QComboBox()
        self._loadout_field.addItems(sorted([str(w) for w in Weapon]))
        self._loadout_field.setEditable(True)
        self._loadout_field.setCurrentIndex(-1)
        self._loadout_field.currentTextChanged.connect(self._on_select_loadout)
        layout.addRow(QLabel("Loadout"), self._loadout_field)

        self._game_field = QComboBox()
        self._game_field.addItems([g.value for g in Game])
        self._game_field.setCurrentIndex(-1)
        layout.addRow(QLabel("Game"), self._game_field)

        self._attachment_fields = {
            "Muzzle": self._add_attachment_field(Muzzle),
            "Barrel": self._add_attachment_field(Barrel),
            "Laser": self._add_attachment_field(Laser),
            "Optic": self._add_attachment_field(Optic),
            "Stock": self._add_attachment_field(Stock),
            "Underbarrel": self._add_attachment_field(Underbarrel),
            "Ammunition": self._add_attachment_field(Ammunition),
            "Rear Grip": self._add_attachment_field(RearGrip),
            "Perk": self._add_attachment_field(Perk),
            "Trigger Action": self._add_attachment_field(TriggerAction),
        }

        self._source_field = QLineEdit()
        layout.addRow(QLabel("Source"), self._source_field)

        self._command_field = QLineEdit()
        self._message_field = QLineEdit()

        command_layout = QHBoxLayout()
        command_layout.addWidget(self._command_field)
        command_layout.addWidget(self._message_field)
        command_layout.setContentsMargins(0, 0, 0, 0)

        command_widget = QWidget()
        command_widget.setLayout(command_layout)
        layout.addRow(QLabel("Command"), command_widget)

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self._on_submit)
        layout.addWidget(submit_button)

    def _add_attachment_field(self, enum: EnumMeta):
        field = QComboBox()
        values = [str(attachment) for attachment in enum]
        sorted_values = sorted(values)
        field.addItems(sorted_values)
        field.setCurrentIndex(-1)
        self.layout().addRow(QLabel(enum.__name__), field)
        return field

    def _on_select_player(self, username: str):  # TODO: add additional loadouts
        self._clear_editor()
        self._selected_player = self._db.select_player(username)

    def _on_select_loadout(self, name: str):
        self._clear_editor()

        if not self._selected_player:
            return

        loadout = self._selected_player.loadouts.get(name)

        if not loadout:
            return

        game_index = self._game_field.findText(loadout["game"])
        self._game_field.setCurrentIndex(game_index)
        self._source_field.setText(loadout["source"])

        for k, v in loadout["attachments"].items():
            field = self._attachment_fields[k]
            index = field.findText(v)
            field.setCurrentIndex(index)

    def _clear_editor(self):  # TODO: clear loadout field?
        [field.setCurrentIndex(-1) for field in self._attachment_fields.values()]
        self._game_field.setCurrentIndex(-1)
        self._source_field.setText("")
        self._command_field.setText("")
        self._message_field.setText("")

    def _on_submit(self):  # TODO: validation
        username = self._selected_player.username.lower()

        loadout = self._loadout_field.currentText()
        attachments = {k: v.currentText() for k, v in self._attachment_fields.items() if v.currentText() != ""}

        game = self._game_field.currentText()
        source = self._source_field.text()
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
        print(f"[{username}] Added {loadout}: {player.loadouts[loadout]}")


if __name__ == '__main__':
    _start_ui()
