import storage
import gui
from ttkthemes import ThemedTk


def main():
    # 1. Hauptfenster & Theme
    root = ThemedTk(theme="equilux")

    # 2. Daten laden
    storage.load_user(root)

    # 3. GUI aufbauen
    app_interface = gui.TrainingAppGUI(root)

    # 4. Start-Checks
    if not storage.user.get("name"):
        storage.ask_new_user(root)

    app_interface.refresh_all()
    root.mainloop()


if __name__ == "__main__":
    main()

'''Nächste Schritte:
1. Wochen Ziele -Bereich definieren ansonsten geht Woche endlos
2. Scrollleiste hinzufügen für längere Übungen, aktuell per Mausrad aber nicht optimal
3. '''